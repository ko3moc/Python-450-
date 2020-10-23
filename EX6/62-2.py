""" Pronađite na Internetu u službenoj Python 3 dokumentaciji kako se
zove funkcija koja se nalazi u modulu math koja se koristi za
korjenovanje. Preko tipkovnice unesite broj i ispišite njegov korijen.
Službenu Python 3 dokumentaciju možete pronaći na URL-u:
https://docs.python.org/3/library/math.html """

""" math.isqrt(n)
     Return the integer square root of the nonnegative integer n. This is 
the floor of the exact square root of n, or equivalently the greatest 
integer a such that a² ≤ n.
     For some applications, it may be more convenient to have the least 
integer a such that n ≤ a², or in other words the ceiling of the exact 
square root of n. For positive n, this can be computed using a = 1 + isqrt(n - 1) """

import math

broj = input("Unesi neki broj: ")
broj = int(broj)
if broj > 0 : 
    try:
        print(math.isqrt(broj))
    except:
        print("Vrijednost nije valjana")
else :
    quit()
        