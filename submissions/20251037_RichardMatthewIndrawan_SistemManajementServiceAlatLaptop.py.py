import os

NAMA_FILE = "data_service.txt"

def simpan_ke_file(data):
   
    file = open(NAMA_FILE, "w")
    for item in data:
        baris = item[0] + "," + item[1] + "," + item[2] + "," + item[3] + "," + item[4] + "," + str(item[5]) + "," + str(item[6]) + "," + str(item[7])
        file.write(baris + "\n")
    file.close()

def baca_dari_file():
    data_kosong = []
    if os.path.exists(NAMA_FILE):
        file = open(NAMA_FILE, "r")
        for baris in file:
            pecahan = baris.strip().split(",")
            if len(pecahan) == 8:
                pecahan[5] = int(pecahan[5]) 
                pecahan[6] = int(pecahan[6])
                pecahan[7] = int(pecahan[7])
                data_kosong.append(pecahan)
        file.close()
    return data_kosong

def tambah_data(data):
    print("\n--- Tambah Data Baru ---")
    try:
        nama = input("Nama Pelanggan       : ")
        jenis = input("Jenis Barang         : ")
        status_byr = input("Status Bayar         : ")
        status_brg = input("Status Barang        : ")
        estimasi = input("Estimasi (YYYY-MM-DD): ")
        unit = int(input("Jumlah Unit          : "))
        harga = int(input("Harga per Unit       : "))
        total = unit * harga
        data_baru = [nama, jenis, status_byr, status_brg, estimasi, unit, harga, total]
        data.append(data_baru)
        
        simpan_ke_file(data)
        print("Data berhasil disimpan!")
    except ValueError:
        print("Error: Unit dan Harga harus angka!")
    return data

def lihat_data(data):
    if len(data) == 0:
        print("Belum ada data.")
    else:
        print("\n--- Daftar Pesanan Lengkap ---")
        print("No | Nama | Jenis | Byr | Stat | Est | Unit | Hrg | Total")
        print("-" * 80) 
        
        nomor = 1
        for item in data:
            print(f"{nomor} | {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]} | {item[5]} | {item[6]} | {item[7]}")
            nomor = nomor + 1

def ubah_data(data):
    lihat_data(data)
    if len(data) == 0:
        return data

    try:
        nomor = int(input("\nMasukkan Nomor yang mau diubah: "))
        index = nomor - 1
        
        if index >= 0 and index < len(data):
            print("Ketik data baru (atau tekan ENTER jika tidak mau diubah)")
            
            data_lama = data[index]
            
            nama_baru = input(f"Nama ({data_lama[0]}): ")
            if nama_baru == "":
                nama_baru = data_lama[0] 
            
            jenis_baru = input(f"Jenis ({data_lama[1]}): ")
            if jenis_baru == "":
                jenis_baru = data_lama[1]

            estimasi_baru = input(f"Estimasi ({data_lama[4]}): ")
            if estimasi_baru == "":
                estimasi_baru = data_lama[4]
                
            data[index][0] = nama_baru
            data[index][1] = jenis_baru
            data[index][4] = estimasi_baru
            
            simpan_ke_file(data)
            print("Data berhasil diubah!")
        else:
            print("Nomor salah.")
    except ValueError:
        print("Input harus angka.")
    return data

def hapus_data(data):
    lihat_data(data)
    if len(data) == 0:
        return data
        
    try:
        nomor = int(input("\nMasukkan Nomor yang mau dihapus: "))
        index = nomor - 1
        
        if index >= 0 and index < len(data):
            del data[index] 
            simpan_ke_file(data) 
            print("Data berhasil dihapus.")
        else:
            print("Nomor tidak ditemukan.")
    except ValueError:
        print("Input harus angka.")
    return data

def cari_data(data):
    print("\n--- Cari Data Spesifik ---")
    cari_nama = input("Masukkan Nama yang dicari : ")
    cari_jenis = input("Masukkan Jenis yang dicari: ")
    
    ditemukan = False
    print(f"\n--- Hasil Pencarian '{cari_nama}' & '{cari_jenis}' ---")
    
    for item in data:
        nama_di_data = item[0].lower()
        jenis_di_data = item[1].lower()
        
        if (cari_nama.lower() in nama_di_data) and (cari_jenis.lower() in jenis_di_data):
            print(f"Ditemukan: {item[0]} | {item[1]} | Status: {item[3]} | Total: Rp{item[7]}")
            ditemukan = True
            
    if ditemukan == False:
        print("Data tidak ditemukan.")

def urutkan_estimasi(data):
    jumlah = len(data)
    
    for i in range(jumlah):
        for j in range(0, jumlah - i - 1):
            if data[j][4] > data[j+1][4]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
                
    simpan_ke_file(data)
    print("Data berhasil diurutkan berdasarkan tanggal estimasi.")
    lihat_data(data)
    return data

data_pesanan = baca_dari_file()
pilihan = 0

while pilihan != 7:
    print("===================================")
    print("=== Aplikasi Service Elektronik ===")
    print("===      by SGP Elektronik      ===")
    print("===================================")
    print("1. Tambah Pesanan")
    print("2. Lihat Pesanan")
    print("3. Edit Pesanan")
    print("4. Hapus Pesanan")
    print("5. Urutkan berdasarkan estimasi selesai")
    print("6. Cari berdasarkan nama dan jenis")
    print("7. Keluar")
    
    try:
        pilihan = int(input("Pilih menu: "))
        
        if pilihan == 1:
            data_pesanan = tambah_data(data_pesanan)
        elif pilihan == 2:
            lihat_data(data_pesanan)
        elif pilihan == 3:
            data_pesanan = ubah_data(data_pesanan)
        elif pilihan == 4:
            data_pesanan = hapus_data(data_pesanan)
        elif pilihan == 5:
            data_pesanan = urutkan_estimasi(data_pesanan)
        elif pilihan == 6:
            cari_data(data_pesanan)
        elif pilihan == 7:
            print("Keluar program.")
    except ValueError:
        print("Masukkan angka saja.")