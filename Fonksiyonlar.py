def pi():
    return 22/7
    
print("pi",pi())

def topla(a=0,b=0,c=0,d=0):
    sonuc = a+b-c-d+pi()
    return sonuc

print("topla",topla())

sonuc =  topla(c=1,d=7,a=4,b=3)
print(sonuc)



#
def tekMi(sayi=0):
    if sayi%2>0:
        return True
    else:
        return False

if tekMi():
    print("Tek")

