# 15 data
data_inti = [22, 28, 34, 41, 55, 63, 72, 78, 31, 47, 66, 81, 19, 58, 69]

# 5 data tambahan untuk menguji batas kategori (0-100%) dan variasi
data_tambahan = [0, 35, 50, 70, 100]

# data yang akan diproses
data_kelembapan = data_inti + data_tambahan

# Function 1: Menentukan status berdasarkan nilai kelembapan (Decision & Return)
def status_sensor(nilai):
    if nilai < 35:
        return "KERING"
    elif 35 <= nilai <= 70:
        return "NORMAL"
    else:
        return "BASAH"

# Function 2: aksi pompa berdasarkan status (Decision & Return)
def aksi_pompa(status):
    if status == "KERING":
        return "POMPA ON"
    else:
        return "POMPA OFF"

# Function 3: perhitungan statistik numerik dan ringkasan (Perhitungan, Loop, & Return)
def hitung_statistik(data):
    total = 0
    maks = data[0]
    mins = data[0]
    
    # Variabel untuk menghitung jumlah tiap kategori
    jml_kering = 0
    jml_normal = 0
    jml_basah = 0
    
    # Loop untuk memproses seluruh data
    for nilai in data:
        total += nilai
        
        # nilai maksimum dan minimum
        if nilai > maks:
            maks = nilai
        if nilai < mins:
            mins = nilai
            
        # distribusi kategori
        kategori = status_sensor(nilai)
        if kategori == "KERING":
            jml_kering += 1
        elif kategori == "NORMAL":
            jml_normal += 1
        elif kategori == "BASAH":
            jml_basah += 1
            
    rata_rata = total / len(data)
    
    return rata_rata, maks, mins, jml_kering, jml_normal, jml_basah

# ==========================================
# BAGIAN UTAMA PROGRAM (OUTPUT)
# ==========================================

print("--- Output Per Data ---")
# Menampilkan output per data beserta nomor urutnya
for i in range(len(data_kelembapan)):
    nilai_saat_ini = data_kelembapan[i]
    status_saat_ini = status_sensor(nilai_saat_ini)
    pompa_saat_ini = aksi_pompa(status_saat_ini)
    
    print(f"Data {i+1}: Kelembapan = {nilai_saat_ini}% -> {status_saat_ini} / {pompa_saat_ini}")

# Memanggil function perhitungan
rata_rata, maks, mins, total_kering, total_normal, total_basah = hitung_statistik(data_kelembapan)

print("\n--- Ringkasan Akhir ---")
print(f"Total data diproses  : {len(data_kelembapan)} data")
print(f"Rata-rata kelembapan : {rata_rata:.2f}%")
print(f"Kelembapan maksimum  : {maks}%")
print(f"Kelembapan minimum   : {mins}%")
print(f"Jumlah KERING        : {total_kering}")
print(f"Jumlah NORMAL        : {total_normal}")
print(f"Jumlah BASAH         : {total_basah}")