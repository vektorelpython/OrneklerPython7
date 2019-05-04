
liste = []
for i in range(0,100):
    if i%2>0:
        liste.append(i)
    else:
        pass
print(liste)
liste.clear()
for i in range(100,0,-2):
    liste.append(i)
print(liste)  




metin = "BEŞİKTAŞ"
#if "B" in metin:
#    print("Var")

for i in metin:
    print("*",i,"*")

print("-"*20)

for i in range(0,len(metin)):
    print("*",metin[i],"*")

