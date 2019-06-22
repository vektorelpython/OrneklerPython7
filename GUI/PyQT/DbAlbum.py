from DB import DB
class dbAlbum(DB):
    def __init__(self):
        DB.adres = r"D:\İbrahim EDİZ\Ornekler\OrnekDB\chinook.db"
        super().__init__()
    
    def AlbumEkle(self,adi,artist):
        sonuc = ""
        if 1==1:
            sorgu = "insert into albums (name) values ('{}',{})".format(adi,artist)
            print(sorgu)
            sonuc = self.idu(sorgu)
        else:
            sonuc = "AE-1"
        return sonuc

    def AlbumListele(self):
        sonuc = []
        sorgu = "select * from v_album where albumid < 20"
        sonuc = self.select(sorgu)
        return sonuc