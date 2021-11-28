def hitungUmur(tahun_ini):
    nama = input('Nama : ')
    tahun_lahir = int(input('Tahun Lahir :'))
    umur = tahun_ini - tahun_lahir
    print('Siswa bernama %s lahir tahun %i berumur %i tahun' %
          (nama, tahun_lahir, umur))


# panggil fungsi
hitungUmur(2021)

hitungUmur(2022)
