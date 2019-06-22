import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow,QTableWidgetItem,QComboBox
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from DbAlbum import dbAlbum
## combo için artist DB eklendi
from DBArtist import DBArtist

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()     
    def initUI(self):
        self.pencere = uic.loadUi(r"D:\İbrahim EDİZ\Ornekler\GUI\PyQT\Album.ui")
        self.pencere.Dugme.clicked.connect(self.on_click)
        self.pencere.listele.clicked.connect(self.listele)
        self.comboDoldur()
        self.pencere.show()        
    @pyqtSlot()
    def on_click(self):
        pass
        # gelen_text = self.pencere.ilkFormTxt.text()
        # kayit = DBArtist()
        # sonuc =  kayit.artistEkle(gelen_text)
        # print(sonuc)
        # if sonuc == "1":
        #     deneme =  QMessageBox.information(self,"Bilgi","Kayıt Başarılı",
        #     QMessageBox.Ok,QMessageBox.Ok)
    def comboDoldur(self):
        listelemeDB = DBArtist()
        sonuc = listelemeDB.artistListele()
        for a,b in sonuc:
            self.pencere.cmbArtist.addItem(a)
    def listele(self):
        listelemeDB = dbAlbum()
        sonuc = listelemeDB.AlbumListele()
        self.pencere.tblAlbum.setColumnCount(4)
        self.pencere.tblAlbum.setRowCount(20)
        for item in sonuc:
            satirNum =  sonuc.index(item)
            print(item[0])
            self.pencere.tblAlbum.setItem(satirNum,0,QTableWidgetItem(item[0]))
            self.pencere.tblAlbum.setItem(satirNum,1,QTableWidgetItem(item[1]))
            self.pencere.tblAlbum.setItem(satirNum,2,QTableWidgetItem(item[2]))
            self.pencere.tblAlbum.setItem(satirNum,3,QTableWidgetItem(item[3]))
        # for item in sonuc:
        #     listitem = QListWidgetItem(item[1])
        #     self.pencere.lstBox.addItem(listitem)
        # print(sonuc)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 
