#tekSayiListe = [i for i in range(1,100,2)]
#print(tekSayiListe)
#ciftSayiListe = [j for i in range(0,100,5) for j in range(0,i)]
#print(ciftSayiListe)

#i = 0
#while i != -99:
#    i = int(input("sayı gir"))
#    if i == -99:
#        break
#    if i < 100 and i > 0:
#        print(i)
#        continue
#    
import random
#kolonSayi = int(input("Kaç kolon istiyorsun"))
#buyukListe = []
#
#for j in range(0,kolonSayi):
#    liste = []
#    i = 0
#    while i < 6:
#        sayi = random.randint(1,50)
#        while not sayi in liste:
#            liste.append(sayi)
#            i+=1
##    for i in range(0,6):
##        sayi = random.randint(1,50)
##        while not sayi in liste:
##            liste.append(sayi)
#    liste.sort()
#    buyukListe.append(liste)
#    
#print(*buyukListe,sep="\n")
#for a,b,c,d,e,f in buyukListe:
#    print(a,b,c,d,e,f)
#    
    
N = int(input("Bir Pozitif Tamsayı Giriniz"))
x=2    
while x<=N:
    i = 2
    while i*i<=x:
        if x%i ==0:
            break
        i+=1
    else:
        print(x)
    x+=1

    
    
