dataBuku = []

# ------------------------------
# 1. TAMBAH DATA
# ------------------------------
def tambah():
    global dataBuku
    print("\n--- Tambah Data Buku ---")

    judul = input("Judul Buku: ")
    jenis = input("Jenis Buku (misal: Komik/Novel): ")
    # --- Tambahan untuk Volume Buku ---
    while True:
        volume_str = input("Volume Buku (kosongkan jika tidak ada, atau masukkan angka): ")
        if volume_str == "":
            volume = None # Gunakan None jika tidak ada volume
            break
        try:
            volume = int(volume_str) # Konversi ke integer
            break
        except ValueError:
            print("Volume harus berupa angka atau dikosongkan. Silakan coba lagi.")
    # ------------------------------------

    # Menambahkan data ke list [Judul, Jenis, Volume]
    dataBuku.append([judul, jenis, volume])
    print("Buku berhasil ditambahkan.\n")


# ------------------------------
# Fungsi Pembantu untuk Format Output Buku
# ------------------------------
def format_buku(buku):
    """Mengembalikan string terformat dari data buku, termasuk volume."""
    judul = buku[0]
    jenis = buku[1]
    volume = buku[2] # Volume ada di index 2

    if volume is not None:
        return f"Judul: {judul} | Jenis: {jenis} | Volume: {volume}"
    else:
        return f"Judul: {judul} | Jenis: {jenis}"

# ------------------------------
# 2. LIHAT DATA
# ------------------------------
def lihat():
    print("\n--- Daftar Buku Perpustakaan ---")

    if len(dataBuku) == 0:
        print("Belum ada data buku.\n")
        return

    nomor = 1
    for buku in dataBuku:
        # Menggunakan fungsi format_buku yang baru
        print(f"{nomor}. {format_buku(buku)}")
        nomor += 1
    print()


# ------------------------------
# 3. UBAH DATA
# ------------------------------
def ubah():
    global dataBuku

    if len(dataBuku) == 0:
        print("Belum ada data buku.\n")
        return

    print("\n--- Daftar Buku ---")
    nomor = 1
    for buku in dataBuku:
        # Menggunakan fungsi format_buku
        print(f"{nomor}. {format_buku(buku)}")
        nomor += 1
    print()

    judulCari = input("Masukkan JUDUL buku yang mau diubah: ")

    for buku in dataBuku:
        if buku[0].lower() == judulCari.lower():
            print("\nData ketemu.")

            # Ubah Judul
            judulBaru = input(f"Judul baru (lama: {buku[0]}): ")
            if judulBaru != "":
                buku[0] = judulBaru
            
            # Ubah Jenis
            jenisBaru = input(f"Jenis baru (lama: {buku[1]}): ")
            if jenisBaru != "":
                buku[1] = jenisBaru

            # --- Tambahan untuk Ubah Volume Buku ---
            volume_lama_str = str(buku[2]) if buku[2] is not None else "Tidak Ada"
            
            while True:
                volumeBaru_str = input(f"Volume baru (lama: {volume_lama_str}, kosongi untuk tetap/hapus, masukkan angka): ")
                
                if volumeBaru_str == "":
                    # Jika input kosong, pertahankan nilai lama
                    break 
                
                if volumeBaru_str.lower() in ("kosong", "hapus", "none", "-"):
                    buku[2] = None
                    break
                    
                try:
                    volumeBaru = int(volumeBaru_str)
                    buku[2] = volumeBaru
                    break
                except ValueError:
                    print("Volume harus berupa angka, dikosongkan, atau ketik 'hapus'. Silakan coba lagi.")
            # ------------------------------------

            print("Data berhasil diupdate.\n")
            return

    print("Judul buku tidak ditemukan.\n")


# ------------------------------
# 4. HAPUS DATA
# ------------------------------
def hapus():
    global dataBuku

    if len(dataBuku) == 0:
        print("Belum ada data.\n")
        return

    print("\n--- Hapus Data Buku ---")
    nomor = 1
    for buku in dataBuku:
        print(f"{nomor}. {format_buku(buku)}") # Menggunakan format_buku
        nomor += 1
    print()

    judulCari = input("Masukkan JUDUL buku yang mau dihapus: ")

    index = 0
    ketemu = False

    while index < len(dataBuku):
        if dataBuku[index][0].lower() == judulCari.lower():
            ketemu = True

            print("\nBuku yang akan dihapus:")
            print(f"Judul : {dataBuku[index][0]}")
            print(f"Jenis : {dataBuku[index][1]}")
            # --- Tambahan tampilan Volume ---
            volume_tampil = dataBuku[index][2] if dataBuku[index][2] is not None else "Tidak Ada"
            print(f"Volume: {volume_tampil}")
            # -------------------------------

            yakin = input("\nYakin dihapus? (y/n): ")

            if yakin.lower() == "y":
                dataBuku.pop(index)
                print("Data dihapus.\n")
            else:
                print("Data tidak dihapus.\n")
            
            break 

        index += 1

    if not ketemu:
        print("Judul buku tidak ditemukan.\n")


# ------------------------------
# 5. CARI DATA (Per Jenis)
# ------------------------------
def cari():
    jenisCari = input("Masukkan JENIS buku yang dicari (misal: Komik): ")
    
    ketemu = False
    nomor = 1
    print(f"\n--- Hasil Pencarian Jenis: {jenisCari} ---")

    for buku in dataBuku:
        if jenisCari.lower() in buku[1].lower():
            # --- Tambahan tampilan Volume ---
            volume_tampil = buku[2] if buku[2] is not None else ""
            if volume_tampil != "":
                volume_tampil = f" (Vol. {volume_tampil})"
            
            print(f"{nomor}. Judul: {buku[0]}{volume_tampil}")
            # --------------------------------
            ketemu = True
            nomor += 1

    if not ketemu:
        print("Tidak ada buku dengan jenis tersebut.\n")
    else:
        print() 


# ------------------------------
# 6. URUTKAN DATA (Abjad Judul)
# ------------------------------
def urutkan():
    global dataBuku

    if len(dataBuku) == 0:
        print("Belum ada data.\n")
        return

    panjang = len(dataBuku)

    # Selection Sort (A-Z)
    for i in range(panjang - 1):
        posisiTerkecil = i

        for j in range(i + 1, panjang):
            # Membandingkan berdasarkan Judul (index 0)
            if dataBuku[j][0].lower() < dataBuku[posisiTerkecil][0].lower():
                posisiTerkecil = j

        dataBuku[i], dataBuku[posisiTerkecil] = dataBuku[posisiTerkecil], dataBuku[i]

    print("\nData buku sudah diurutkan sesuai Abjad Judul (A-Z).\n")


# ------------------------------
# MENU UTAMA
# ------------------------------
def menu():
    print("===================================")
    print("        Manajemen Data Buku        ")
    print("===================================")
    print("1. Tambah Buku")
    print("2. Lihat Semua Buku")
    print("3. Ubah Data Buku")
    print("4. Hapus Buku")
    print("5. Cari Buku (Per Jenis)")
    print("6. Urutkan Buku (Abjad)")
    print("7. Keluar")
    return input("Pilih menu (1-7): ")


# ------------------------------
# MAIN PROGRAM
# ------------------------------
def main():
    while True:
        pilih = menu()

        if pilih == "1":
            tambah()
        elif pilih == "2":
            lihat()
        elif pilih == "3":
            ubah()
        elif pilih == "4":
            hapus()
        elif pilih == "5":
            cari()
        elif pilih == "6":
            urutkan()
        elif pilih == "7":
            print("Terima kasih.")
            break
        else:
            print("\nPilihan salah.\n")

        input("ENTER untuk lanjut...")


if __name__ == "__main__":
    main()