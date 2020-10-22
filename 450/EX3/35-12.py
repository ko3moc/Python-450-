"""  ** Napišite program koji će inicijalizirati varijablu n na proizvoljnu
cjelobrojnu vrijednost. Vrijednost varijable n neka predstavlja red
matrice. Ispisati matricu veličine n redaka i n stupaca. Vrijednost 1
neka se nalazi na glavnoj dijagonali, a vrijednost 0 na svim ostalim
mjestima. U nastavku slijedi primjer za n=5:
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
Napomena: za ispis vrijednost, tako da se nakon ispisa vrijednosti
dane print() funkciji ne ispiše novi redak koristiti sljedeću
sintaksu: print(vrijednost, end='') 

** zadatak: ako se ne želi nakon svakog poziva funkcije print() ispisati i
novi redak, to je moguće postići sa sljedećom sintaksom:
print(vrijednost, end='')
Ako se želi ispisati samo novi redak bez ikakve vrijednosti to je moguće 
postići sa sljedećom sintaksom: print()
 
"""

redMatrice = 5
vrijednost = 1 

for x in range(0, redMatrice):         #postavlja vrijednost redka 
    for y in range (0, redMatrice) :    #postavlja vrijednost stupca 
        if x == y :
            print ("1", end = '')
        else :
            print ("0", end = '')
            
    print()                           