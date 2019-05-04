##adi = input("Adını Giriniz:")
##soyadi = input("Soyadı Giriniz:")
##telefon  = input("Telefon Giriniz:")
##metin = "{};{};{}\n".format(adi,soyadi,telefon)
#
#dosya = open("deneme.txt","r+")
##print(dosya.readline())
#dosya.truncate()
#liste = dosya.readlines()
#liste.append("""
#             denemelisteden;
#             denemelisteden;
#             denemelisteden
#             """)
#dosya.writelines(liste)
#dosya.close()


dosya = open("defter.txt","r+")
print("1",dosya.read())
print(dosya.tell())
print("2",dosya.read())

#dosya.readline()
#dosya.readlines()