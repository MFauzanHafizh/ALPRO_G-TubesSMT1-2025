#===========================
def create(data):
    print("== Tambah Data Barang ==")

    nama = input("Nama barang: ")
    if not nama:
        print("Nama tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return data

    kondisi = input("Kondisi: ")
    cara = input("Cara didapatkan: ")

    try:
        harga = float(input("Perkiraan harga: "))
    except ValueError:
        print("Harga harus angka!")
        input("Tekan Enter untuk kembali...")
        return data

    kisah = input("Kisah/History: ")

    id_baru = len(data) + 1
    data.append([id_baru, nama, kondisi, cara, harga, kisah])

    print(f"Barang '{nama}' ditambahkan dengan ID {id_baru}")
    input("Tekan Enter untuk kembali...")
    return data

#===========================

def read(data):
    print("== Daftar Barang ==")
    print("ID | Nama | Kondisi | Cara Didapat | Harga | Kisah/History")
    print("=" * 75)
    for r in data:
        print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]}")

    input("Tekan Enter untuk kembali...")

#===========================

def update(data):
    print("== Update Data ==")

    if not data:
        print("Belum ada data.")
        input("Tekan Enter untuk kembali...")
        return data

    print("ID | Nama | Kondisi | Cara Didapat | Harga | Kisah/History")
    print("=" * 75)
    for r in data:
        print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]}")
    print()

    try:
        id_update = int(input("Masukkan ID yang ingin diupdate: "))
    except ValueError:
        print("ID harus angka!")
        input("Tekan Enter untuk kembali...")
        return data

    item = None
    for u in data:
        if u[0] == id_update:
            item = u
            break

    if item is None:
        print("ID tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return data

    print("Data sekarang:")
    print(f"1. Nama      : {item[1]}")
    print(f"2. Kondisi   : {item[2]}")
    print(f"3. Cara      : {item[3]}")
    print(f"4. Harga     : {item[4]}")
    print(f"5. Kisah     : {item[5]}")

    try:
        pilih = int(input("Pilih bagian (1-5): "))
    except ValueError:
        print("Input salah!")
        input("Tekan Enter untuk kembali...")
        return data

    if pilih == 1:
        item[1] = input("Nama baru: ") or item[1]
    elif pilih == 2:
        item[2] = input("Kondisi baru: ") or item[2]
    elif pilih == 3:
        item[3] = input("Cara baru: ") or item[3]
    elif pilih == 4:
        try:
            item[4] = float(input("Harga baru: "))
        except ValueError:
            print("Harga harus angka!")
    elif pilih == 5:
        item[5] = input("Kisah baru: ") or item[5]
    else:
        print("Pilihan salah!")

    print("Data berhasil diperbarui.")
    input("Tekan Enter untuk kembali...")
    return data


#===========================

def delete(data):
    print("== Hapus Data ==")

    if not data:
        print("Belum ada data.")
        input("Tekan Enter untuk kembali...")
        return data

    print("ID | Nama | Kondisi | Cara Didapat | Harga | Kisah/History")
    print("=" * 75)
    for r in data:
        print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]}")
    print()

    try:
        id_hapus = int(input("Masukkan ID yang ingin dihapus: "))
    except ValueError:
        print("ID harus angka!")
        input("Tekan Enter untuk kembali...")
        return data

    ditemukan = False
    for item in data:
        if item[0] == id_hapus:
            data.remove(item)
            ditemukan = True
            break

    if not ditemukan:
        print("ID tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return data

    for i in range(len(data)):
        data[i][0] = i + 1

    print("Data berhasil dihapus.")
    input("Tekan Enter untuk kembali...")
    return data

#===========================

def search(data):
    print("== Cari Data Berdasarkan ID (Binary Search) ==")
    for r in data:
        print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]}")
    if not data:
        print("Belum ada data.")
        input("Tekan Enter untuk kembali...")
        return data

    try:
        dicari = int(input("Masukkan ID yang dicari: "))
    except ValueError:
        print("ID harus angka!")
        input("Tekan Enter untuk kembali...")
        return

    low = 0
    high = len(data) - 1
    ditemukan = False
    mid = 0  

    while low <= high and not ditemukan:
        mid = (low + high) // 2

        print(f"Low: {low}, Mid: {mid}, High: {high}")

        if data[mid][0] == dicari:
            ditemukan = True
            print(f"Nilai {dicari} ditemukan di indeks ke-{mid}")
        elif data[mid][0] < dicari:
            low = mid + 1
        else:
            high = mid - 1

    if not ditemukan:
        print(f"Nilai {dicari} tidak ditemukan di list.")
        input("Tekan Enter untuk kembali...")
        return

    hasil = data[mid]
    print("Data ditemukan:")
    print(f"ID      : {hasil[0]}")
    print(f"Nama    : {hasil[1]}")
    print(f"Kondisi : {hasil[2]}")
    print(f"Cara    : {hasil[3]}")
    print(f"Harga   : {hasil[4]}")
    print(f"Kisah   : {hasil[5]}")

    input("Tekan Enter untuk kembali...")

#===========================

def sorting(data):
    print("== Sorting Harga Barang ==")

    if not data:
        print("Belum ada data.")
        input("Tekan Enter untuk kembali...")
        return

    print("1. Termurah ke Termahal (Ascending)")
    print("2. Termahal ke Termurah (Descending)")

    pilih = input("Pilih jenis sorting: ")
    salin_data = data.copy()

    if pilih == "1":
        for i in range(len(salin_data)):
            for j in range(len(salin_data) - i - 1):
                if salin_data[j][4] > salin_data[j + 1][4]:
                    temp = salin_data[j]
                    salin_data[j] = salin_data[j + 1]
                    salin_data[j + 1] = temp

    elif pilih == "2":
        for i in range(len(salin_data)):
            for j in range(len(salin_data) - i - 1):
                if salin_data[j][4] < salin_data[j + 1][4]:
                    temp = salin_data[j]
                    salin_data[j] = salin_data[j + 1]
                    salin_data[j + 1] = temp

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
        return

    print("=== Hasil Sorting ===")
    print("ID | Nama | Kondisi | Cara Didapat | Harga | Kisah/History")
    print("=" * 75)
    for r in salin_data:
        print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]}")

    input("Tekan Enter untuk kembali...")


#===========================

def menuutama(): #contoh fungsi menuUtama
    print("=====================================")
    print("===   Sistem Data Barang Museum   ===")
    print("===     by Ahmad Nur Farizi       ===")
    print("=====================================")
    print("1. Tambah Data")
    print("2. Liat Data")
    print("3. Edit Data")
    print("4. Hapus Data")
    print("5. Search Id For history")
    print("6. Sorting By Harga")
    print("7. Keluar")

    try:
        pilihan = int(input("Masukkan pilihan [1 - 7]: "))
        if 1 <= pilihan <= 7:
            return pilihan
        else:
            print("Pilihan hanya 1-7!")
            input()
    except ValueError:
        print("Input harus angka!")
        input()


##### PROGRAM UTAMA #####
pilihan = 0
data = [
    [1, "Vas Kuno", "Baik", "Donasi", 250000, "Ditemukan di rumah tua tahun 1950"],
    [2, "Pedang Kerajaan", "Sedang", "Peninggalan", 1500000, "Dari era kerajaan kuno abad ke-18"],
    [3, "Koin Perunggu", "Kurang Baik", "Pembelian", 50000, "Koin langka dari masa kolonial"]
]

while pilihan != 7:
    pilihan = menuutama()

    if pilihan == 1:
        data = create(data)
    elif pilihan == 2:
        read(data)
    elif pilihan == 3:
        update(data)
    elif pilihan == 4:
        delete(data)
    elif pilihan == 5:
        search(data)
    elif pilihan == 6:
        sorting(data)
    elif pilihan == 7:
        print("Program selesai.")