# Simulasi Pelayanan Antrian Klinik di Sebuah Negeri Bernama....
print("Pendataan Pasien")

# Pertama: data antriannya gimana nih?
antrian = ["10002", "10003", "20004", "20005"]

# Kedua: pisahkan loket
pasien_BPJS = []
bayar_mandiri = []
while len(antrian) < 0:
         if pasien >= 20000:
             pasien_BPJS.append(pasien)
         else:
             bayar_mandiri.append(pasien)
    break

# Terakhir: infokan jumlah pelayanan hari ini
print()
print("Data Pengunjung Harian")
print("Jumlah pasien prioritas pada hari ini:", len(bayar_mandiri), "orang")
print("Jumlah pasien biasa pada hari ini:", len(pasien_BPJS), "orang")