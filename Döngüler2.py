
#liste = [1,1.1,"deneme",(1,2),{"a":1}]
#
#for item in liste:
#    if str(type(item)) == "<class 'tuple'>":
#        print(item)
def AsalListe(N):
    liste = []  
    x=2
    while x<=N:
        i = 2
        while i*i<=x:
            if x%i ==0:
                break
            i+=1
        else:
            liste.append(x)
        x+=1
    return liste
N = int(input("Bir Pozitif Tamsayı Giriniz"))
x= int(input("Alt Sınır"))
adim = x
i = 0
liste = []
while i < N:
    for item in AsalListe(adim):
        if item > x:
            while not item in liste:
                liste.append(item)
                i+=1
    else:
        adim+=1
print(liste)            




#
#
#sayac = int(input("Döngü ne kadar dönecek"))
#
#for i in range(1,sayac):
#    for j in range(2,i):
#        if i%j ==0:
#            print(i,"Sayı Asal Değil")
#            break
#    else:
#        print(i,"Sayı Asal")
    
        