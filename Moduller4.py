import os 
def tara(dizin):
    baslangic = os.getcwd()
    dosyalar = []
    os.chdir(dizin)
    
    for item in os.listdir(os.curdir):
        if not os.path.isdir(item):
            dosyalar.append(item)
        else:
            dosyalar.extend(tara(item))
    os.chdir(baslangic)
    return dosyalar

print(os.path.dirname(os.path.abspath("deneme.txt")))

