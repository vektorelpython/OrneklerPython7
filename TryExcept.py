#ay = 12
#try:
#    yas = input("Yaşınızı Giriniz")
#    yas = int(yas)
#except ValueError:
#    yas = 20
#except:
#    print("Hata Oluştu")
#    
#print(yas*ay,"Ay Yaşamışsınız")


try:
    sayi1 = input("1. Sayıyı Giriniz")
    sayi2 = input("2. Sayıyı Giriniz")
    
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    if sayi2==0:
       raise Exception("Sıfır Rakamını Girdiniz")
    
    print(sayi1,"+",sayi2,"=",sayi1+sayi2)
    
except Exception as Hata:
    print("Hata Mesajı:",Hata)
else:
    try:
        print(sayi1,"/",sayi2,"=",sayi1/sayi2)
    except ZeroDivisionError:
        print("Sıfıra Bölünme Hatası")
    
    