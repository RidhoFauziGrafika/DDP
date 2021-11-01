ar_buah = ['Pepaya', 'Mangga', 'Pisang', 'Jambu', 'Belimbing']
ar_buah[2] = 'Apel'
del ar_buah[4]
print('Buah index ke-2:', ar_buah[2])
#print('Buah index ke-4:', ar_buah[4])

# tambah list
ar_buah.insert(0, 'Naga')
ar_buah.append('Jeruk')

# cetak all element list
for buah in ar_buah:
    print('Buah', buah)

# memotong list index 1 sampai 5
print('Memotong List Buah Index 1-5', ar_buah[1:5])
