""" Napišite funkciju mnozenje() koja može primiti 2 vrijednosti, od
kojih je druga vrijednost unaprijed zadana, sami odredite broj koji
ćete pridružiti unaprijed zadanoj vrijednosti. Funkcija mora izračunati
i ispisati rezultat množenja.
U glavnom programu pozovite funkciju dva puta. Kod prvog poziva
funkcije, kao argumente funkcije navedite dvije vrijednosti (vrijednost
drugog argumenta neka bude drugačija od unaprijed zadane
vrijednosti). Drugi put funkciju pozovite samo jednim argumentom """

def mnozenje(a,b=0):
    print(a*b)
    
mnozenje(1)

mnozenje(1,5)
