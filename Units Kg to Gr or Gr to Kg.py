#Ubah satuan 
def Kg(kg):
    return kg*1000
def Gr(gr):
    return gr/1000

while True:
    print("\n===== UBAH SATUAN =====")
    print("1. kg to g")
    print("2. g to kg")
    print("3. Keluar")
    pilihan = input("Pilih operasi (1-3): ")
    
    if pilihan == '1' or pilihan == '2':
        try:
            berat = float(input("Masukkan angka: "))
            if pilihan == "1":
                hasil = Kg(berat)
                print(f'Hasil: {hasil: .3f} Kg')
            elif pilihan == "2":
                hasil = Gr(berat)
                print(f'Hasil: {hasil: .5f} Gr')
        except ValueError:
            print("Input harus berupa angka!")
    elif pilihan == '3':
        print("\nTerima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1-3.")
