""" Pomoću operatora usporedbe detektirajte je li broj koji ste dobili u
prethodnom zadatku manji od 500. Ispišite rezultat usporedbe (ispis
će biti vrijednosti "True" ili "False"). """

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

print (500 > kvadrat) # usporedba veličine kao rezultat ispisuje Boolean vrijednost, True ili False 