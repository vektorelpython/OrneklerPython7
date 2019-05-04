#demet = (1,)
#liste = [(123,23123),[123,123]]
#demet = (1,2,3,[123123,123123],(3243,2323))
#print(demet[3])


sozluk = {"Kitap":"Book","Apple":"Elma","apple":"elma"}
print(sozluk)
print(sozluk["Apple"])

adaylar = {"1":{"Adı":"Sinan","Soyadı":"İlhan","Yaş":19},
           "2":{"Adı":"Ali","Soyadı":"Veli","Yaş":23}}
adaylar["2"]["Adı"] = "Ahmet"
adaylar.update({"3":{"Adı":"Abuzer","Soyadı":"Ahmet","Yaş":32}})
print(adaylar)