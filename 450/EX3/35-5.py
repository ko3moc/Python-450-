""" Napišite program koji će inicijalizirati u varijable a, b, c, d, e pet
realnih brojeva proizvoljnih vrijednosti. Ako su bar tri od pet brojeva
veći od 100, tada ispišite poruku "Zadovoljava.", u suprotnom
program neka ispiše poruku "Ne zadovoljava.". """

a = input("Unesi neki broj: ")
fa = float(a)
b = input("Unesi neki broj: ")
fb = float(b)
c = input("Unesi neki broj: ")
fc = float(c)
d = input("Unesi neki broj: ")
fd = float(d)
e = input("Unesi neki broj: ")
fe = float(e)

counter = 0

if fa > 100:
    counter += 1
if fb > 100:
    counter += 1
if fc > 100:
    counter += 1
if fd > 100:
    counter += 1
if fe > 100: 
    counter += 1

if counter >= 3 : 
    print ("Zadovoljava")
else :
    print("Ne zadovoljava.") 

