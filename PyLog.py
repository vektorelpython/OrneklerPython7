import os
import datetime as dt
yol = ""
def KlasorKontrol():
    if os.name == "nt":
        if not os.path.exists(r"{}{}Logs".format(os.getcwd(),os.sep)):
            os.system("md Logs")
    if os.name == "posix":
        if not os.path.exists(r"{}{}Logs".format(os.getcwd(),os.sep)):
            os.system("mkdir Logs")
            
            
def tarihGonder():
    return str(dt.datetime.today().year) + "_" + str(dt.datetime.today().month) + "_" + str(dt.datetime.today().day)

def saatGonder():
    return str(dt.datetime.today().hour) + "_"+ str(dt.datetime.today().minute)

def KlasorKontrolTarih():
    global yol
    
    tarih = tarihGonder()
    if os.name == "nt":
        yol = r"{0}{1}Logs{1}{2}".format(os.getcwd(),os.sep,tarih)
        if not os.path.exists(yol):
            os.chdir(r"{0}{1}Logs".format(os.getcwd(),os.sep))
            os.system("md {}".format(tarih))
    if os.name == "posix":
        yol = r"{0}{1}Logs{1}{2}".format(os.getcwd(),os.sep,tarih)
        if not os.path.exists(yol):
            os.chdir(r"{0}{1}Logs".format(os.getcwd(),os.sep))
            os.system("mkdir {}".format(tarih))


def dosyaKontrol(yol):
    dosya = None
    tarih  = saatGonder()
#    print(yol+"{}log_{}.txt".format(os.sep,tarih))
    if not os.path.exists(yol+r"{}log_{}.csv".format(os.sep,tarih)):
        dosya = open(yol+r"{}log_{}.csv".format(os.sep,tarih),"w")
    else:
        dosya = open(yol+r"{}log_{}.csv".format(os.sep,tarih),"r+")
    return dosya
        

KlasorKontrol()
KlasorKontrolTarih()
dosyaKontrol(yol)