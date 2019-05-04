#def OutFunc(a,b):
#    c = a + b
#    def InFunc(c):
#        c = c**a
#        return c
#    def InFunc2(c):
#        c = c**b
#        return c
#    return InFunc(c),InFunc2(c)
#print(OutFunc(2,5)[1])


def HesapMakinesi(**kwargs):
    sonuc = 0
    for key,value in kwargs.items():
        if key.upper() == "TOPLA":
            for i in value:
                sonuc += i
            print(sonuc)
        elif key.upper() == "CIKAR":
            a,b = value
            sonuc = a-b
            print(sonuc)
    else:
        print("Girdiğiniz parametreleri kontrol ediniz")
        
    
HesapMakinesi(top=[1,2,3])




    
    
