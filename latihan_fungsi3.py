def person(nama="Firda", pekerjaan="Pelajar", hobby="Memasak"):
    print("Nama\t\t: %s"
          "\nPekerjaan\t: %s"
          "\nHobby\t\t: %s"
          % (nama, pekerjaan, hobby))
    print("---------------------------")


# panggil fungsi
person()
person('Fawwaz', 'Santri', 'Menghafal Al-qur an')
person('Inaya', hobby='Membaca')
person(pekerjaan="Mahasiswa")
