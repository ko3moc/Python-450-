"""Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni niz
znakova. Ispišite koliko velikih slova se nalazi u nizu. Ako je neko od
unesenih slova u nizu jednako slovu "A", brojanje velikih slova je
potrebno prekinuti i ispisati informaciju da je veliko slovo "A"
pronađeno. """

count = 0
veliko_Slovo_A = 0 
unos = input("Unesi neki text: ")
#print(unos)

for slovo in unos:
    if slovo >= "A" and slovo <= "Z" :
        count += 1
    
    if slovo == "A":
        veliko_Slovo_A += 1
        print("Veliko slovo A pronađeno je:", veliko_Slovo_A, "puta u textu.")
        quit() 