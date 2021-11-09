data_nilai = {'Siti': 75, 'Inaya': 98, 'Bedu': 59,
              'Fawwaz': 100, 'Zaki': 88, 'Ina': 40}
data_nilai['Siti'] = 80  # ubah data
data_nilai.pop('Ina')
del data_nilai['Zaki']

# cetak all
print('Data nilai:', data_nilai)

# cetak nilai(value)nya saja
for nilai in data_nilai.values():
    print('Daftar nilai:', nilai)

# cetak key(index)nya saja
for nama in data_nilai.keys():
    print('Daftar siswa:', nama)

# cetak all manual
for nama, nilai in data_nilai.items():
    ket = ('Lulus', 'Gagal')[nilai < 60]
    print('Siswa:', nama, 'nilai:', nilai, 'dinyatakan', ket)
