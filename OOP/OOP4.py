
# class HarfSayaci():
#     sinifniteligi = "Sınıf Metodu"
#     def __init__(self):
#         self.harf_seti = ""
#         self.sayac = 0
#         self.ifade = ""

#     def kelimesor(self):
#         return input("Kelime Giriniz")

#     @classmethod
#     def SinifMetodu(cls):
#         cls.sinifniteligi = "Değişiklik Yapıldı"
#         return cls.sinifniteligi

#     def kontrol(self,harf):
#         # print("gönderilen harf",harf)
#         return harf in self.harf_seti

#     @staticmethod
#     def piSayisi():
#         return 22/7

#     def arttir(self):
#         for harf in self.kelime:
#             if self.kontrol(harf):
#                 self.sayac += 1
#         return self.sayac

#     def ekranayazdir(self):
#         sayi = self.arttir()
#         print("""{} kelimesinin içinde 
#                  {} {} harf var""".format(self.kelime,sayi,self.ifade))

#     def calistir(self):
#         self.kelime = self.kelimesor()
#         self.ekranayazdir()


# class SesliHarf(HarfSayaci):
#     def __init__(self):
#         super().__init__()
#         self.harf_seti = "aeoöüuiı"
#         self.ifade = "Sesli"

# class SessizHarf(HarfSayaci):
#     def __init__(self):
#         super().__init__()
#         self.harf_seti = "szxwqrdfcvgtbnhyjmklpğçş"
#         self.ifade = "Sessiz"

# class TurkceKarakter(HarfSayaci):
#     def __init__(self):
#         super().__init__()
#         self.harf_seti = "çşğöüı"
#         self.ifade = "Türkçe"

# class GenelKontrol(HarfSayaci):
#     def __init__(self):
#         super().__init__()
#         self.kontrol1 = SesliHarf()
#         self.kontrol2 = SessizHarf()
#         self.kontrol3 = TurkceKarakter()
    
        
#     def ekranayazdir(self):
#         self.kontrol1.kelime = self.kelime
#         self.kontrol2.kelime = self.kelime
#         self.kontrol3.kelime = self.kelime
#         sesli,sessiz,turkce = self.kontrol1.arttir(),self.kontrol2.arttir(),self.kontrol3.arttir()

#         print("""{} kelimesinin içinde 
#                  {} sesli {} sessiz {} türkçe harf var""".format(self.kelime,sesli,sessiz,turkce))


# if __name__ == "__main__":
#     sayac = GenelKontrol()
#     sayac.calistir()



# var1 = HarfSayaci()
# var2 = HarfSayaci()
# # var1.sinifniteligi = "abdc"
# print("var1",var1.sinifniteligi)
# print("var2",var2.sinifniteligi)
# HarfSayaci.SinifMetodu()
# print("var1",var1.sinifniteligi)
# print("var2",var2.sinifniteligi)



class Sınıf():
    sinif_niteligi = 0
    __gizli = 0
    def __init__(self,param1):
        self.param1 = param1
        self.ornek_nitelik =0
    def OrnekMetod(self):
        self.__gizli_ = 1
        return self.__gizli_

    @classmethod
    def sinifMetod(cls):
        cls.sinif_niteligi = 4
        return cls.sinif_niteligi

    @property
    def version(self):
        return 1.0

    
    

# a = Sınıf()
# a.OrnekMetod
# print(Sınıf.__gizli)



s = Sınıf("aa")
print(s.version)