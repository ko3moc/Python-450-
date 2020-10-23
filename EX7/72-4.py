"""  Pomoću programa Notepad kreirajte datoteku i u 10 redaka te
datoteke napišite po jedan proizvoljan broj. Napišite program koji će
pročitati tu datoteku te sve parne brojeve iz nje upisati u novu
datoteku. Također, izračunajte sumu svih neparnih brojeva te ih
zapišite u treću datoteku. """

ulaz = open("ulazni.txt", "r")
izlazna_datotekaP = open("izlaz_parni.txt", "w")
izlaz_zbrojNepar = open("izlaz_zbrojNepar.txt", "w")

zbrojBrojeva = 0
for line in ulaz.readlines():
    line = float(line)
    if line % 2 == 0 :
        izlazna_datotekaP.write(str(line) + "\n")
    else :
        zbrojBrojeva += line
        
        
izlaz_zbrojNepar.write("Zbroj neparnih brojeva iznosi: " + str(zbrojBrojeva))

ulaz.close()
izlazna_datotekaP.close
izlaz_zbrojNepar.close

print("Postupak završen, pregledaj nove datoteke!")