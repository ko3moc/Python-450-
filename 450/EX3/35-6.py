""" Napišite program koji će inicijalizirati u varijable a1, a2, b1, b2 četiri
cijela broja proizvoljnih vrijednosti. Prilikom inicijalizacije vrijednosti
zadovoljiti sljedeće uvjete: a1 < a2 i b1 < b2. Te vrijednosti
predstavljaju granice dvaju intervala [a1, a2] – prvi interval i [b1, b2]
– drugi interval. Provjerite je li početna granica prvog intervala manja
ili jednaka početnoj granici drugog intervala (a1 ≤ b1) te je li završna
granica prvog intervala veća ili jednaka završnoj granici drugog
intervala (b2 ≤ a2). Ako su ovi uvjeti zadovoljeni, ispišite poruku
"Zadovoljava.", u suprotnom ispišite poruku "Ne zadovoljava.  """

ax = input("Unesi neki broj")
a1 = int(ax)
ay = input("Unesi neki broj")
a2 = int(ay)
bx = input("Unesi neki broj")
b1 = int(bx)
by = input("Unesi neki broj")
b2 = int(by)

if (a1 < b1) and (a2 >= b2):
    print("Zadovoljava.")
else:
    print("Ne zadovoljava.")

