#Örnek Proje Başlangıç
with open(r"D:\İbrahim EDİZ\Proje\harita.txt","r+") as dosya:
    liste = dosya.readlines()
    for item in liste:
        for i in item.split(";"):
            print(i)
