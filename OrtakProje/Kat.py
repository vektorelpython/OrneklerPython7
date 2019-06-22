class KatHarita:
    en_sayi = 10
    boy_sayi = 10
    magazametre = 50
    yolmetre = 50
    kat_sayisi = []
    def __init__(self,magazasayisi=0,adi=""):
        self.magazasayi = magazasayisi
        self.adi = adi
        self.kat_sayisi.append(adi)
    
    def magazasayiYazdir(self):
        print(self.magazasayi)

    def katisimListesi(self):
        print(*self.kat_sayisi,sep="\n")
        
    def Nasil(self):
        print(__name__)

    def __str__(self):
       return self.adi

