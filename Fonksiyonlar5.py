def topla(*args,islem):
    toplam = 0
    if islem == 1:
        for item in args:
            toplam += item
    else:
        for item in args:
            toplam *= item
    return toplam
        
print(topla(12,34,65,87,23,43,56,islem=1))
#
#degisken = input("Sayılar giriniz")
#print(topla(degisken))
#
#
#def armstrong(sayi):
#    toplam = 0
#    sayi = str(sayi)
#    basamak = len(sayi)
#    for i in sayi:
#        toplam += int(i)**basamak
#    if int(sayi) == toplam:
#        return True
#    else:
#        return False
#
#
#print(armstrong(371))