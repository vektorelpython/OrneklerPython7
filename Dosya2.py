with open("indir.png","rb+") as dosya:
    
    if dosya.read()[1:4] == b"PNG":
        print("Dosyanın Formatı Doğru")
        
print("1- Merhaba\n",file=open("deneme.txt","a+"))
print("2- Merhaba\n",file=open("deneme.txt","a+"))