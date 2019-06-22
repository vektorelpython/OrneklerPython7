# class Gozluk():
#     Malzeme = ""
#     DereceSag = ""
#     DereceSol = ""

#     def Temizlenme():
#         pass
    
#     def Takmak():
#         pass

# benimgoz = Gozluk()



sesli_harf = "aeıioöuü"
sayac = 0

kelime = input("Kelime Giriniz")
for harf in kelime:
    if harf in sesli_harf:
        sayac += 1

print('{} kelimesinin içinde {} sesli harf var'.format(kelime,sayac))