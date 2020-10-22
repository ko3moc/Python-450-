""" Korištenjem skraćenih aritmetičkih operatora rezultat dobiven iz
prethodnog zadatka multiplicirajte za 100 i ispišite dobivenu
vrijednost. """

a = 5
b = 10 
c = 15 
d = 21 

zbroj = a + b + c + d
clanova = 4 
artSredina = zbroj / clanova 
print(artSredina)

cjeliBroj = int(artSredina) # pretvaranje u int (cjelobrojni) tip podatka 
print(cjeliBroj)

kvadrat = cjeliBroj ** 2  # kvadriranje (power)

kvadrat *= 100      #skraceni zapis umnoška 
print(kvadrat)
