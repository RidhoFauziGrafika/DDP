daftar_makanan = [
    ['Bakwan', 'Combro', 'Misro'],
    ['Sop Iga', 'Sop Buntut', 'Sop Kaki'],
    ['Nasi Uduk', 'Nasi Goreng', 'Nasi Rames']
]
print('------- cetak per item ----------')
print(daftar_makanan[0][0])
print(daftar_makanan[1][1])
print(daftar_makanan[2][1])

print('------- cetak all item nesteploop ----------')
for menu in daftar_makanan:
    for makanan in menu:
        print(makanan)
