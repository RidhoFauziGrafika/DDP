print('---------banyak input---------')
nama = input('Nama: ')
gender = str(input('Jenis Kelamin: '))
umur = int(input('Umur: '))
beratBadan = float(input('Berat Badan: '))

print("Nama\t\t: %s"
      "\nJenis Kelamin\t: %s"
      "\nUmur\t\t: %i tahun"
      "\nBerat Badan\t: %.2f tahun" % (nama, gender, umur, beratBadan))
