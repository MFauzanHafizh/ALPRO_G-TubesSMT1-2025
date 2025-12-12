# =========================
#  JASA LAUNDRY SEDERHANA
# =========================

def create(data):
    print("\n--- Tambah Pesanan Baru ---")
    nama = input("Masukkan nama pelanggan: ")
    alamat = input("Masukkan alamat pelanggan: ")
    while True:
        try:
            berat = float(input("Masukkan berat laundry (kg): "))
            if berat > 0:
                break
            else:
                print("Berat harus lebih dari 0!")
        except ValueError:
            print("Masukkan angka yang valid!")
    
    layanan = input("Layanan (Cuci+Setrika / Cuci / Setrika): ").title()
    harga_per_kg = 5000
    total_bayar = berat * harga_per_kg

    pesanan = {
        "nama": nama.strip(),
        "alamat": alamat.strip(),
        "berat": berat,
        "layanan": layanan,
        "total_bayar": total_bayar
    }

    data.append(pesanan)
    print("Pesanan berhasil ditambahkan!\n")
    return data


def read(data):
    if not data:
        print("Tidak ada data pesanan.\n")
        return
    
    print("\n" + "="*60)
    print("                  DAFTAR PESANAN LAUNDRY")
    print("="*60)
    for i, p in enumerate(data, 1):
        print(f"{i:<2}. {p['nama']:<15} | {p['berat']:>5} kg | {p['layanan']:<15} | Rp{3['total_bayar']:>10,.0f}")
    print("="*60 + "\n")


def update(data):
    if not data:
        print("Tidak ada data untuk diupdate.\n")
        return data

    read(data)
    try:
        no = int(input("Nomor pesanan yang ingin diupdate: "))
        if 1 <= no <= len(data):
            p = data[no - 1]
            print("Kosongkan jika tidak ingin diubah.\n")

            nama = input(f"Nama [{p['nama']}]: ").strip() or p['nama']
            alamat = input(f"Alamat [{p['alamat']}]: ").strip() or p['alamat']
            
            berat_input = input(f"Berat [{p['berat']} kg]: ").strip()
            if berat_input:
                berat = float(berat_input)
            else:
                berat = p['berat']
                
            layanan = input(f"Layanan [{p['layanan']}]: ").strip() or p['layanan']

            total_bayar = berat * 5000

            data[no - 1] = {
                "nama": nama,
                "alamat": alamat,
                "berat": berat,
                "layanan": layanan,
                "total_bayar": total_bayar
            }
            print("Data berhasil diupdate!\n")
        else:
            print("Nomor tidak valid.\n")
    except ValueError:
        print("Input harus berupa angka!\n")
    return data


def delete(data):
    if not data:
        print("Tidak ada data untuk dihapus.\n")
        return data

    read(data)
    try:
        no = int(input("Nomor pesanan yang ingin dihapus: "))
        if 1 <= no <= len(data):
            hapus = data.pop(no - 1)
            print(f"Pesanan atas nama {hapus['nama']} berhasil dihapus!\n")
        else:
            print("Nomor tidak valid.\n")
    except ValueError:
        print("Input harus angka!\n")
    return data


# =========================
#      FITUR SEARCHING
# =========================
def search(data):
    if not data:
        print("Tidak ada data untuk dicari.\n")
        return

    keyword = input("\nMasukkan nama pelanggan yang dicari: ").lower()
    hasil = [p for p in data if keyword in p["nama"].lower()]

    if hasil:
        print(f"\nDitemukan {len(hasil)} data:\n")
        for p in hasil:
            print(f"→ {p['nama']} | {p['berat']}kg | {p['layanan']} | Rp{p['total_bayar']:,.0f}")
    else:
        print("Tidak ditemukan data yang sesuai.\n")
    print()


# =========================
#      FITUR SORTING 
# =========================

import operator

def sorting(data):
    if not data:
        print("Tidak ada data untuk diurutkan.\n")
        return data

    print("\nUrutkan berdasarkan Total Bayar:")
    print("1. Termahal → Termurah (besar → kecil)")
    print("2. Termurah → Termahal (kecil → besar)")
    
    try:
        pilih = int(input("Pilih (1 atau 2): "))
        
        if pilih == 1:
            data.sort(key=operator.itemgetter("total_bayar"), reverse=True)
            print("Data berhasil diurutkan dari Termahal → Termurah.\n")
        
        elif pilih == 2:
            data.sort(key=operator.itemgetter("total_bayar"))
            print("Data berhasil diurutkan dari Termurah → Termahal.\n")
        
        else:
            print("Pilihan tidak valid! Harus 1 atau 2.\n")
            return data
    
    except ValueError:
        print("Input harus angka!\n")
        return data
    
    print("\n" + "="*60)
    print("           DAFTAR PESANAN SETELAH DIURUTKAN")
    print("="*60)
    for i, p in enumerate(data, 1):
        print(f"{i:<2}. {p['nama']:<15} | {p['berat']:>5} kg | {p['layanan']:<15} | Rp{p['total_bayar']:>10,.0f}")
    print("="*60 + "\n")
    
    return data

# =========================
#       MENU UTAMA 
# =========================
def menu():
    print("===================================")
    print("=== JASA LAUNDRY ONLINE ===")
    print("===================================")
    print("1. Tambah Pesanan")
    print("2. Lihat Pesanan")
    print("3. Edit Pesanan")
    print("4. Hapus Pesanan")
    print("5. Cari Pesanan")
    print("6. Urutkan Data")
    print("7. Keluar")

    try:
        pilih = int(input("Masukkan pilihan [1-7]: "))
        return pilih
    except ValueError:
        print("Input harus angka!\n")
        return 0

# =========================
#      PROGRAM UTAMA
# =========================
data_pesanan = []
pilihan = 0

print("Selamat datang di Jasa Laundry Online!")

while pilihan != 7:
    pilihan = menu()

    if pilihan == 1:
        data_pesanan = create(data_pesanan)
    elif pilihan == 2:
        read(data_pesanan)
    elif pilihan == 3:
        data_pesanan = update(data_pesanan)
    elif pilihan == 4:
        data_pesanan = delete(data_pesanan)
    elif pilihan == 5:
        search(data_pesanan)
    elif pilihan == 6:
        data_pesanan = sorting(data_pesanan)
    elif pilihan == 7:
        print("\nTerima kasih telah menggunakan Jasa Laundry Kami")
        print("Semoga hari Anda menyenangkan!")
    else:
        if pilihan != 0:

            print("Pilihan tidak valid! Silakan pilih 1-7.\n")
