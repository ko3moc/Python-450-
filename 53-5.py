"""  Napišite program koji s tipkovnice učitava tri cijela broja: redni broj
dana u mjesecu, redni broj mjeseca u godini i redni broj godine.
Prekontrolirajte jesu li učitane vrijednosti ispravne (ispravne
vrijednosti su: dan - [1, 31], mjesec - [1, 12], godina - [0, 2020]). Za
ulazne podatke 19, 2, 2017, ispišite datum u sljedećem formatu:
19. veljače, 2017.  """

print("Unesi brojčane vrijednosti datuma u formatu DD-MM-YY")

dan = input("Dan: ")
mjesec = input("Mjesec: ")
godina = input("Godina: ")

dan = int(dan)
mjesec = int(mjesec)
godina = int(godina)

if dan < 1 or dan > 31 or mjesec < 1 or mjesec > 12 or godina < 1900 or godina > 2018:
    print("Greška")
else:
    print(dan, ". ", sep="", end="")
    if mjesec == 1:
        print("siječnja, ", end="")
    elif mjesec == 2:
        print("veljače, ", end="")
    elif mjesec == 3:
        print("ožujka, ", end="")
    elif mjesec == 4:
        print("travnja, ", end="")
    elif mjesec == 5:
        print("svibnja, ", end="")
    elif mjesec == 6:
        print("lipnja, ", end="")
    elif mjesec == 7:
        print("srpnja, ", end="")
    elif mjesec == 8:
        print("kolovoza, ", end="")
    elif mjesec == 9:
        print("rujna, ", end="")
    elif mjesec == 10:
        print("listopada, ", end="")
    elif mjesec == 11:
        print("studenog, ", end="")
    elif mjesec == 12:
        print("prosinca, ", end="")
print(godina, ".", sep="")