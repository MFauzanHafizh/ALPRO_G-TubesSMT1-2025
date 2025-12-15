# Program Kasir Sederhana
menu = {
    "nasi goreng": 15000,
    "ayam goreng": 20000,
    "es teh": 5000,
    "kopi": 7000,
    "ikan bakar": 25000
}

keranjang = {}

def tampil_menu():
    print("\nMenu:")
    for item, harga in menu.items():
        print(f"{item}: Rp{harga}")

def hitung_total():
    total_harga = 0
    total_item = 0
    for item, jumlah in keranjang.items():
        total_harga += menu[item] * jumlah
        total_item += jumlah
    print(f"Total item: {total_item}, Total harga: Rp{total_harga}")
    return total_harga, total_item

def kasir():
    while True:
        print("===============================") 
        print("===          MENU           ===") 
        print("===============================")
        print("\nPilih:")
        print("1. Tambah menu")
        print("2. Tambah ke keranjang")
        print("3. Hapus dari keranjang")
        print("4. Edit pesanan")
        print("5. Lihat keranjang")
        print("6. Checkout")
        print("7. Total semua menu")
        print("8. Cari menu")
        print("9. Urutkan menu")
        print("10. Keluar")
        
        pilihan = input("Masukkan pilihan: ")
        
        if pilihan == "1":
            item = input("Nama item: ").lower()
            if item in menu:
                print("Sudah ada.")
            else:
                harga = int(input("Harga: "))
                menu[item] = harga
                print("Ditambah.")
        
        elif pilihan == "2":
            tampil_menu()
            item = input("Item: ").lower()
            if item not in menu:
                print("Tidak ada.")
            else:
                jumlah = int(input("Jumlah: "))
                if item in keranjang:
                    keranjang[item] += jumlah
                else:
                    keranjang[item] = jumlah
                print("Ditambah.")
                hitung_total()
        
        elif pilihan == "3":
            if not keranjang:
                print("Kosong.")
            else:
                item = input("Item hapus: ").lower()
                if item not in keranjang:
                    print("Tidak ada.")
                else:
                    jumlah = int(input("Jumlah hapus: "))
                    keranjang[item] -= jumlah
                    if keranjang[item] <= 0:
                        del keranjang[item]
                    print("Dihapus.")
                    hitung_total()
        
        elif pilihan == "4":
            if not keranjang:
                print("Kosong.")
            else:
                print("Keranjang:")
                for item, jumlah in keranjang.items():
                    print(f"{item} x{jumlah}")
                item = input("Item edit: ").lower()
                if item not in keranjang:
                    print("Tidak ada.")
                else:
                    jumlah_baru = int(input("Jumlah baru: "))
                    if jumlah_baru <= 0:
                        del keranjang[item]
                        print("Dihapus.")
                    else:
                        keranjang[item] = jumlah_baru
                        print("Diedit.")
                    hitung_total()
        
        elif pilihan == "5":
            print("Keranjang:")
            for item, jumlah in keranjang.items():
                print(f"{item} x{jumlah}")
            hitung_total()
        
        elif pilihan == "6":
            if not keranjang:
                print("Kosong.")
            else:
                hitung_total()
                print("Checkout selesai.")
                keranjang.clear()
        
        elif pilihan == "7":
            total_menu = sum(menu.values())
            print(f"Total harga semua menu: Rp{total_menu}")
        
        # --- MULAI SEARCHING  ---
        elif pilihan == "8":
            # Fitur Searching: Cari berdasarkan nama item atau harga
            query = input("Masukkan nama item atau harga untuk dicari: ").lower()
            found = False
            print("\nHasil pencarian:")
            for item, harga in menu.items():
                if query in item or str(harga) == query:
                    print(f"{item}: Rp{harga}")
                    found = True
            if not found:
                print("Tidak ditemukan.")
        # --- AKHIR SEARCHING ---
        
        # --- MULAI SORTING  ---
        elif pilihan == "9":
            # Fitur Sorting: Urutkan menu berdasarkan nama atau harga
            print("Urutkan berdasarkan:")
            print("1. Nama (A-Z)")
            print("2. Nama (Z-A)")
            print("3. Harga (rendah-tinggi)")
            print("4. Harga (tinggi-rendah)")
            sub_pilihan = input("Pilih: ")
            if sub_pilihan == "1":
                sorted_menu = sorted(menu.items(), key=lambda x: x[0])
            elif sub_pilihan == "2":
                sorted_menu = sorted(menu.items(), key=lambda x: x[0], reverse=True)
            elif sub_pilihan == "3":
                sorted_menu = sorted(menu.items(), key=lambda x: x[1])
            elif sub_pilihan == "4":
                sorted_menu = sorted(menu.items(), key=lambda x: x[1], reverse=True)
            else:
                print("Pilihan salah.")
                continue
            print("\nMenu yang diurutkan:")
            for item, harga in sorted_menu:
                print(f"{item}: Rp{harga}")
        # --- AKHIR SORTING ---
        
        elif pilihan == "10":
            print("Terima Kasih sudah membeli :) Jangan lupa kembali lagi")
            break
        
        else:
            print("Salah.")

kasir()
