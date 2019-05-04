print("*"*30)
print("1 Toplam","2 Çıkarma",sep="\n")
print("*"*30)
giris = input("Yapmak istediğiniz işlemi seçiniz")
sayi1 = int(input("1. Sayıyı Giriniz"))
sayi2 = int(input("2. Sayıyı Giriniz"))
if giris=="1":
    sonuc= sayi1+sayi2
    islem = "+"
elif giris == "2":
    sonuc= sayi1-sayi2
    islem = "-"
else:
    sonuc = "Hatalı Giriş Yaptınız"

print("{0} {2} {1} ={3}".format(sayi1,sayi2,islem,sonuc))

