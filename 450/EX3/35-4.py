""" Napišite program koji će inicijalizirati u varijable a i b dva realna
broja proizvoljnih vrijednosti. Program neka ispiše poruku
"Zadovoljava." ako se barem jedan od brojeva nalazi u intervalu [5,
20], u suprotnom program neka ispiše poruku "Ne zadovoljava. """ 

a = input("Unesi neki broj: ")
fa = float(a)
b = input("Unesi neki broj: ")
fb = float(b)

if (5 < fa <20) or (5 < fb <20) :
    print("Zadovoljava.")
else : 
    print("Ne zadovoljava.")

