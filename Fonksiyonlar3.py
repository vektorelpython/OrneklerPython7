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
    
while True:
    fonk = None
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
    print("*"*45)
    islem = int(input("Yapmak İstediğiniz İşlem"))
    if islem:
        if islem== 7:
            print("İyi Günler Dileriz")
            break
        else:
            if islem == 1:
                fonk = Topla
            elif islem == 2:
                fonk = Cıkar
            elif islem == 3:
                fonk = Carp
            elif islem == 4:
                fonk = Bol
            elif islem == 5:
                fonk = Kuvvet
            elif islem == 6:
                fonk = Mod
            Islem(fonk,int(input("1. Sayı")),int(input("2. Sayı")))

       
        
        
        
        
        
        
        
        
        
        