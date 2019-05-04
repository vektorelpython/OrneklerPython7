def Topla(a,b):
    return a+b
def Carp(a,b):
    return a*b
def Cıkar(a,b):
    return a-b
def Bol(a,b):
    return a/b
def Kuvvet(a,b):
    return a**b
def Mod(a,b):
    return a%b
def Islem(fonk,a,b):
    print(fonk(a,b))
def Islem(fonk)
while True:
    print("*"*15,"Hesap Makinesi","*"*15)
    print("""
          1- Toplama
          2- Çıkarma
          3- Çarpma
          4- Bölme
          5- KuvvetAlma
          6- ModAlma
          7- Çıkış
          """)
    print("*"*30)
    sonuc = 0
    islem = int(input("Yapmak İstediğiniz İşlem"))
    if islem== 7:
        print("İyi Günler Dileriz")
        break
    else:
        sayi1 = int(input("1. Sayıyı Giriniz"))
        sayi2 = int(input("2. Sayıyı Giriniz"))
    if islem == 1:
        sonuc = Topla(sayi1,sayi2)
        
        
        
    
