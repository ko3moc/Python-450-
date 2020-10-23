""" Modificirajte prethodno napisani program tako da se ukupna suma
brojeva iz datoteke brojevi.txt zapiše na kraj datoteke u
formatu: "<55>" """

with open("brojevi.txt", 'w') as f:
    for i in range(1,10):
        f.write(str(i) + "\n")
        
        
zbroj = 0
with open("brojevi.txt", "r") as f:
    for i in f.readlines():
        zbroj += int(i)

with open("brojevi.txt", "a") as f:
    f.write("<" + str(zbroj) + "+")
    f.close()
     
print(zbroj)