# POV: Manajemen Ketersediaan Bahan di Perusahaan Reklame dan Percetakan

# Kedua: Data Bahan dan Akun Pengguna
# luas bahan spanduk, neon box, baliho (dalam hitungan meter persegi (m^2)):
# luas bahan spanduk, neon box, baliho (dalam hitungan meter persegi (m^2)):

bahan = {
    "albatros": 150,           # (1 roll ukuran 3 x 50 meter)
    "flexy china": 150,        # (1 roll ukuran 3 x 50 meter)
    "flexy korea": 150,       # (1 roll ukuran 3 x 50 meter)

    # luas bahan lain (dalam hitungan sentimeter persegi (cm^2)):
    "stiker bening": 300000,   # (1 roll ukuran 100 x 3000 cm)
    "stiker vinyl": 300000,    # (1 roll ukuran 100 x 3000 cm)
    "stiker backlit": 300000,  # (1 roll ukuran 100 x 3000 cm)
    "PVC namecard": 3000       # (5 lembaran set, ukuran 20 x 30 cm)
}
akun = {
    "260001": "adminiboss",
    "260010": "iniuserrr"
}

# Kedua: deklarasi function, list, dan library
import pwinput
bahan_habis = []
list_restock = []
kuantitas = []
def cek_stok():
    while True:
        jenis = input("Jenis bahan sesuai request pemesan: ")
        if jenis in bahan:
            jumlah = int(input("Jumlah pesanan: "))
            p = int(input("Panjang (dalam satuan cm untuk produk stiker dan PVC namecard, dalam satuan meter untuk produk selainnya): "))
            l = int(input("Lebar (dalam satuan cm untuk produk stiker dan PVC namecard, dalam satuan meter untuk produk selainnya): "))
            ukuran = p * l
            kebutuhan = ukuran * jumlah
            if kebutuhan <= bahan[jenis]:
                bahan[jenis] -= kebutuhan
                print("Pesanan dapat diproses.")
                print("Sisa ukuran bahan yang tersedia:", bahan[jenis])
            else:
                print("Sisa bahan ini tidak tersedia/tidak mencukupi kebutuhan pemesanan.")
                if jenis not in bahan_habis:
                    bahan_habis.append(jenis)
            klik = input("Lanjutkan? ")
            print()
            if klik == "lanjutkan":
                continue
            else:
                return False
        else:
            print("Perusahaan belum menyediakan jasa pembuatan reklame atau produk lainnya berbahan ini")
            return False
def info_restock():
    if len(bahan_habis) >= 1:
        print("Bahan yang stoknya kosong/tidak mencukupi:", bahan_habis)
        opsi_restock = input("Ketik 'Tambahkan' jika ada bahan yang akan segera restock: ")
        print()
        while True:
            if opsi_restock == "Tambahkan":
                jenis_restock = input("Bahan yang dibeli (ketik 'Tidak ada' jika selesai): ")
                pjg = int(input("Panjang: "))
                lbr = int(input("Lebar: "))
                jumlah_restock = int(input("Jumlah lembaran/roll bahan: "))
                if pjg <= 0 or lbr <= 0 or jumlah_restock <= 0:
                    print("Ukuran dan jumlah restock harus lebih dari 0.")
                    continue
                ukuran_restock = pjg * lbr
                total = ukuran_restock * jumlah_restock
                bahan[jenis_restock] += total
                list_restock.append(jenis_restock)
                kuantitas.append(total)
                if jenis_restock in bahan_habis:
                    bahan_habis.remove(jenis_restock)
                print("Restock berhasil. Stok", jenis_restock, "sekarang:", bahan[jenis_restock])
                opsi_restock = input("Tambahkan restock lain? Ketik 'Tambahkan' atau 'Tidak ada': ")
                if opsi_restock == "tidak ada":
                    return False
            else:
                print("Bahan belum tersedia, order yang membutuhkan bahan ini tidak bisa diproses sebelum bahan kembali restock")
                return False
    else:
        print("Stok bahan masih aman seluruhnya. Semua pesanan siap diproses")
def cek_all():
    for jenis, stok in bahan.items():
        print(jenis, ":", stok)


# Ketiga: Fitur yang Dilihat Pengguna
print("Selamat datang kembali....")
print("Silakan log-in dengan username dan kata sandi Anda untuk menggunakan layanan ini")
status_user = input("Masuk sebagai: ADMIN/PELANGGAN? ")
username = input("Username: ")
password = pwinput.pwinput("Kata Sandi: ")
while True:
    if username in akun:
        if password == akun[username]:
            if status_user == "PELANGGAN":
                while True:
                    pilihan = input("AJUKAN PESANAN/CEK BAHAN YANG TERSEDIA/KELUAR? ")
                    if pilihan == "AJUKAN PESANAN":
                        proses_cek = cek_stok()
                        if proses_cek == False:
                            break
                        else:
                            continue
                    elif pilihan == "CEK BAHAN YANG TERSEDIA":
                        proses_ini = cek_all()
                        if proses_ini == False:
                            break
                        else:
                            continue
                    elif pilihan == "KELUAR":
                        break
                    else:
                        print("Maaf, menu yang Anda ketik tidak valid atau tidak sesuai ketentuan")
                        continue
            elif status_user == "ADMIN":
                while True:
                    pilihan = input("KELOLA PESANAN/CEK BAHAN YANG TERSEDIA/KELOLA RESTOCK/KELUAR? ")
                    if pilihan == "KELOLA PESANAN":
                        proses_cek = cek_stok()
                        if proses_cek == False:
                            break
                        else:
                            continue
                    elif pilihan == "CEK BAHAN YANG TERSEDIA":
                        proses_ini = cek_all()
                        if proses_ini == False:
                            break
                        else:
                            continue
                    elif pilihan == "KELOLA RESTOCK":
                        kelola = info_restock()
                        if kelola == False:
                            break
                        else:
                            continue
                    elif pilihan == "KELUAR":
                        break
                    else:
                        print("Maaf, menu yang Anda ketik tidak valid atau tidak sesuai ketentuan")
                        continue
            else:
                print("Maaf, hanya admin dan pelanggan yang diperkenankan log-in dan menggunakan layanan ini")
                break
        else:
            print("Kata sandi Anda tidak valid, mohon masukkan kembali dengan benar")
            username = input("Username: ")
            password = pwinput.pwinput("Kata Sandi: ")
            continue
    else:
        print("Username Anda tidak valid, mohon masukkan kembali dengan benar")
        username = input("Username: ")
        password = pwinput.pwinput("Kata Sandi: ")
        continue
    log_out = input("Ketik 0 untuk log-out: ")
    if log_out == "0":
        print("Terima kasih telah menggunakan dan mempercayakan jasa pembuatan reklame di perusahaan kami")
        break
    else:
        status_user = input("Masuk sebagai: ADMIN/PELANGGAN? ")
        username = input("Username: ")
        password = pwinput.pwinput("Kata Sandi: ")
        continue