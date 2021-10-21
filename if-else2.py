nama = "ridho fauzi"
matkul = "matematika"
nilai = 90.00

# ternary
keterangan = "Lulus" if nilai >= 60 else "gagal"

if (nilai >= 85 and nilai <= 100):
    grade = 'A'
elif(nilai >= 75 and nilai < 85):
    grade = 'B'
elif(nilai >= 60 and nilai < 75):
    grade = 'C'
elif(nilai >= 30 and nilai < 60):
    grade = 'D'
else:
    grade = '-'
print("Data nilai siswa:"
      "\nNama\t\t:", nama, "\nmata kuliah\t:", matkul, "\nNilai\t\t:", nilai, "\nketerangan\t:", keterangan, "\ngrade\t\t:", grade)
