import random
kolonSayi = int(input("Kaç kolon istiyorsun"))
buyukListe = []

for j in range(0,kolonSayi):
    liste = []
    i = 0
    while i < 6:
        sayi = random.randint(1,50)
        while not sayi in liste:
            liste.append(sayi)
            i+=1
#    for i in range(0,6):
#        sayi = random.randint(1,50)
#        while not sayi in liste:
#            liste.append(sayi)
    liste.sort()
    buyukListe.append(liste)
print(*buyukListe,sep="\n")

    

