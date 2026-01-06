# Data utama
import os 
Nama = input("Masukkan nama kamu: ").strip().capitalize()
print(f"selamat datang {Nama} ")

def clear():
    if os.name == 'nt':
        os.system('cls')

# Fungsi menambahkan barang
def tambah_barang(daftar, item):
    item = item.strip()
    if item in daftar:
        print(f'{item} tidak dapat ditambahkan karena sudah ada')
    else:
        daftar.append(item)

# Fungsi menghapus barang
def hapus_barang(daftar, item):
    if item in daftar:
        daftar.remove(item)
        print(f"{item} telah dihapus.")
    else:
        print(f"{item} tidak ditemukan.")

# Fungsi menampilkan isi daftar
def tampilkan_daftar(daftar):
    if daftar:
        print("Isi daftar saat ini:")
        for i, barang in enumerate(daftar, start=1):
            print(f"{i}. {barang}")
    else:
        print("Daftar kosong.")

def ganti_barang(daftar, lama, baru):
    if baru in daftar:
        print(f'{baru} tidak dapat ditambahkan karena sudah ada')
    elif lama in daftar:
        a = daftar.index(lama)
        daftar[a] = baru
        print(f'{lama} telah diganti dengan yang {baru}')
    else:
        print(f'{lama} barang yang tidak ditemukan')

# Contoh menu
daftar_belanja1 = []

# Menu utama
while True:
    print("\n--- MENU ---")
    print("1. Manage daftar belanja 1")
    print("2. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        daftar_aktif = daftar_belanja1
    elif pilihan == "2":
        print(f"Terimakasih {Nama}, Program Anda telah selesai.")
        break
    else:
        print("Pilihan tidak valid.")
        continue

    # Menu dalam daftar
    while True:
        print("\n--- MENU DAFTAR ---")
        print("1. Tambah barang")
        print("2. Hapus barang")
        print("3. Tampilkan daftar")
        print("4. Ganti barang")
        print("5. Kembali ke menu utama")

        aksi = input("Pilih aksi: ")

        if aksi == "1":
            item = input("Masukkan nama barang: ")
            tambah_barang(daftar_aktif, item)
        elif aksi == "2":
            item = input("Masukkan nama barang yang ingin dihapus: ")
            hapus_barang(daftar_aktif, item)
        elif aksi == "3":
            tampilkan_daftar(daftar_aktif)
        elif aksi == "4":
            lama = input("Masukkan nama barang yang ingin diganti: ")
            baru = input("Masukkan nama barang baru: ")
            ganti_barang(daftar_aktif, lama, baru)
        elif aksi == "5":
            break  # kembali ke menu utama
        else:
            print("Pilihan tidak ada.")