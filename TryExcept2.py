def SayiKontrol(metin):
    for i in metin:
        if i.isnumeric():
            return False
    return True

def UzunlukKontrol(metin):
    adim = "UzFonk1A"
    if len(metin) < 8:
        return True
    else:
        return False
    
def BuyukHarfKontrol(metin):
    for i in metin:
        if i.isalpha():
            if i.isupper():
                return False
    return True

def SifreKontrol(sifre):
        try:
            adim = "A1_1"
            password = sifre
            adim = "A2"
            if SayiKontrol(password):
                raise Exception("Şifrenizde Nümerik değer bulunmamaktadır")
                adim="ifA21"
            if UzunlukKontrol(password):
                raise Exception("Şifreniz en az 8 karakter uzunluğunda olmalıdır")
            if BuyukHarfKontrol(password):
                raise Exception("Şifreniz en az 1 büyük harf bulunmalıdır")
            return True
        except Exception as hata:
            print(hata,adim)
            return False

   