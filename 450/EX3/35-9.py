"""  Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni
niz znakova i varijablu n. Provjerite da li je vrijednost varijable n
manja od broja znakova u nizu. Ako je vrijednost varijable n veća
ispišite informaciju o grešci. Ispišite iz niza znakova svako n-to
slovo. Na primjer, ulazni niz je "ABCDEFGH", n je 2, tada je izlaz
"ACEG". """

rijec = input("Unesi neki text: ")
broj = input("Unesi neki broj: ")
fbroj = float(broj)

brojSlova = len(rijec)
fbrojslova = float(brojSlova)

if fbrojslova > fbroj :
    index = 0
    for slovo in rijec:
        if index % fbroj == 0 : 
            print (slovo, end="")
        index += 1
        
else: 
    print("Greška!")
        
    