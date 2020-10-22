""" Napišite program koji će inicijalizirati u varijablu r neki proizvoljni
realni broj koji predstavlja radijus kugle. Ako je radijus ispravno
upisan (radijus ne može biti negativan), ispišite radijus i volumen
kugle, 𝑉 = 4/3 × 𝑟 3 × 𝜋. Inače, ispišite poruku da je vrijednost u
varijabli r neispravna. """


pi = 3.1515953
radijus = input ("Molimo unesite radijus kugle: ")
frad = float(radijus)

try :
    if frad > 0:
        volumen = (((3/4)*(frad**3)*pi))
        print("Radijus iznosi: ", frad, "centimentara!")
        print("Radijus kugle iznosi: ", volumen ,"kubičnih centimetara.")
    else: 
        print("Radijus ne može biti negativan broj!")
except :
    quit()

    

