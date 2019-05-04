import random

sayi = random.randint(0,100)
print(sayi)
for i in range(10,1,-1):
    tahmin = int(input("Tahmin Giriniz"))
    if sayi > tahmin:
        print("yukarı","kalan hak:",i-1)
    elif sayi<tahmin:
        print("aşağı","kalan hak:",i-1)
    else:
        print("Tebrikler",10-(i-1)," tahminde bildin")
        break
else:
    print("Kaybettin")