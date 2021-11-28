def infoSuhu():
    lokasi = input('Lokasi\t: ')
    suhu = int(input('Suhu\t: '))

    def status():
        if(suhu <= 0):
            kondisi = 'Beku'
        elif(suhu > 0 and suhu <= 16):
            kondisi = 'Dingin'
        elif(suhu > 16 and suhu <= 23):
            kondisi = 'Sejuk'
        elif(suhu > 23 and suhu <= 29):
            kondisi = 'Biasa'
        else:
            kondisi = 'Panas'

        return kondisi

    print('Lokasi di %s dengan suhu %i kondisinya %s' %
          (lokasi, suhu, status()))


# panggil fungsi
infoSuhu()
