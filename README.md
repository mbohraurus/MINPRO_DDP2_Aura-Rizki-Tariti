# MINPRO_DDP2_Aura-Rizki-Tariti

Nama: Aura Rizki Tariti
Kelas: A'
Angkatan: 2026
NIM: 2609116032

Kode kali ini sama saja dengan yang versi Mini Project 1 DDP saya, tapi ada pembedaan fitur tergantung pengguna mana yang menggunakan sistem ini (admin atau pelanggan). Sesuai instruksi tugas, pengguna akan diarahkan untuk log-in dengan mengisi username serta password terlebih dulu (pengguna dianggap memang sudah memiliki akun). Kemudian, username dan password akan dicocokkan ke dictionary akun, lalu pengguna akan diminta memasukkan ulang username dan password mereka jika ada kesalahan dalam pengisian sebelumnya. Admin berhak menambah, membuat, mengubah, dan menghapus data bahan beserta jumlah stoknya (dalam function info_restock), di samping mengecek ketersediaan stok baik per masing-masing jenis bahan setelah adanya penggunaan (cek_stok) ataupun secara keseluruhan (cek_all). Sedangkan pelanggan hanya bisa mengecek stok bahan yang tersedia satu per satu (cek_stok) atau keseluruhan setelah melakukan pemesanan (cek_all). Library yang saya gunakan di sini hanya pwinput untuk menyembunyikan karakter yang diketik pengguna saat input password. Awalnya saya ingin menggunakan library prettytable juga untuk fitur menampilkan data stok dari dictionary bahan, tapi tidak jadi karena malah ada bug (elemen dalam baris/row tidak ada karena menggunakan variabel key dan value dari dictionary bahan).

Ini contoh hasil output untuk penggunaan function paling sederhana dalam program ini yaitu cek_all:
<img width="752" height="320" alt="Screenshot 2026-10-07 003345" src="https://github.com/user-attachments/assets/c9a6d486-12c2-422f-bdbc-0f913a89b5ef" />
