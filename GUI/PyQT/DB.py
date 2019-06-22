import sqlite3 as sql

class DB():
    adres = "" 
    def __init__(self):
        self.db = None
        self.cur = None
        self.dbAc()
        

    def dbAc(self):
        self.db = sql.connect(self.adres)
        self.cur = self.db.cursor() 

    def select(self,sorgu):
        liste = []
        try:
            self.dbAc()
            self.cur.execute(sorgu)
            liste =  self.cur.fetchall()
        except Exception as hata: 
            liste.append(hata)
        finally:
            self.db.close()
            return liste

    def idu(self,sorgu=""):
        sonuc = "0"
        try:
            self.dbAc()
            self.cur.execute(sorgu)
            sonuc = "1"
            self.db.commit()
        except Exception as hata:
            sonuc = hata
        finally:
            self.db.close()
            return sonuc
        
