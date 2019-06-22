try:
    toplam = 0
    dosya = open("Kitap1.csv","r+")
    dosya.seek(0)
    liste = dosya.readlines()
    for i in liste:
#        print(i)
        toplam +=  int(i.split(";")[0])
except Exception as hata:
    print("Kalınan Satır:",liste.index(i))
    print("Hata Mesajı:",hata)
finally:
    dosya.close()
    




