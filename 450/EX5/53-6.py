""" Učitavajte realne brojeve koji predstavljaju dobiveni broj bodova na
ispitu. Za broj bodova [0,50>, ispišite "Nedovoljan!", za broj bodova
[50, 62.5> ispišite "Dovoljan!", za broj bodova [62.5, 75> ispišite
"Dobar!", za broj bodova [75, 87.5> ispišite "Vrlo dobar!", a za broj
bodova [87.5, 100] ispišite "Odličan!". U slučaju da je uneseni broj
izvan raspona brojeva <0, 100>, ispišite prikladnu poruku i prekinite
daljnje učitavanje broja bodova.
"""

while True:

    bodovi = input("Unesi ostvarene bodove na testu: ")
    bodovi = float(bodovi)


    
    if 0 < bodovi <= 50:
        print("Nedovoljan")
    elif 50 < bodovi <= 62.5 :
        print("Dovoljan!")
    elif 62.5 < bodovi <= 75 :
        print("Dobar")
    elif 75 < bodovi <= 87.5 : 
        print("Vrlo dobar!")
    elif 87.5 < bodovi <= 100:
        print("Odličan!!")
    else :
        print ("Uneseni broj bodova je neispravan!")
        break