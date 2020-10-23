"""  U službenoj Python 3 dokumentaciji pronađite ime funkcije koja
služi za zaokruživanje na prvi viši cijeli broj i na prvi niži cijeli broj.
Broj nad kojim se želi napraviti zaokruživanje učitajte s tipkovnice.
Tako učitani broj neka bude broj realne vrijednosti. Na primjer, za
učitani broj 5.587, ispis na ekran mora biti sadržaja: "5, 6". U ovom
zadatku najavite korištenje funkcija, no nemojte ih uključiti. """

""" ***math.floor(x) - vraca int broj umanjen za vrijednost nakon decimale 
Return the floor of x, the largest integer less than or equal to x. 
If x is not a float, delegates to x.__floor__(), which should return 
an Integral value. 
     
    ***math.ceil(x) - vraca broj zaokruzenu na vrijednost INT BROJA nakon decimale
Return the ceiling of x, the smallest integer greater than or equal to x. 
If x is not a float, delegates to x.__ceil__(), which should return an 
Integral value.

"""


import math 

broj = input("Unesi broj: ")
broj = float(broj)

f = math.floor(broj)
c = math.ceil(broj)

print(f, c, sep=', ')

