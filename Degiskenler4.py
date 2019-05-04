# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 09:04:00 2019

@author: vektorel
"""
#
#Adi =  input("Adın ne?")
#print("Merhaba",Adi)

#say1 = int(input("1. Sayıyı Giriniz"))
#say2 = int(input("2. Sayıyı Giriniz"))
#print(say1+say2)
#


var1 = ""
var1 = ''
#var1 = """"""
#
#var1 = "-----------------M e r haba----------------"
#var1 =  var1.lstrip("-").rstrip("-").replace(" ","")
#
#var1 = var1.replace("'","")
#
#
#var1 = "Teşekkürler Süpermen"
#print(var1)
#var1 = var1.replace("e","i").replace("ü","i")
#print(var1)
#
#
#print(input("Adınız :").upper())
#var2 = "deneme"
#print(var2.split("e"))
#


var1 =  "Ali;Veli;123456"
print(var1.split(";"))
print(var1.index("Veli"))


#var1 = "www.mektep.com.tr"
#print(var1[0:3],var1[4:10],sep="\n")



var1 = "0123456789"
print(var1.index("3"))


var1 = "www.google.com"
print(len(var1))
print(var1)
ifade = input("Çıkarmak istediğin kelimeyi yaz")
sayisal = var1.index(ifade)
var1 = var1.replace(var1[sayisal:sayisal + (len(ifade))],var1[sayisal:sayisal + (len(ifade))].upper())
print(var1)


"I know, it isn't the greatest"























