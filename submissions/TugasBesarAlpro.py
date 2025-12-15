import csv

film_list = {
    "1": {"judul": "Avatar: The Way of Water", "harga": 60000, "jadwal": ["13:00", "15:00", "17:00"]},
    "2": {"judul": "The Counjuring: Last Riles", "harga": 55000, "jadwal": ["14:00", "16:00", "20:00"]},
    "3": {"judul": "Frozen II", "harga": 40000, "jadwal": ["10:00", "14:50", "19:30"]},
}

FILE_NAME = "pemesanan.csv"

def load_data():
    data = []
    try:
        with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["jumlah"] = int(row["jumlah"])
                row["total"] = int(row["total"])
                data.append(row)
    except FileNotFoundError:
        pass
    return data

def save_data(data):
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["nama", "film", "jadwal", "jumlah", "total"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

riwayat_pemesanan = load_data()

def tampilkan_film():
    print("\n=== DAFTAR FILM ===")
    for key, film in film_list.items():
        print(f"{key}. {film['judul']} - Rp{film['harga']} - Jadwal: {', '.join(film['jadwal'])}")

def create_pemesanan():
    tampilkan_film()
    pilihan = input("\nPilih nomor film yang ingin dipesan: ")
    if pilihan not in film_list:
        print("Nomor film tidak valid!")
        return

    film = film_list[pilihan]
    print(f"\nKamu memilih film: {film['judul']}")
    print(f"Jadwal tersedia: {', '.join(film['jadwal'])}")
    jadwal = input("Pilih jam tayang: ")

    if jadwal not in film["jadwal"]:
        print("Jam tayang tidak tersedia!")
        return

    try:
        jumlah = int(input("Masukkan jumlah tiket: "))
    except ValueError:
        print("Jumlah tiket harus berupa angka!")
        return

    total = film["harga"] * jumlah
    nama = input("Masukkan nama pemesan: ")

    pemesanan = {
        "nama": nama,
        "film": film["judul"],
        "jadwal": jadwal,
        "jumlah": jumlah,
        "total": total
    }

    riwayat_pemesanan.append(pemesanan)
    save_data(riwayat_pemesanan)
    print("\nPemesanan berhasil ditambahkan!")

def read_pemesanan():
    print("\n=== RIWAYAT PEMESANAN ===")
    if not riwayat_pemesanan:
        print("Belum ada pemesanan.")
    else:
        for i, data in enumerate(riwayat_pemesanan, start=1):
            print(f"{i}. {data['nama']} - {data['film']} ({data['jadwal']}) x{data['jumlah']} = Rp{data['total']}")

def update_pemesanan():
    read_pemesanan()
    if not riwayat_pemesanan:
        return

    try:
        index = int(input("\nMasukkan nomor pemesanan yang ingin diubah: ")) - 1
        if index < 0 or index >= len(riwayat_pemesanan):
            print("Nomor tidak valid!")
            return
    except ValueError:
        print("Input harus berupa angka!")
        return

    pesanan = riwayat_pemesanan[index]
    print(f"\nMengubah data untuk {pesanan['nama']} - {pesanan['film']} ({pesanan['jadwal']})")

    nama_baru = input("Nama baru (kosongkan jika tidak diubah): ")
    jumlah_baru = input("Jumlah tiket baru (kosongkan jika tidak diubah): ")

    if nama_baru:
        pesanan["nama"] = nama_baru
    if jumlah_baru:
        try:
            jumlah_baru = int(jumlah_baru)
            pesanan["jumlah"] = jumlah_baru
            
            for film in film_list.values():
                if film["judul"] == pesanan["film"]:
                    pesanan["total"] = film["harga"] * jumlah_baru
        except ValueError:
            print("Jumlah tiket harus angka!")

    save_data(riwayat_pemesanan)
    print("\nData berhasil diperbarui!")

def delete_pemesanan():
    read_pemesanan()
    if not riwayat_pemesanan:
        return

    try:
        index = int(input("\nMasukkan nomor pemesanan yang ingin dihapus: ")) - 1
        if index < 0 or index >= len(riwayat_pemesanan):
            print("Nomor tidak valid!")
            return
    except ValueError:
        print("Input harus berupa angka!")
        return

    konfirmasi = input(f"Yakin ingin menghapus {riwayat_pemesanan[index]['nama']}? (yes/no): ")
    if konfirmasi.lower() == "yes":
        riwayat_pemesanan.pop(index)
        save_data(riwayat_pemesanan)
        print("Pemesanan berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")


def searching():
    print("\n=== PENCARIAN DATA ===")
    print("1. Cari berdasarkan nama")
    print("2. Cari berdasarkan film")
    
    pilihan = input("Pilih: ")

    keyword = input("Masukkan kata yang dicari: ").lower()
    hasil = []

    if pilihan == "1":
        hasil = [p for p in riwayat_pemesanan if keyword in p["nama"].lower()]
    elif pilihan == "2":
        hasil = [p for p in riwayat_pemesanan if keyword in p["film"].lower()]
    else:
        print("Pilihan tidak valid!")
        return

    print("\n=== HASIL PENCARIAN ===")
    if hasil:
        for i, p in enumerate(hasil, start=1):
            print(f"{i}. {p['nama']} - {p['film']} ({p['jadwal']}) x{p['jumlah']} = Rp{p['total']}")
    else:
        print("Data tidak ditemukan.")


def sorting():
    print("\n=== SORTING DATA ===")
    print("1. Sortir berdasarkan nama")
    print("2. Sortir berdasarkan film")
    print("3. Sortir berdasarkan jam tayang")
    print("4. Sortir berdasarkan jumlah tiket")
    print("5. Sortir berdasarkan total harga")

    pilihan = input("Pilih: ")

    if pilihan == "1":
        sorted_data = sorted(riwayat_pemesanan, key=lambda x: x["nama"])
    elif pilihan == "2":
        sorted_data = sorted(riwayat_pemesanan, key=lambda x: x["film"])
    elif pilihan == "3":
        sorted_data = sorted(riwayat_pemesanan, key=lambda x: x["jadwal"])
    elif pilihan == "4":
        sorted_data = sorted(riwayat_pemesanan, key=lambda x: x["jumlah"])
    elif pilihan == "5":
        sorted_data = sorted(riwayat_pemesanan, key=lambda x: x["total"])
    else:
        print("Pilihan tidak valid!")
        return

    print("\n=== DATA SETELAH DI-SORT ===")
    for i, p in enumerate(sorted_data, start=1):
        print(f"{i}. {p['nama']} - {p['film']} ({p['jadwal']}) x{p['jumlah']} = Rp{p['total']}")


def menu():
    while True:
        print("\n=== PEMESANAN TIKET BIOSKOP ===")
        print("1. Tambah Pemesanan (Create)")
        print("2. Lihat Semua Pemesanan (Read)")
        print("3. Ubah Pemesanan (Update)")
        print("4. Hapus Pemesanan (Delete)")
        print("5. Searching")
        print("6. Sorting")
        print("7. Keluar")

        pilihan = input("\nPilih menu (1-7): ")

        if pilihan == "1":
            create_pemesanan()
        elif pilihan == "2":
            read_pemesanan()
        elif pilihan == "3":
            update_pemesanan()
        elif pilihan == "4":
            delete_pemesanan()
        elif pilihan == "5":
            searching()
        elif pilihan == "6":
            sorting()
        elif pilihan == "7":
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid!")

menu()