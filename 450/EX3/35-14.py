"""  ** Napišite program koji ispisuje sumu znamenaka proizvoljnog
broja. Na primjer, suma broja 159 iznosi 15.
Napomena: 159%10 = 9, 159 // 10 = 15. """ 

broj = input ("Unesi neki broj: ")
ibroj = int(broj)

suma = 0 

while ibroj > 0 :
    suma += (ibroj % 10)
    ibroj //= 10 
    
print(suma)
