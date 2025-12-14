# SISTEM PENDATAAN MENU ES KRIM
menu_ice = [
    ["ES01", "Coklat", 15000, 100],
    ["ES02", "Vanila", 5000, 50],
    ["ES03", "Strobery", 10000, 30],
    ["ES04", "Oreo", 20000, 80],
]

def create():
    print("\n=== Tambahkan Menu Es Krim ===")
    try:
        id_menu = input("ID Menu: ")
        nama = input("Nama Varian: ")
        harga = int(input("Harga: "))
        stok = int(input("Stok: "))

        menu_ice.append([id_menu, nama, harga, stok])
        print("Menu berhasil ditambahkan!")
    
    except ValueError:
        print("Harga & stok harus berupa angka!") 


def read():
    print("\n=== Lihat Menu Es Krim ===")
    print("1. Tampilkan Semua Menu")
    print("2. Cari Menu")
    pilihan = input("Pilih (1/2): ").strip()
    
      
    if pilihan == "1":
        print("\n=== Semua Menu Es Krim ===")
        print("ID    Nama Varian               Harga      Stok")
        print("===============================================")
        for data in menu_ice:
            print(f"{data[0]:<6} {data[1]:<24} Rp{data[2]:<8} {data[3]}")
    #searcing
    elif pilihan == "2":
        print("\n=== Pencarian Menu ===")
        print("1. Berdasarkan ID")
        print("2. Berdasarkan Nama Varian")
        cari = input("Pilih (1/2): ")

        kata = input("Masukkan kata pencarian: ").strip().lower()
        ketemu = False

        for data in menu_ice:
            if (cari == "1" and kata.lower() in data[0].lower()) or\
               (cari == "2" and kata.lower() in data[1].lower()):
                print("Hasil:", data)
                ketemu = True

        if not ketemu:
            print("Data tidak ditemukan!")
    
    else:
        print("Pilihan tidak valid!")


def update():
    print("\n=== Edit Menu Es Krim ===")
    id_cari = input("Masukkan ID menu yang akan diedit: ").strip()

    for data in menu_ice:
        if data[0] == id_cari:
            try:
                data[0] = input("ID baru: ")
                data[1] = input("Nama varian baru: ")
                data[2] = int(input("Harga baru: "))
                data[3] = int(input("Stok baru: "))
                print("Data berhasil diperbarui!\n")
                return
            except ValueError:
                print("Harga dan stok harus berupa angka!")
                return

    print("Data tidak ditemukan!")


def delete():
    print("\n=== Hapus Menu Es Krim ===")
    id_cari = input("Masukkan ID menu yang akan dihapus: ").strip()

    for data in menu_ice:
        if data[0] == id_cari:
            menu_ice.remove(data)
            print("Data berhasil dihapus!")
            return 
    
    print("Data tidak ditemukan!")


def selection(data, index):
    n = len(data)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if data[j][index] < data[min_idx][index]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]


def sorting():
    print("\n=== Pilih Cara Mengurutkan ===")
    print("1. Berdasarkan Harga (Murah → Termahal)")
    print("2. Berdasarkan Stok (Sedikit → Banyak)")
    pilihan = input("Pilih: ")

    if pilihan == "1":
        selection(menu_ice, 2)
        print("Diurutkan berdasarkan harga!")
        read()

    elif pilihan == "2":
        selection(menu_ice, 3)
        print("Diurutkan berdasarkan stok!")
        read()

    else:
        print("Pilihan tidak valid!")


def menuUtama():
    while True:
        print("\n===================================")
        print("===     SISTEM MENU ES KRIM     ===")
        print("===          by Amix            ===")
        print("===================================")
        print("1. Tambah Menu")
        print("2. Lihat Menu")
        print("3. Urutkan Menu")
        print("4. Edit Menu")
        print("5. Hapus Menu")
        print("6. Keluar")
        try:
            pilihan = int(input("Masukkan pilihan [1 - 6]: "))
            if 1 <= pilihan <= 6:
                return pilihan
            print("Pilihan hanya antara 1 sampai 6!")
        except ValueError:
            print("Input harus berupa angka!")


##### PROGRAM UTAMA #####
pilihan = 0

while pilihan != 6:
    pilihan = menuUtama()
    if pilihan == 1:
        create()
    elif pilihan == 2:
        read()
        input("Tekan ENTER untuk lanjut...")
    elif pilihan == 3:
        sorting()
    elif pilihan == 4:
        update()
    elif pilihan == 5:
        delete()
print("🍦Terima kasih..!🍦")
