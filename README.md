# Praktikum_7_Pertemuan_10

*A. ALGORITMA PROGRAM*

1.	Mulai Program
   
        Inisialisasi dictionary data_mahasiswa kosong untuk menyimpan data mahasiswa.
  	 
2.	Tampilkan Menu Utama
   
   Pilihan menu:
   
     Lihat Data (L)
     Tambah Data (T)
     Ubah Data (U)
     Hapus Data (H)
     Cari Data (C)
     Keluar (K)
      
3. Input Pilihan Pengguna
   
>> Lihat Data (L):

     Jika data_mahasiswa kosong, tampilkan pesan "TIDAK ADA DATA".

     Jika ada data, tampilkan tabel data mahasiswa.

>> Tambah Data (T):

     Minta input NIM, Nama, Nilai Tugas, UTS, dan UAS. 
     
     Hitung Nilai Akhir dengan rumus : Nilai Akhir = (Tugas * 0.3) + (UTS * 0.35) + (UAS * 0.35)

     Simpan data ke dalam dictionary.

     Tampilkan pesan "Data berhasil ditambahkan".

>> Ubah Data (U):

     Minta input NIM yang ingin diubah.
     
     Jika NIM ditemukan, minta data baru, hitung ulang Nilai Akhir, dan perbarui dictionary.
     
     Jika NIM tidak ditemukan, tampilkan pesan "Data tidak ditemukan".

>> Hapus Data (H):

     Minta input NIM yang ingin dihapus.

     Jika NIM ditemukan, hapus dari dictionary.

     Jika tidak, tampilkan pesan "Data tidak ditemukan".

>> Cari Data (C):

     Minta input NIM yang ingin dicari.
     
     Jika NIM ditemukan, tampilkan data mahasiswa tersebut.
     
     Jika tidak, tampilkan pesan "Data tidak ditemukan".

>> Keluar (K):

     Tampilkan pesan "Keluar dari program".
     
     Hentikan program.
     
4.	Kembali ke Menu Utama jika pengguna belum memilih "Keluar (K)".
   
5.	Selesai Program.

#

*B. FLOWCHART*

![image](https://github.com/user-attachments/assets/a472a526-3507-44a6-a26e-b21983d090ae)

#

*C. CODE PROGRAM DAN PENJELASAN*

![image](https://github.com/user-attachments/assets/b2861a4c-25c2-4bf5-b954-8afd24f7ca26)

![image](https://github.com/user-attachments/assets/2987d597-baf0-4c1b-b8a6-49689d54745e)

PENJELASAN CODE : 

     data_mahasiswa = {}

Fungsi: Mendefinisikan sebuah dictionary kosong bernama data_mahasiswa yang akan digunakan untuk menyimpan data mahasiswa. Di dalam dictionary ini, NIM (Nomor Induk Mahasiswa) akan menjadi kunci, dan informasi mahasiswa lainnya (nama, nilai tugas, UTS, UAS, dan nilai akhir) akan disimpan sebagai nilai.

     def tampilkan_data():
     
Fungsi: Mendefinisikan fungsi tampilkan_data yang bertugas untuk menampilkan daftar nilai mahasiswa.   

     if data_mahasiswa:

Fungsi: Memeriksa apakah data_mahasiswa tidak kosong. Jika ada data, maka akan ditampilkan.

      print("\nDaftar Nilai")  
      print("="*67) 
      
Fungsi: Mencetak header untuk tabel yang akan ditampilkan, memberikan informasi bahwa yang akan ditampilkan adalah daftar nilai.
