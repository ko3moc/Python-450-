""" * Napišite program koji će izračunati sumu sljedećih članova niza:
1/1 − 1/2 + 1/3 − 1/4 + 1/5 − 1/6+ ⋯ + 1/997 − 1/998 + 1/999 − 1/1000"""

vrijednost = 0

for x in range(1, 1001):
    if x % 2 == 0:
        vrijednost -= 1 / x
    else:
        vrijednost += 1 / x
    
print(vrijednost)