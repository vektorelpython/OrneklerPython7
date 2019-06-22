from DB import DB
class DBArtist(DB):
    def __init__(self):
        DB.adres = r"D:\İbrahim EDİZ\Ornekler\OrnekDB\chinook.db"
        super().__init__()
    
    def artistEkle(self,adi):
        sonuc = ""
        if 1==1:
            sorgu = "insert into artists (name) values ('{}')".format(adi)
            print(sorgu)
            sonuc = self.idu(sorgu)
        else:
            sonuc = "AE-1"
        return sonuc

    def artistListele(self):
        sonuc = []
        sorgu = "SELECT * FROM artists"
        sonuc = self.select(sorgu)
        return sonuc