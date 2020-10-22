""" Napišite funkciju koja prima 2 parametara. Rezultat izračuna funkcije
ovog puta se ne ispisuje izravno u funkciji već se kao povratni
parametar šalje u pozivajući dio programa. Funkcija mora izračunati
rezultat matematičke formule:
(a*a) + (b*b)
Rezultat funkcije spremite u varijablu koja se nalazi u dijelu
programskoga kôda u kojem se funkcija poziva te ispišite povratnu
vrijednost funkcije koja je spremljena u varijablu proizvoljnog imena. """

var1 = 0 

def zadatak(a,b):
    return (a*a) + (b*b)

var1 = zadatak(5,6)
print(var1)

var1 = zadatak(10,20)
print(var1)

