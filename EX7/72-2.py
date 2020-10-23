""" Modificirajte prethodni zadatak tako da se kreira datoteka naziva
brojevi.txt. U tako kreiranu datoteku spremite sve brojeve od 1
do 10. Svaki broj neka bude u zasebnoj liniji. Nakon što je datoteka
kreirana, pročitajte iz nje sve brojeve te napravite sumu pročitanih
brojeva, a taj rezultat ispišite na zaslon.  """

with open("brojevi.txt", 'w') as f:
    for i in range(1,10):
        f.write(str(i) + "\n")
        
        
zbroj = 0
with open("brojevi.txt", "r") as f:
    for i in f.readlines():
        zbroj += int(i)

print(zbroj)

        