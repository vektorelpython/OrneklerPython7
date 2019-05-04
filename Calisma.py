basamak = {0:"",1:"bin",2:"milyon",3:"milyar"}
birler = {"0":"",
          "1":"bir",
          "2":"iki",
          "3":"üç",
          "4":"dört",
          "5":"beş",
          "6":"altı",
          "7":"yedi",
          "8":"sekiz",
          "9":"dokuz"}
onlar = {"0":"",
         "1":"on",
         "2":"yirmi",
         "3":"otuz",
         "4":"kırk",
         "5":"elli",
         "6":"altmış",
         "7":"yetmiş",
         "8":"seksen",
         "9":"doksan"
        }
sayi = input("okunmasını istediğiniz sayıyı giriniz")
#sayi = "9052741"
sayi = sayi.replace(".","").replace(",","")

while len(sayi)%3!=0:
    sayi = "0" + sayi
liste = []
for i in range(0,len(sayi),3):
    liste.append(sayi[i:i+3])

sonuc = ""

uzunluk = len(liste)-1
for item in liste:
    if item[0] != "0":
        sonuc += birler[item[0]] + " yüz "
    sonuc += onlar[item[1]] + " "
    sonuc += birler[item[2]] + " "
    sonuc += basamak[uzunluk] + " "
    uzunluk = uzunluk -1
print(sonuc)

