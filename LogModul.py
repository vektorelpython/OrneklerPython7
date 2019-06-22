import PyLog
import datetime as dt
PyLog.KlasorKontrol()
PyLog.KlasorKontrolTarih()
#1 bilgi
#2 uyarı
#3 hata
def LogTut(mesaj,logtipi):
    with PyLog.dosyaKontrol(PyLog.yol) as dosya:
        liste =  dosya.readlines()
        dosya.seek(0)
        dosya.truncate()
        log = "{};{};{}\n".format(mesaj,logtipi,str(dt.datetime.today().second))
        liste.append(log)
        dosya.writelines(liste)
    
