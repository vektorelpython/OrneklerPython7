# sesli_harf = "aeıioöuü"
# sayac = 0

# kelime = input("Kelime Giriniz")
# for harf in kelime:
#     if harf in sesli_harf:
#         sayac += 1

# print('{} kelimesinin içinde {} sesli harf var'.format(kelime,sayac))

# 1.Aşama
# sesli_harf = "aeıioöuü"
# sayac = 0
# kelime = input("Kelime Giriniz")
# def seslidir(harf):
#     print("gönderilen harf",harf)
#     return harf in sesli_harf

# def arttir(sayac):
#     for harf in kelime:
#         if seslidir(harf):
#             sayac += 1
#     return sayac

# print('{} kelimesinin içinde {} sesli harf var'.format(kelime,arttir(sayac)))


## 2. Aşama

# sesli_harf = "aeıioöuü"
# sayac = 0
# def kelimesor():
#     return input("Kelime Giriniz")


# def seslidir(harf):
#     # print("gönderilen harf",harf)
#     return harf in sesli_harf

# def arttir(sayac,kelime):
#     for harf in kelime:
#         if seslidir(harf):
#             sayac += 1
#     return sayac
# def ekranayazdir(kelime):
#     print('{} kelimesinin içinde {} sesli harf var'.format(kelime,arttir(sayac,kelime)))

# def calistir():
#     kelime = kelimesor()
#     ekranayazdir(kelime)



## 3. Aşama



# class HarfSayaci():
#     def __init__(self):
#         self.sesli_harf = "aeıioöuü"
#         self.sessiz_harf = "bmnvcxzsqwdrftgyhjklpğşç"
#         self.sesli_sayac = 0
#         self.sessiz_sayac = 0

#     def kelimesor(self):
#         return input("Kelime Giriniz")


#     def seslidir(self,harf):
#         # print("gönderilen harf",harf)
#         return harf in self.sesli_harf

#     def sessizdir(self,harf):
#         return harf in self.sessiz_harf

#     def arttir(self):
#         for harf in self.kelime:
#             if self.seslidir(harf):
#                 self.sesli_sayac += 1
#             if self.sessizdir(harf):
#                 self.sessiz_sayac += 1
#         return self.sesli_sayac,self.sessiz_sayac

#     def ekranayazdir(self):
#         sesli,sessiz = self.arttir()
#         print("""{} kelimesinin içinde 
#                  {} sesli harf
#                  {} sessiz harf var""".format(self.kelime,sesli,sessiz))

#     def calistir(self):
#         self.kelime = self.kelimesor()
#         self.ekranayazdir()

# if __name__ == "__main__":
#     sayac = HarfSayaci()
#     sayac.calistir()

## 4. Aşama

class HarfSayaci():
    def __init__(self):
        self.harf_seti = ""
        self.sayac = 0
        self.ifade = ""

    def kelimesor(self):
        return input("Kelime Giriniz")


    def kontrol(self,harf):
        # print("gönderilen harf",harf)
        return harf in self.harf_seti

    def arttir(self):
        for harf in self.kelime:
            if self.kontrol(harf):
                self.sayac += 1
        return self.sayac

    def ekranayazdir(self):
        sayi = self.arttir()
        print("""{} kelimesinin içinde 
                 {} {} harf var""".format(self.kelime,sayi,self.ifade))

    def calistir(self):
        self.kelime = self.kelimesor()
        self.ekranayazdir()


class SesliHarf(HarfSayaci):
    def __init__(self):
        super().__init__()
        self.harf_seti = "aeoöüuiı"
        self.ifade = "Sesli"

class SessizHarf(HarfSayaci):
    def __init__(self):
        super().__init__()
        self.harf_seti = "szxwqrdfcvgtbnhyjmklpğçş"
        self.ifade = "Sessiz"

class TurkceKarakter(HarfSayaci):
    def __init__(self):
        super().__init__()
        self.harf_seti = "çşğöüı"
        self.ifade = "Türkçe"

class GenelKontrol(HarfSayaci):
    def __init__(self):
        super().__init__()
        self.kontrol1 = SesliHarf()
        self.kontrol2 = SessizHarf()
        self.kontrol3 = TurkceKarakter()
    
        
    def ekranayazdir(self):
        self.kontrol1.kelime = self.kelime
        self.kontrol2.kelime = self.kelime
        self.kontrol3.kelime = self.kelime
        sesli,sessiz,turkce = self.kontrol1.arttir(),self.kontrol2.arttir(),self.kontrol3.arttir()

        print("""{} kelimesinin içinde 
                 {} sesli {} sessiz {} türkçe harf var""".format(self.kelime,sesli,sessiz,turkce))


if __name__ == "__main__":
    sayac = GenelKontrol()
    sayac.calistir()
