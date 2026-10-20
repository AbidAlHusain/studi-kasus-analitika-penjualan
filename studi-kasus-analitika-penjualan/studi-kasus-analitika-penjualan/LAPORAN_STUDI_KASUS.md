# Studi Kasus: Penerapan Analitika Data untuk Mendukung Keputusan Penjualan Toko Ritel

## A. Latar Belakang
Dalam kegiatan bisnis, data transaksi penjualan sering memiliki masalah seperti data kosong, format tanggal yang tidak konsisten, penulisan nama produk yang berbeda, duplikasi transaksi, serta jumlah atau harga yang tidak valid. Jika data tersebut langsung digunakan, hasil laporan dapat menyesatkan dan berisiko menyebabkan keputusan stok yang kurang tepat. Oleh karena itu, dibutuhkan sistem sederhana yang mampu membersihkan, menganalisis, dan menyajikan data agar dapat digunakan sebagai dasar pengambilan keputusan.

## B. Rumusan Masalah
Bagaimana mengubah data transaksi penjualan yang belum terstruktur dengan baik menjadi informasi, insight, prediksi sederhana, dan rekomendasi yang membantu pengelola toko menentukan prioritas produk serta perbaikan pencatatan?

## C. Tujuan
Membangun dashboard analitika penjualan menggunakan Python, Pandas, Streamlit, Plotly, dan Scikit-learn. Sistem melakukan pembersihan data, menampilkan indikator penjualan, membandingkan performa produk dan kota, memperkirakan pendapatan bulan berikutnya, serta menghasilkan rekomendasi awal.

## D. Metode
Proyek mengadaptasi alur CRISP-DM. Pada tahap pemahaman bisnis, masalah yang diangkat adalah sulitnya mengambil keputusan jika data transaksi tidak rapi. Pada tahap pemahaman data, sistem membaca data transaksi yang berisi tanggal, produk, kategori, jumlah, harga satuan, dan kota. Pada tahap persiapan data, format tanggal dan angka dinormalisasi, teks dirapikan, ID duplikat dihapus, dan transaksi tidak valid dikeluarkan. Tahap pemodelan menggunakan agregasi untuk analisis penjualan dan regresi linear sederhana untuk contoh prediksi. Hasil ditampilkan melalui dashboard untuk dievaluasi pengguna sebelum diterapkan sebagai dasar tindakan.

## E. Implementasi Sistem
Sistem memiliki empat bagian. Bagian Ringkasan menampilkan jumlah transaksi valid, total pendapatan, unit terjual, rata-rata nilai transaksi, dan grafik penjualan per bulan, produk, serta kota. Bagian Kualitas Data memperlihatkan perubahan jumlah baris dan beberapa indikator masalah data, serta menyediakan unduhan CSV bersih. Bagian Prediksi menggunakan regresi linear pada pendapatan bulanan untuk memperkirakan nilai bulan selanjutnya. Bagian Rekomendasi mengidentifikasi produk dan kota berdasarkan pendapatan, lalu menyusun saran awal untuk pengelolaan stok dan evaluasi penjualan.

## F. Hubungan dengan Hierarki Data–Informasi–Insight–Decision
Data mentah berupa catatan transaksi merupakan bahan awal. Setelah dibersihkan dan dikelompokkan, data menghasilkan informasi berupa total pendapatan dan jumlah unit terjual. Perbandingan antarproduk dan kota menghasilkan insight awal mengenai bagian yang berkontribusi besar atau kecil terhadap pendapatan. Insight tersebut kemudian diterjemahkan menjadi keputusan yang dapat dipertimbangkan, misalnya meninjau persediaan produk dengan pendapatan tinggi, mengevaluasi produk berpendapatan rendah, dan memperbaiki validasi saat pencatatan transaksi.

## G. Hasil yang Diharapkan
Dashboard diharapkan membantu pengguna memahami kondisi penjualan dengan lebih cepat, mengurangi risiko akibat data ganda atau tidak valid, dan membuat proses analisis lebih transparan. Karena dataset bersifat sintetis, hasil angka yang muncul hanya untuk demonstrasi dan tidak mewakili kondisi toko nyata.

## H. Keterbatasan dan Pengawasan Manusia
Prediksi menggunakan regresi linear sederhana dan data bulanan terbatas, sehingga hasilnya tidak boleh dianggap sebagai kepastian. Pendapatan juga belum memperhitungkan modal, biaya operasional, diskon, retur, atau margin laba. Rekomendasi otomatis perlu diperiksa bersama informasi stok, tren musiman, pemasok, dan kondisi pasar. Sistem mendukung keputusan, bukan menggantikan tanggung jawab pengambil keputusan.

## I. Kesimpulan
Studi kasus ini menunjukkan penerapan konsep analitika data secara praktis melalui alur dari data mentah hingga rekomendasi keputusan. Persiapan data menjadi tahap penting karena kualitas hasil analisis sangat bergantung pada kualitas data masukan. Kombinasi analisis deskriptif, diagnostik sederhana, prediksi, dan rekomendasi dapat membantu organisasi menyusun keputusan yang lebih berbasis data, dengan verifikasi manusia sebagai bagian yang tidak terpisahkan.
