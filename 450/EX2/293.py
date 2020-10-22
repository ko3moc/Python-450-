""" Napišite program koji će inicijalizirati u varijable a i b dva broja
proizvoljnih vrijednosti. U varijablu a pohranite zadnju znamenku
broja koji se nalazi u varijabli b, a u varijablu b pohranite zadnju
znamenku broja koja se nalazi u varijabli a. Ispišite sadržaj varijabli a
i b. """

a = 92
b = 44 

temp = a 
a = b 
b = temp 

a = a%10
b %= 10

print(a, b)