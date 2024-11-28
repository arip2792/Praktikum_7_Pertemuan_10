print("========================= ARIEF ADJI =========================")

data_mahasiswa = {}

def tampilkan_data():
    if data_mahasiswa:
        print("\nDaftar Nilai")
        print("="*67)
        print("| {:<2} | {:<10} | {:<12} | {:<5} | {:<5} | {:<5} | {:<6} |".format(
            "NO", "NIM", "NAMA", "TUGAS", "UTS", "UAS", "AKHIR"))
        print("="*67)
        for i, (nim, data) in enumerate(data_mahasiswa.items(), start=1):
            print("| {:<2} | {:<10} | {:<12} | {:<5} | {:<5} | {:<5} | {:<6.2f} |".format(
                i, nim, data['nama'], data['tugas'], data['uts'], data['uas'], data['akhir']))
        print("="*67)
    else:
        print("\nDaftar Nilai")
        print("="*67)
        print("| {:<2} | {:<10} | {:<12} | {:<5} | {:<5} | {:<5} | {:<6} |".format(
            "NO", "NIM", "NAMA", "TUGAS", "UTS", "UAS", "AKHIR"))
        print("="*67)
        print("|{:^70}|".format("TIDAK ADA DATA"))
        print("="*67)

def tambah_data():
    print("\nTambah Data")
    nim = input("NIM         : ")
    nama = input("Nama        : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))
    akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    data_mahasiswa[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "akhir": akhir}
    print("Data berhasil ditambahkan!")

def ubah_data():
    print("\nUbah Data")
    nim = input("Masukkan NIM yang akan diubah: ")
    if nim in data_mahasiswa:
        print("Data ditemukan. Masukkan data baru.")
        nama = input("Nama        : ")
        tugas = float(input("Nilai Tugas : "))
        uts = float(input("Nilai UTS   : "))
        uas = float(input("Nilai UAS   : "))
        akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
        data_mahasiswa[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "akhir": akhir}
        print("Data berhasil diubah!")
    else:
        print("Data dengan NIM tersebut tidak ditemukan.")

def hapus_data():
    print("\nHapus Data")
    nim = input("Masukkan NIM yang akan dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data berhasil dihapus!")
    else:
        print("Data dengan NIM tersebut tidak ditemukan.")

def cari_data():
    print("\nCari Data")
    nim = input("Masukkan NIM yang dicari: ")
    if nim in data_mahasiswa:
        data = data_mahasiswa[nim]
        print("\nData Ditemukan:")
        print(f"NIM         : {nim}")
        print(f"Nama        : {data['nama']}")
        print(f"Nilai Tugas : {data['tugas']}")
        print(f"Nilai UTS   : {data['uts']}")
        print(f"Nilai UAS   : {data['uas']}")
        print(f"Nilai Akhir : {data['akhir']:.2f}")
    else:
        print("Data dengan NIM tersebut tidak ditemukan.")

while True:
    print("\nProgram Input Nilai")
    print("===================")
    print("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar")
    pilihan = input("Pilih menu: ").lower()

    if pilihan == 'l':
        tampilkan_data()
    elif pilihan == 't':
        tambah_data()
    elif pilihan == 'u':
        ubah_data()
    elif pilihan == 'h':
        hapus_data()
    elif pilihan == 'c':
        cari_data()
    elif pilihan == 'k':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
