batas_nilai = (65, 100)
nilai_masuk = []
lulus = []
remedi = []

print("Pengelompokan Nilai uJian")

while True:
    input_nilai = input("Masukkan nilai: ")

    if input_nilai == "selesai":
        if len(nilai_masuk) < 5:
            print("nilai yg dimasukkan belum 5")
            continue
        else:
            break

    nilai = int(input_nilai)

    if nilai < 0 or nilai > 100:
        print("Nilai harus 0-100")
        continue

    nilai_masuk.append(nilai)

    if nilai >= batas_nilai[0]:
        lulus.append(nilai)
    else:
        remedi.append(nilai)


print(f"nilai yang sudah dimasukkan : {nilai_masuk}")

while True:
    hapus = input("apa ada nilai yang ingin dihapus?")

    if hapus == "tidak":
        break

    elif hapus == "ya":
        nilai_hapus = int(input("masukkan nilai yang ingin dihapus: "))
        if nilai_hapus in nilai_masuk:
                nilai_masuk.remove(nilai_hapus)
                
                if nilai_hapus in lulus:
                    lulus.remove(nilai_hapus)
                elif nilai_hapus in remedi:
                    remedi.remove(nilai_hapus)

        else:
            print("nilai tidak ditemukan")
            break

print("batas nilai:", batas_nilai)
print("nilai masuk:", nilai_masuk)
print("nilai lulus:", lulus)
print("nilai remedi:", remedi)  


