""" Napišite program koji će inicijalizirati u varijable a i b dva broja
proizvoljnih vrijednosti. Ako je jedan od brojeva veći od 100, a onaj
drugi manji od 100, tada ispišite poruku "Jedna je veća, a druga je
manja od 100.". Također, ispišite prikladne poruke i za slučaj ako su
obje vrijednosti veće od 100 ili pak za slučaj ako su obje vrijednosti
manje od 100 te ako su obje vrijednosti jednake. """

var1 = input("Unesi neki broj: ")
fvar1 = float(var1)

var2 = input("Unesi neki broj: ")
fvar2 = float(var2)

if (fvar1 > 100 and fvar2 < 100) or (fvar2 > 100 and fvar1 < 100) :
    print("Jedna je vrijednost veća od 100 a druga mmanja od 100.")

elif fvar1 and fvar2 > 100 :
    print("Oba dva unesena broja su veća od 100.")

else:
    print("Unesene vrijednosti su manje od 100.")


