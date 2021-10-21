# struktur kendali if
pelanggan = "Ridho Fauzi"
totalBelanja = 90000

# if(totalBelanja >= 100000):
#   keterangan = "Selamat Anda Mendapatkan Hadiah"
# else:
#    keterangan = "Terima kasih telah belanja di toko kami"
keterangan = "selamat anda mendapatkan hadiah" if totalBelanja >= 100000 else "terima kasih telah berbelanja di toko kami"
print("Pelanggan", pelanggan, "telah berbelanja",
      totalBelanja, keterangan)
