import PyLog
import datetime as dt
PyLog.KlasorKontrol()
PyLog.KlasorKontrolTarih()
def LogTut(mesaj,logtipi):
    with PyLog.dosyaKontrol(PyLog.yol) as dosya:
        liste =  dosya.readlines()
        dosya.seek(0)
        dosya.truncate()
        log = "{};{};{}".format(mesaj,logtipi,dt.time.second)
        liste.append(log)
        dosya.writelines(liste)
        dosya.write("{};{}".format(mesaj,logtipi))
    
