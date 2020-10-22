"""  Napišite program koji ispisuje koliko ima prostih brojeva između
dva proizvoljna broja.  """

brojac = 0
vrijednosta = input("Unesi vrijednost: ")
a = int(vrijednosta)
vrijednostb = input("Unesi vrijednost: ")
b = int(vrijednostb)

for n in range(a, b+1):
    jePrim = True
    for x in range(2, n):
        if n % x == 0:
            jePrim = False
            break
    
    if jePrim == True:
        brojac += 1
        
        
print(brojac)
    