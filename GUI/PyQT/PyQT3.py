import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow,QListWidgetItem
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from DBArtist import DBArtist
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()     
    def initUI(self):
        self.pencere = uic.loadUi(r"D:\İbrahim EDİZ\Ornekler\GUI\PyQT\ilkForm.ui")
        self.pencere.Dugme.clicked.connect(self.on_click)
        self.pencere.listele.clicked.connect(self.listele)
        self.pencere.show()        
    @pyqtSlot()
    def on_click(self):
        gelen_text = self.pencere.ilkFormTxt.text()
        kayit = DBArtist()
        sonuc =  kayit.artistEkle(gelen_text)
        print(sonuc)
        if sonuc == "1":
            deneme =  QMessageBox.information(self,"Bilgi","Kayıt Başarılı",
            QMessageBox.Ok,QMessageBox.Ok)

    def listele(self):
        listelemeDB = DBArtist()
        sonuc = listelemeDB.artistListele()
        for item in sonuc:
            listitem = QListWidgetItem(item[1])
            self.pencere.lstBox.addItem(listitem)
        print(sonuc)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 
