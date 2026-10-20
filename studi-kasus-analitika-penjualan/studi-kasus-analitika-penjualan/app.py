import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np
from pathlib import Path

st.set_page_config(page_title="Analitika Penjualan", page_icon="📊", layout="wide")
st.title("📊 Dashboard Analitika Penjualan")
st.caption("Studi kasus: mengubah data transaksi operasional yang kotor menjadi informasi, insight, dan rekomendasi keputusan.")

DATA_PATH = Path(__file__).parent / "data" / "transaksi_penjualan_kotor.csv"

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

def clean_data(raw):
    df = raw.copy()
    df["tanggal"] = pd.to_datetime(df["tanggal"], errors="coerce", dayfirst=True, format="mixed")
    df["produk"] = df["produk"].astype("string").str.strip().str.title()
    df["kategori"] = df["kategori"].astype("string").str.strip().str.title()
    df["kota"] = df["kota"].astype("string").str.strip().str.title()
    df["jumlah"] = pd.to_numeric(df["jumlah"], errors="coerce")
    df["harga_satuan"] = pd.to_numeric(df["harga_satuan"], errors="coerce")

    # Duplikasi ID transaksi dihapus; nilai kosong dan transaksi tidak valid ditangani.
    df = df.drop_duplicates(subset=["id_transaksi"], keep="first")
    df = df.dropna(subset=["tanggal", "produk", "jumlah", "harga_satuan"])
    df = df[(df["jumlah"] > 0) & (df["harga_satuan"] > 0)]
    df["kategori"] = df["kategori"].fillna("Tidak diketahui")
    df["kota"] = df["kota"].fillna("Tidak diketahui")
    df["pendapatan"] = df["jumlah"] * df["harga_satuan"]
    return df

raw = load_data(DATA_PATH)
clean = clean_data(raw)

with st.sidebar:
    st.header("Filter analisis")
    products = ["Semua"] + sorted(clean["produk"].dropna().unique().tolist())
    selected_product = st.selectbox("Produk", products)
    cities = ["Semua"] + sorted(clean["kota"].dropna().unique().tolist())
    selected_city = st.selectbox("Kota", cities)

filtered = clean.copy()
if selected_product != "Semua":
    filtered = filtered[filtered["produk"] == selected_product]
if selected_city != "Semua":
    filtered = filtered[filtered["kota"] == selected_city]

tab1, tab2, tab3, tab4 = st.tabs(["Ringkasan", "Kualitas Data", "Prediksi", "Rekomendasi"])

with tab1:
    st.subheader("Descriptive Analytics — Apa yang terjadi?")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Transaksi valid", f"{len(filtered):,}")
    c2.metric("Total pendapatan", f"Rp {filtered['pendapatan'].sum():,.0f}")
    c3.metric("Unit terjual", f"{filtered['jumlah'].sum():,.0f}")
    c4.metric("Rata-rata transaksi", f"Rp {filtered['pendapatan'].mean():,.0f}" if len(filtered) else "Rp 0")

    if not filtered.empty:
        monthly = filtered.assign(bulan=filtered["tanggal"].dt.to_period("M").astype(str)).groupby("bulan", as_index=False)["pendapatan"].sum()
        st.plotly_chart(px.line(monthly, x="bulan", y="pendapatan", markers=True, title="Pendapatan per Bulan"), use_container_width=True)
        left, right = st.columns(2)
        by_product = filtered.groupby("produk", as_index=False)["pendapatan"].sum().sort_values("pendapatan", ascending=False)
        left.plotly_chart(px.bar(by_product, x="produk", y="pendapatan", title="Pendapatan per Produk"), use_container_width=True)
        by_city = filtered.groupby("kota", as_index=False)["pendapatan"].sum().sort_values("pendapatan", ascending=False)
        right.plotly_chart(px.bar(by_city, x="kota", y="pendapatan", title="Pendapatan per Kota"), use_container_width=True)
        st.dataframe(filtered.sort_values("tanggal", ascending=False), use_container_width=True)

with tab2:
    st.subheader("Data Preparation — Apakah data dapat dipercaya?")
    st.write(f"Jumlah baris awal: **{len(raw)}**")
    st.write(f"Jumlah baris setelah pembersihan: **{len(clean)}**")
    st.write(f"Baris yang dikeluarkan: **{len(raw) - len(clean)}**")
    quality = pd.DataFrame({
        "Pemeriksaan": ["ID transaksi duplikat", "Tanggal kosong/tidak valid", "Jumlah kosong/tidak valid", "Harga kosong/tidak valid"],
        "Keterangan": [
            int(raw["id_transaksi"].duplicated().sum()),
            int(pd.to_datetime(raw["tanggal"], errors="coerce", dayfirst=True, format="mixed").isna().sum()),
            int(pd.to_numeric(raw["jumlah"], errors="coerce").isna().sum() + (pd.to_numeric(raw["jumlah"], errors="coerce") <= 0).sum()),
            int(pd.to_numeric(raw["harga_satuan"], errors="coerce").isna().sum() + (pd.to_numeric(raw["harga_satuan"], errors="coerce") <= 0).sum())
        ]
    })
    st.dataframe(quality, hide_index=True, use_container_width=True)
    st.info("Catatan: pembersihan ini menghapus transaksi dengan tanggal/jumlah/harga yang tidak valid, menghapus ID duplikat, menyeragamkan teks, dan memberi label untuk kategori/kota kosong.")
    st.download_button("Unduh data bersih (CSV)", clean.to_csv(index=False).encode("utf-8"), "transaksi_penjualan_bersih.csv", "text/csv")

with tab3:
    st.subheader("Predictive Analytics — Perkiraan pendapatan bulan berikutnya")
    monthly = clean.assign(bulan=clean["tanggal"].dt.to_period("M")).groupby("bulan", as_index=False)["pendapatan"].sum()
    monthly = monthly.sort_values("bulan")
    if len(monthly) >= 2:
        x = np.arange(len(monthly)).reshape(-1, 1)
        y = monthly["pendapatan"].values
        model = LinearRegression().fit(x, y)
        pred = max(0, float(model.predict(np.array([[len(monthly)]]))[0]))
        next_month = (monthly["bulan"].max() + 1).strftime("%Y-%m")
        st.metric(f"Prediksi pendapatan {next_month}", f"Rp {pred:,.0f}")
        st.caption("Model demonstrasi menggunakan regresi linear sederhana dari agregat bulanan. Prediksi bukan jaminan; jumlah bulan yang sedikit dapat membuat hasil tidak stabil.")
        plot_df = monthly.copy()
        plot_df["bulan"] = plot_df["bulan"].astype(str)
        st.plotly_chart(px.bar(plot_df, x="bulan", y="pendapatan", title="Riwayat pendapatan bulanan"), use_container_width=True)
    else:
        st.warning("Data minimal dua bulan diperlukan untuk membuat contoh prediksi.")

with tab4:
    st.subheader("Prescriptive Analytics — Tindakan yang disarankan")
    if clean.empty:
        st.warning("Belum ada data valid untuk dianalisis.")
    else:
        product_rev = clean.groupby("produk")["pendapatan"].sum().sort_values(ascending=False)
        top_product = product_rev.index[0]
        low_product = product_rev.index[-1]
        city_rev = clean.groupby("kota")["pendapatan"].sum().sort_values(ascending=False)
        top_city = city_rev.index[0]
        st.markdown(f"- **Prioritaskan stok produk {top_product}**, karena menghasilkan pendapatan tertinggi pada data contoh.")
        st.markdown(f"- **Evaluasi produk {low_product}**: periksa harga, promosi, dan permintaan sebelum menambah stok.")
        st.markdown(f"- **Fokuskan evaluasi penjualan di {top_city}**, kota dengan pendapatan tertinggi pada data yang sudah dibersihkan.")
        st.markdown("- **Perbaiki pencatatan transaksi** dengan validasi tanggal, jumlah positif, harga, dan ID unik agar kualitas analisis berikutnya meningkat.")
        st.warning("Rekomendasi dibuat dari data contoh dan aturan sederhana. Manusia perlu memeriksa stok, margin keuntungan, musim, biaya, serta kondisi pasar sebelum mengambil keputusan.")

st.divider()
st.caption("Proyek pembelajaran — bukan sistem akuntansi atau peramalan produksi.")
