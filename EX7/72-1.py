""" 1. Napišite program koji će kreirati praznu tekstualnu datoteku (ako
datoteka identičnog imena već postoji od prije, tada ju je potrebno
pregaziti s praznom datotekom) te je u tako kreiranu datoteku
potrebno ispisati sve parne brojeve do 20. Parni brojevi neka
međusobno budu odvojeni razmakom.  """
 
with open('parni_brojevi.txt', 'a+' ) as f:
    for i in range(0, 20):
        if i % 2 == 0:
            f.write(str(i) + " ")
 
 


   
     
        
