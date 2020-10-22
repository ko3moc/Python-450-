""" Ispišite sve parne brojeve između 1 i 1000 koju su istovremeno
djeljivi i s 5 i s 13. """

for x in range(1, 1001):
    if (x % 2 == 0 ) and (x % 5 == 0) and (x % 13 == 0):
        print(x)
    else: 
        continue

    