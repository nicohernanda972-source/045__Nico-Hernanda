========================================================================
DOKUMENTASI MINI PROJECT UTS - DASAR KOMPUTER DAN PEMROGRAMAN
Kelompok E (Embedded / IoT): Monitoring Kelembapan Tanah & Aksi Pompa
========================================================================

Identitas Mahasiswa:
- Nama     : Nico Hernanda
- NIm      : 03041282631045
- Kelas    : Indralaya A
- Kelompok : E

1. ANALISIS INPUT - PROCESS - OUTPUT (IPO)
- Input:
  List `data_kelembapan` berisi 20 data integer persentase kelembapan tanah (%), terdiri dari 15 data inti soal dan 5 data tambahan uji batas.
- Process:
  a. Melakukan perulangan (loop) untuk membaca setiap elemen data berdasarkan indeks (0 hingga 19).
  b. Mengklasifikasikan status kelembapan menggunakan percabangan:
     - Nilai < 35%          -> KERING
     - 35% <= Nilai <= 70%  -> NORMAL
     - Nilai > 70%          -> BASAH
  c. Menentukan aksi pompa berdasarkan status (POMPA ON jika KERING, POMPA OFF jika NORMAL/BASAH).
  d. Menghitung statistik keseluruhan: rata-rata, nilai maksimum, nilai minimum, serta jumlah masing-masing kategori.
- Output:
  a. Output per data: nomor urut (1-20), nilai kelembapan (%), status sensor, dan aksi pompa.
  b. Ringkasan akhir: total data (20), rata-rata kelembapan (%), nilai maksimum (%), nilai minimum (%), serta jumlah data KERING, NORMAL, dan BASAH.

2. PENJELASAN FUNCTION DALAM PROGRAM (`main.py`)
- `status_sensor(nilai)`: Menerima parameter `nilai` (int), mengevaluasi kondisi dengan struktur `if-elif-else`, dan mengembalikan (`return`) string kategori ("KERING", "NORMAL", atau "BASAH").
- `aksi_pompa(status)`: Menerima parameter `status` (str) dari hasil fungsi pertama, lalu mengembalikan (`return`) keputusan kontrol aktuator ("POMPA ON" atau "POMPA OFF").
- `hitung_statistik(data)`: Menerima parameter list `data` (20 elemen), melakukan iterasi menggunakan `for` untuk menjumlahkan nilai, mencari nilai maksimum & minimum, serta menghitung frekuensi tiap kategori, lalu mengembalikan 6 nilai statistik sekaligus.

3. ALUR KERJA PROGRAM & CARA MENJALANKAN
- Alur Program: Inisialisasi list 20 data -> Loop 1 mencetak status & aksi pompa tiap data (1-20) -> Pemanggilan `hitung_statistik()` untuk memproses seluruh data -> Mencetak ringkasan statistik akhir.
- Cara Menjalankan: Buka terminal/CMD pada direktori proyek, lalu jalankan perintah:
  python main.py

4. ALASAN PEMILIHAN 5 DATA TAMBAHAN (RENTANG 0-100%)
1. Nilai 0   : Menguji batas bawah absolut (0%) untuk memastikan kondisi ekstrem terkering terbaca sebagai "KERING" dan memicu "POMPA ON".
2. Nilai 35  : Menguji batas transisi awal (boundary value), tepat di titik saat status berubah dari "KERING" menjadi "NORMAL" dan "POMPA OFF".
3. Nilai 50  : Menguji variasi nilai tengah yang realistis pada kondisi kelembapan tanah yang ideal ("NORMAL").
4. Nilai 70  : Menguji batas transisi akhir (boundary value) untuk memastikan nilai tepat 70% masih masuk kategori "NORMAL" sebelum berubah menjadi "BASAH".
5. Nilai 100 : Menguji batas atas absolut (100%) untuk memastikan kondisi ekstrem terbasah terbaca sebagai "BASAH" dan "POMPA OFF".

5. CONTOH OUTPUT PROGRAM (HASIL EKSEKUSI TERMINAL)
--- Output Per Data ---
Data 1: Kelembapan = 22% -> KERING / POMPA ON
Data 2: Kelembapan = 28% -> KERING / POMPA ON
Data 3: Kelembapan = 34% -> KERING / POMPA ON
Data 4: Kelembapan = 41% -> NORMAL / POMPA OFF
Data 5: Kelembapan = 55% -> NORMAL / POMPA OFF
Data 6: Kelembapan = 63% -> NORMAL / POMPA OFF
Data 7: Kelembapan = 72% -> BASAH / POMPA OFF
Data 8: Kelembapan = 78% -> BASAH / POMPA OFF
Data 9: Kelembapan = 31% -> KERING / POMPA ON
Data 10: Kelembapan = 47% -> NORMAL / POMPA OFF
Data 11: Kelembapan = 66% -> NORMAL / POMPA OFF
Data 12: Kelembapan = 81% -> BASAH / POMPA OFF
Data 13: Kelembapan = 19% -> KERING / POMPA ON
Data 14: Kelembapan = 58% -> NORMAL / POMPA OFF
Data 15: Kelembapan = 69% -> NORMAL / POMPA OFF
Data 16: Kelembapan = 0% -> KERING / POMPA ON
Data 17: Kelembapan = 35% -> NORMAL / POMPA OFF
Data 18: Kelembapan = 50% -> NORMAL / POMPA OFF
Data 19: Kelembapan = 70% -> NORMAL / POMPA OFF
Data 20: Kelembapan = 100% -> BASAH / POMPA OFF

--- Ringkasan Akhir ---
Total data diproses  : 20 data
Rata-rata kelembapan : 48.95%
Kelembapan maksimum  : 100%
Kelembapan minimum   : 0%
Jumlah KERING        : 6
Jumlah NORMAL        : 10
Jumlah BASAH         : 4