""" 4. Kreirajte dvije varijable i pridijelite im proizvoljne vrijednosti, ispišite
rezultat operatora usporedbe (usporedba jednakosti, nejednakosti,
strogo veće, strogo manje, veće ili jednako, manje ili jednako).   """

a = 42
b = 56

jednakost = a == b 
print(jednakost)

nejednakost = a != b
print(nejednakost)

strogo_vece = a > b
print(strogo_vece)

strogo_manje = a < b 
print(strogo_manje)

vece_ili_jednako = a >= b
print(vece_ili_jednako) 

manje_ili_jednako = a <= b
print(manje_ili_jednako)

# jednostavniji oblik 

print(a < b)              # manje 
print(a > b)              # veće 
print(a <= b)             # manje ili jednjako
print(a >= b)             # veće ili jednako
print(a == b)             # jednako
print(a != b)             # različito 
