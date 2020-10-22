"""  Odaberite proizvoljno koordinatu T=(x,y), vrijednosti varijabli x
(stupac) i y (redak) neka budu manje od 10. Program neka ispiše
polje 10x10 čiji su svi elementi vrijednosti "-" osim koordinate T čija
je vrijednost "X". 
"""
n = 10
t1 = 1 
t2 = 5 

for x in range(0, n):         #postavlja vrijednost redka 
    for y in range (0, n) :    #postavlja vrijednost stupca 
        if  x == t1 and y == t2 :
            print (" X ", end = '')
        else :
            print (" - ", end = '')
            
    print() 
 