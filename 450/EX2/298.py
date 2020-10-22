""" . Iskoristite prethodni zadatak te dobiveni rezultat pretvorite u cijeli broj
i tu vrijednost spremite u varijablu. Nad cjelobrojnom aritmetičkom
sredinom koju ste prethodno spremili u varijablu napravite
kvadriranje i ispišite dobiveni rezultat. """

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

kvadrat = cjeliBroj ** 2  # kwadriranje (power)
