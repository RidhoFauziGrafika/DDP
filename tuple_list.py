# siswa yang dinyatakan lulus minimal 60 nilainya
nama = "Budi Santoso"
matkul = "Matematika"
nilai = 90.99

# tuple dan list
keterangan = ("Gagal", "Lulus")[nilai >= 60]

# cetak data
print("Nama Siswa \t:", nama,
      "\nMata Kuliah \t:", matkul,
      "\nNilai \t\t:", nilai,
      "\nKeterangan \t:", keterangan)
