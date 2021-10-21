string = ""
bar = 1
# Looping baris
while bar <= 5:
    kol = bar
    # looping kolom
    while kol > 0:
        string += "*"
        kol = kol - 1
    string += "\n"
    bar = bar + 1
print(string)
