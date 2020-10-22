""" Napišite program koji će inicijalizirati u varijable a i b dva broja
proizvoljnih vrijednosti. Ako je vrijednost varijable a bar za 50 veća
od vrijednosti varijable b, a uz to je vrijednost varijable b parna, tada
ispišite poruku "Uvjeti su zadovoljeni.", u suprotnom ispišite poruku
"Uvjeti nisu zadovoljeni. """

a = input("Unesi neki broj: ")
fa = float(a)
b = input("Unesi neki broj: ")
fb = float(b)

if (fa > fb) and ( fb % 2 == 0 ) and (fa - fb >= 50):
    print("Uvjeti su zadovoljeni.")
    
else: 
    print("Uvjeti nisu zadovoljeni.")
    
#isti se zadatak moze i napraviti na sljedeci nacin 

if fa > ( fb+50 ) and (fb % 2 == 0) : 
    print("Uvjeti su zadovoljeni.")
else: 
    print("Uvjeti nisu zadovoljeni.")
    
    
    
