# ==========================================
# UTS Dasar Komputer dan Pemrograman
# Kasus: Kelompok E  
# Deskripsi: Monitoring Kelembapan Tanah & Aksi Pompa
# Nama: Nico hernanda
# NIM : 03041282631045
# ==========================================

# 1. Fungsi menentukan status tanah berdasarkan nilai kelembapan (Decision & Return)
def status_sensor(nilai):
    if nilai < 35:
        return "KERING"
    elif 35 <= nilai <= 70:
        return "NORMAL"
    else:
        return "BASAH"

# 2. Fungsi menentukan aksi pompa berdasarkan status tanah (Decision & Return)
def aksi_pompa(status):
    if status == "KERING":
        return "POMPA ON"
    else:
        return "POMPA OFF"

# 3. Fungsi menghitung rata-rata (Perhitungan, Loop, & Return)
def rata_rata(data_list):
    total = 0
    for nilai in data_list:
        total += nilai
    return total / len(data_list)

# ==========================================
# DATA & INISIALISASI
# ==========================================

# 15 data inti dari soal
data_inti = [22, 28, 34, 41, 55, 63, 72, 78, 31, 47, 66, 81, 19, 58, 69]

# 5 data tambahan (realistis 0-100%) untuk menguji batas
data_tambahan = [35, 70, 71, 0, 100] 

# Menggabungkan menjadi tepat 20 data dalam satu List
data_kelembapan = data_inti + data_tambahan

# Variabel untuk menyimpan perhitungan ringkasan
jumlah_kering = 0
jumlah_normal = 0
jumlah_basah = 0

# Set nilai awal max dan min menggunakan data pertama
nilai_maks = data_kelembapan[0]
nilai_min = data_kelembapan[0]

# ==========================================
# PROSES UTAMA (LOOP) & OUTPUT PER DATA
# ==========================================

print("="*60)
print("HASIL MONITORING KELEMBAPAN TANAH")
print("="*60)
print(f"{'No':<4} | {'Kelembapan (%)':<15} | {'Status Tanah':<12} | {'Aksi Pompa':<10}")
print("-" * 60)

for i in range(len(data_kelembapan)):
    nilai = data_kelembapan[i]
    
    # Memanggil fungsi
    status = status_sensor(nilai)
    pompa = aksi_pompa(status)
    
    # Menghitung jumlah per kategori
    if status == "KERING":
        jumlah_kering += 1
    elif status == "NORMAL":
        jumlah_normal += 1
    else:
        jumlah_basah += 1
        
    # Mencari nilai maksimum dan minimum
    if nilai > nilai_maks:
        nilai_maks = nilai
    if nilai < nilai_min:
        nilai_min = nilai
        
    # Menampilkan output per data (format rapi)
    print(f"{i+1:<4} | {nilai:<15} | {status:<12} | {pompa:<10}")

# ==========================================
# RINGKASAN AKHIR
# ==========================================

# Memanggil fungsi hitung rata-rata
nilai_rata2 = rata_rata(data_kelembapan)

print("="*60)
print("\nRINGKASAN AKHIR")
print("="*30)
print(f"Total Data Diproses : {len(data_kelembapan)}")
print(f"Kategori KERING     : {jumlah_kering} data")
print(f"Kategori NORMAL     : {jumlah_normal} data")
print(f"Kategori BASAH      : {jumlah_basah} data")
print("-" * 30)
print(f"Nilai Rata-rata     : {nilai_rata2:.2f} %")
print(f"Nilai Maksimum      : {nilai_maks} %")
print(f"Nilai Minimum       : {nilai_min} %")
print("="*30)