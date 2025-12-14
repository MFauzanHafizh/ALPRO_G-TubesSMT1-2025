makanan = [] 

def tambah():
    if not makanan:
        new_id = 1
    else:
        new_id = makanan[-1][0] + 1
        
    nama = input("Nama: ")
    harga = int(input("Harga: "))
    stock = int(input("Stock: "))
    
    makanan.append([new_id, nama, harga, stock])
    print("Makanan berhasil ditambahkan.") 
    

def tampilkan_makanan_ringan():
    print("\nDaftar Makanan:")
    if not makanan: 
        print("Daftar makanan ringan.")
        return
        
    for item in makanan:
        print(f"ID: {item[0]}, Nama: {item[1]}, Harga: {item[2]}, Stock: {item[3]}")

def ubah():
    tampilkan_makanan_ringan()
    if not makanan:
        return
        
    try:
        id_ubah = int(input("Masukkan ID makanan yang ingin diubah: "))
    except ValueError:
        print("Input ID harus berupa angka.")
        return
        
    ditemukan = False
    for item in makanan:
        if item[0] == id_ubah:
            item[1] = input("Nama baru: ")
            item[2] = int(input("Harga baru: "))
            item[3] = int(input("Stock baru: "))
            print("Data berhasil diubah.")
            ditemukan = True
            return
    
    if not ditemukan:
        print("ID tidak ditemukan.")

def hapus():
    tampilkan_makanan_ringan()
    if not makanan:
        return

    try:
        id_hapus = int(input("Masukkan ID makanan yang ingin dihapus: "))
    except ValueError:
        print("Input ID harus berupa angka.")
        return

    for item in makanan:
        if item[0] == id_hapus:
            makanan.remove(item)
            print("Data berhasil dihapus.")
            return
    print("ID tidak ditemukan.")
    
def urutkan():
    if not makanan:
        print("Tidak ada data untuk diurutkan.")
        return
    
    print("Urutkan berdasarkan:")
    print("1. Nama  2. Harga  3. Stock")
    
    try:
        pilih = int(input("Pilih (1-3): "))
        
        if pilih not in [1, 2, 3]:
            print("Pilihan tidak valid.")
            return
        
        for i in range(len(makanan)):
            for j in range(i + 1, len(makanan)):
                if makanan[i][pilih] > makanan[j][pilih]:
                    makanan[i], makanan[j] = makanan[j], makanan[i]
        
        label = ["", "Nama", "Harga", "Stock"][pilih]
        print(f"Data berhasil diurutkan berdasarkan {label}.")
        
    except ValueError:
        print("Pilihan tidak valid.")

def cari():
    if not makanan:
        print("Daftar makanan kosong. Tidak dapat melakukan pencarian.")
        return
    
    nama_cari = input("Masukkan nama makanan yang dicari: ")
    hasil = [item for item in makanan if item[1] == nama_cari]
    
    if hasil:
        for item in hasil:
            print(f"Ditemukan: ID: {item[0]}, Nama: {item[1]}, Harga: {item[2]}, Stock: {item[3]}")
    else:
        print("Makanan tidak ditemukan.")
    

while True:
    print("\n--- Menu  Makanan ---")
    print("1. Tambah Makanan")
    print("2. Tampilkan Makanan")
    print("3. Ubah Makanan")
    print("4. Hapus Makanan")
    print("5. Cari berdasarkan urutan")
    print("6. Cari otomatis")
    print("7. Keluar dari program")
    print("-----------------------------------")
    
    pilihan = input("Pilih menu (1-7): ")
    
    if pilihan == '1':
        try:
            tambah()
        except ValueError:
            print("Input Harga dan Stock harus berupa angka!")
    elif pilihan == '2':
        tampilkan_makanan_ringan()
    elif pilihan == '3':
        try:
            ubah()
        except ValueError:
            print("Input Harga/Stock baru harus berupa angka!")
    elif pilihan == '4':
        hapus()
    elif pilihan == '5':
        urutkan()
    elif pilihan == '6':
        cari()
    elif pilihan == '7':
        print("Keluar dari program.cle")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")