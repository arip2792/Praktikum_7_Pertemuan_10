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

1. Fungsi tampilkan_data()

![image](https://github.com/user-attachments/assets/8688910d-37f4-485a-9c36-55f684da49f4)

>Fungsi ini menampilkan daftar nilai mahasiswa.

>Jika data_mahasiswa tidak kosong, fungsi mencetak tabel dengan kolom untuk nomor urut, NIM, nama, nilai tugas, UTS, UAS, dan nilai akhir.

>Data mahasiswa akan ditampilkan dan nilai akhir ditampilkan dengan dua angka desimal.

>Jika tidak ada data, fungsi mencetak pesan "TIDAK ADA DATA" untuk memberi tahu pengguna bahwa tidak ada informasi yang tersedia.

2. Fungsi tambah_data()

![image](https://github.com/user-attachments/assets/a9f95c7d-775f-4e5c-8074-81f51005e6b0)

>Fungsi ini digunakan untuk menambahkan data mahasiswa baru ke dalam sistem.

>Pengguna diminta untuk memasukkan NIM, nama, dan nilai untuk tugas, UTS, dan UAS.

>Nilai akhir dihitung berdasarkan bobot nilai yang telah ditentukan (30% untuk tugas, 35% untuk UTS, dan 35% untuk UAS).

>Data mahasiswa disimpan dalam dictionary data_mahasiswa dengan NIM sebagai kunci dan informasi lainnya sebagai nilai dalam bentuk dictionary.

>Setelah data ditambahkan, fungsi mencetak pesan konfirmasi bahwa data berhasil ditambahkan.

3. Fungsi ubah_data()

![image](https://github.com/user-attachments/assets/0bd705d0-44ea-4048-a035-4e10124f4c74)

>Fungsi ini memungkinkan pengguna untuk mengubah data mahasiswa yang sudah ada.

>Pengguna diminta untuk memasukkan NIM mahasiswa yang ingin diubah.

>Jika NIM ditemukan dalam data_mahasiswa, pengguna diminta untuk memasukkan data baru (nama dan nilai).

>Nilai akhir dihitung kembali dan data diperbarui dalam dictionary.

>Jika NIM tidak ditemukan, fungsi mencetak pesan bahwa data tidak ada.

4. Fungsi hapus_data()

![image](https://github.com/user-attachments/assets/ca6c1507-e546-45e0-a052-a4612e5c0e5b)

>Fungsi ini digunakan untuk menghapus data mahasiswa berdasarkan NIM.

>Pengguna diminta untuk memasukkan NIM yang ingin dihapus.

>Jika NIM ditemukan, data mahasiswa dihapus dari dictionary data_mahasiswa, dan fungsi mencetak pesan konfirmasi bahwa data berhasil dihapus.

>Jika NIM tidak ditemukan, fungsi mencetak pesan bahwa data tidak ada.

5. Fungsi cari_data()

![image](https://github.com/user-attachments/assets/ae0c74da-aeed-43aa-8b0d-574400f27494)

>Fungsi ini memungkinkan pengguna untuk mencari data mahasiswa berdasarkan NIM.

>Pengguna diminta untuk memasukkan NIM yang ingin dicari.

>Jika NIM ditemukan, fungsi mencetak semua informasi terkait mahasiswa tersebut, termasuk nilai akhir dengan dua angka desimal.

>Jika NIM tidak ditemukan, fungsi mencetak pesan bahwa data tidak ada.

6. Loop/perulangan utama

![image](https://github.com/user-attachments/assets/698e0aea-096e-4d29-abd6-83660a0067fd)

>Pengguna diberikan pilihan untuk melihat, menambah, mengubah, menghapus, atau mencari data mahasiswa, atau keluar dari program.

>Input pengguna diproses, dan fungsi yang sesuai dipanggil berdasarkan pilihan yang dimasukkan.

>Jika pengguna memilih untuk keluar, loop dihentikan, dan program berakhir. Jika pilihan tidak valid, program meminta pengguna untuk mencoba lagi.

#

*D. HASIL RUN CODE*

![image](https://github.com/user-attachments/assets/a9691972-a60e-422a-9776-9b388a20aa25)

![image](https://github.com/user-attachments/assets/eebd46ce-06f6-45a7-aa6a-24bb238d254a)

