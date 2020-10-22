""" ** Napišite program koji će inicijalizirati u varijable n i m dva cijela
broja proizvoljnih vrijednosti. Provjerite zadovoljavaju li inicijalizirane
vrijednosti uvjet: 0 ≤ n ≤ m. Ako uvjet nije zadovoljen, tada
ispišite poruku: "Nedozvoljene vrijednosti!". Ako je uvjet zadovoljen
izračunajte i ispišite binomni koeficijent "m povrh n", pri čemu
koristite sljedeći izraz:(𝑚 𝑛) =  𝑚! / 𝑛! ∗ (𝑚 − 𝑛)!
    (  Primjer: 5! se izračunava na način 5*4*3*2  )
(Napomena: Implementirajte funkciju fakt(), tako implementirana
funkcija izračunava faktorijele, na primjer, za poziv funkcije
fakt(5), povratna vrijednost je: 120. Funkcija se mora pozivati iz
glavnog programa za sve 3 vrijednosti: m!, n!, (m-n)!) """ 

n = 5
m = 10
def fakt(x):
    umnozak = 1
    
    while x > 1:
        umnozak *= x
        x -= 1

    return umnozak

if 0 <= n and n <= m:
    print(fakt(m) / (fakt(n) * fakt(m-n)))
else:
    print("Greška.")
