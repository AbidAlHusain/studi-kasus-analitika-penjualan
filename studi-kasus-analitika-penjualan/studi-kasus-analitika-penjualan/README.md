# Studi Kasus Analitika Data: Dashboard Penjualan Toko

## 1. Latar belakang
Toko ritel memiliki data transaksi operasional yang tidak selalu rapi. Data dapat berisi format tanggal berbeda, spasi pada nama produk/kota, nilai kosong, ID transaksi ganda, dan transaksi tidak valid. Jika data langsung dianalisis, laporan penjualan dan keputusan stok dapat keliru.

## 2. Tujuan
Membangun dashboard sederhana untuk:
- membersihkan data transaksi;
- merangkum pendapatan dan jumlah unit terjual;
- membandingkan penjualan berdasarkan produk, bulan, dan kota;
- membuat contoh prediksi pendapatan bulanan;
- menyusun rekomendasi awal yang tetap perlu diverifikasi manusia.

## 3. Pemetaan materi pemateri
| Konsep | Implementasi dalam proyek |
|---|---|
| Data | `data/transaksi_penjualan_kotor.csv` sebagai data mentah |
| Informasi | KPI, tabel transaksi bersih, grafik pendapatan |
| Insight | Produk/kota dengan pendapatan tertinggi dan terendah |
| Decision | Rekomendasi stok, evaluasi produk, dan perbaikan pencatatan |
| CRISP-DM | Memahami masalah, memahami data, menyiapkan data, membuat model sederhana, mengevaluasi, dan menampilkan hasil |
| Descriptive | Ringkasan transaksi, pendapatan, unit terjual |
| Diagnostic | Perbandingan pendapatan berdasarkan produk dan kota |
| Predictive | Regresi linear sederhana untuk perkiraan bulan berikutnya |
| Prescriptive | Saran tindakan berbasis hasil agregasi |
| Generative AI / human oversight | AI dapat membantu menulis dan mengevaluasi workflow, tetapi hasil harus dicek manusia |

## 4. Struktur repositori
```text
studi-kasus-analitika-penjualan/
├── app.py
├── requirements.txt
├── README.md
└── data/
    └── transaksi_penjualan_kotor.csv
```

## 5. Cara menjalankan di komputer
Disarankan menggunakan Python 3.10 atau lebih baru.

1. Ekstrak ZIP atau clone repositori.
2. Buka terminal di folder proyek.
3. Buat virtual environment (opsional tetapi disarankan):
   ```bash
   python -m venv .venv
   ```
4. Aktifkan environment:
   - Windows CMD: `.venv\Scripts\activate`
   - PowerShell: `.venv\Scripts\Activate.ps1`
5. Pasang dependensi:
   ```bash
   pip install -r requirements.txt
   ```
6. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```
7. Buka alamat lokal yang ditampilkan terminal, biasanya `http://localhost:8501`.

## 6. Ringkasan proses pembersihan
1. Mengubah kolom tanggal menjadi format tanggal; format yang tidak terbaca menjadi nilai kosong.
2. Menyeragamkan teks nama produk, kategori, dan kota.
3. Menghapus ID transaksi duplikat.
4. Mengubah jumlah dan harga menjadi angka.
5. Mengeluarkan transaksi yang tanggal, jumlah, atau harganya tidak valid; jumlah dan harga harus positif.
6. Mengisi kategori/kota yang kosong dengan label `Tidak diketahui`.
7. Menghitung pendapatan = jumlah × harga satuan.

Prinsipnya adalah *Garbage In, Garbage Out*: data yang buruk dapat menghasilkan kesimpulan yang buruk. Aturan pembersihan harus didokumentasikan dan disesuaikan dengan aturan bisnis sebenarnya.

## 7. Catatan metodologi dan keterbatasan
- Dataset yang disediakan adalah data sintetis untuk pembelajaran, bukan data bisnis nyata.
- Pendapatan tidak sama dengan laba karena biaya dan margin belum tersedia.
- Regresi linear memakai agregat bulanan dan data yang terbatas; prediksi hanya demonstrasi, bukan dasar keputusan otomatis.
- Analisis diagnostik pada proyek ini berupa perbandingan sederhana, bukan bukti sebab-akibat.
- Sebelum digunakan di dunia nyata, validasi aturan bisnis, cek pencilan, audit data, dan lakukan evaluasi model yang lebih kuat.
- Jangan mengunggah data pribadi atau data perusahaan rahasia ke repositori publik.

## 8. Ide pengembangan
- Tambahkan unggah CSV dari pengguna.
- Tambahkan filter rentang tanggal.
- Gunakan data biaya untuk menghitung laba dan margin.
- Bandingkan beberapa model prediksi dan evaluasi dengan MAE/RMSE.
- Tambahkan pengujian otomatis untuk fungsi `clean_data`.
- Simpan hasil ke database jika aplikasi berkembang.

## 9. Lisensi
Materi pembelajaran untuk tugas kuliah. Silakan modifikasi dan cantumkan sumber jika mengadaptasi kode dari pihak lain.
