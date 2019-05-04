import os
adres = r"D:\İbrahim EDİZ\Ornekler\defter.csv"
if os.path.exists(adres):
    dosya = open(adres,"r+")
else:
    dosya = open(adres,"w")
while True:    
    print("""
          *************
          1-Yeni Kayıt
          2-Güncelleme
          3-Silme
          4-Listeleme
          5-Bulma
          6-Çıkış
          *************
          """)
    islem=int(input("Yapmak istediğiniz işlemi seçiniz:"))
    if islem  == 1:
        adi = input("Adını Giriniz:")
        soyadi = input("Soyadı Giriniz:")
        telefon  = input("Telefon Giriniz:")
        metin = "{};{};{}\n".format(adi,soyadi,telefon)
        dosya.seek(0)
        liste = dosya.readlines()
        liste.append(metin)
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
    elif islem == 2:
    #    güncelleme
        dosya.seek(0)
        liste = dosya.readlines()
        for item in liste:
            print(liste.index(item)+1,item)
        kayit = int(input("Düzenlemek istediğiniz kaydın numarasını giriniz"))
        metin = "{};{};{}\n".format(input("Adını Giriniz:"),input("Soyadı Giriniz:"),input("Telefon Giriniz:"))
        liste[kayit-1] = metin
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
    elif islem == 3:
    #    Silme
        dosya.seek(0)
        liste = dosya.readlines()
        for item in liste:
            print(liste.index(item)+1,item)
        kayit = int(input("Silmek istediğiniz kaydın numarasını giriniz"))
        liste.pop(kayit-1)
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
    elif islem == 4:
    #    Listeleme
        dosya.seek(0)
        liste = dosya.readlines()
        for item in liste:
            print(liste.index(item)+1,item)
    elif islem == 6:
        break
dosya.close()
    
    
    
    
    
    
    
    
    