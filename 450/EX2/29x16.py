""" . * U varijablu upišite neki proizvoljni niz znakova. Nad varijablom
pozovite odgovarajuću funkciju koja će vratiti duljinu upisanoga niza
znakova te rezultat spremite u varijablu. Na temelju duljine niza
ispišite sve znakove do polovice niza. Primjer: ako imamo niz od 14
znakova (abcdefghijklmn), potrebno je ispisati 1., 2., 3., 4., 5., 6. i 7.
znak (abcdefg). """

var1 = "ovo Je Velika Hrpa Nekih Slova I br0jev4"

print(var1)
print(len(var1))
x = (len(var1))/2
print(var1[:int(x)]) #int() funkcija se koristi jer index mora biti cijeli broj 

