""" Napišite program koji će inicijalizirati u varijablu proizvoljnog imena,
proizvoljnu vrijednost temperature izražene u stupnjevima
Celzijevim. Na ekran ispisati vrijednost temperature u farenhajtima.
Formula: ( 𝑥 × 9/5) + 32 , x je vrijednost izražena u stupnjevima
Celzijevim. """


celz = input("Unesi temperaturu u Celzijusima: ")
temp = float(celz)           #pretvaranje unesene vrijednosti u numerički tip podatka
fahrenhait = (((temp)*(9/5))+32)
print (fahrenhait)


#jednostavniji oblik zapisa 

celz = 24 
fahr = (celz * 9/4) + 32
print(fahr)