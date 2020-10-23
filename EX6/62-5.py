"""  U službenoj Python 3 dokumentaciji pronađite ime funkcije za
potenciranje (zamjena za aritmetički operator **). S tipkovnice
učitajte cjelobrojne vrijednosti i spremite ih u varijable a i b. Nije
potrebno provjeravati ispravnost učitanih brojeva. Na temelju tih
vrijednosti izračunajte kvadrat zbroja (𝑎 + 𝑏)**2. Formula za kvadrat
zbroja je (𝑎 + 𝑏)**2 = 𝑎**2 + 2𝑎𝑏 + 𝑏**2. Funkcije koje ćete koristiti 
u ovom zadatku uključite u program """ 

import math

a = input("Unesi neki broj: ")
a = float(a)
b = input("Unesi neki broj: ")
b = float(b)

rezultat = pow(a,2) + 2*a*b + pow(b,2)
print(rezultat)





