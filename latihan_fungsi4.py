def hitungGaji():
    nama = input('Nama Pegawai\t\t :')
    jabatan = input('Jabatan\t\t\t :')
    agama = input('Agama\t\t\t :')
    jumlah = int(input('Jumlah Anak\t\t :'))

    def gapok(jabatan):
        return {
            'General Manager': 20000000,
            'Manager': 10000000,
            'Staff': 5000000
        }[jabatan]
    # tunjangan jabatan
    tunjab = 0.2 * gapok(jabatan)
    # tunjangan keluarga
    persen = 0.1
    if(jumlah > 0 and jumlah < 4):
        tunkel = gapok(jabatan) * persen
    elif(jumlah > 3):
        tunkel = gapok(jabatan) * persen * (jumlah-(jumlah - 3))
    else:
        tunkel = 0

    gaji_kotor = gapok(jabatan) + tunkel
    zakat = (0, 0.025 * gaji_kotor)[gaji_kotor >= 6000000 and agama == 'Islam']
    gaji_bersih = gapok(jabatan) + tunkel - zakat

    print('Nama Pegawai\t\t: %s'
          '\nJabatan\t\t\t: %s'
          '\nAgama\t\t\t: %s'
          '\nJumlah Anak\t\t: %i'
          "\nGaji Pokok\t\t: %i"
          '\nTunjangan Jabatan\t: %i'
          '\nGaji kotor\t\t: %i'
          '\nZakat Profesi\t\t: %i'
          '\nGaji Bersih\t\t: %i'
          % (nama, jabatan, agama, jumlah, gapok(jabatan), tunjab, gaji_kotor, zakat, gaji_bersih))


# panggil fungsi
hitungGaji()
