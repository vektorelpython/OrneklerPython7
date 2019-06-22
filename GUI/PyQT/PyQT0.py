import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow,QTableWidgetItem,QComboBox
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from DB0 import DBPyQT0
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()     
    def initUI(self):
        self.pencere = uic.loadUi(r"D:\İbrahim EDİZ\Ornekler\GUI\PyQT\PyQT0.ui")
        self.tabloDoldur()
        self.pencere.show()
    def tabloDoldur(self):
        self.pencere.tblArtist.setRowCount(5)
        self.pencere.tblArtist.setColumnCount(3)
        listeledb = DBPyQT0()
        liste = listeledb.listele()
        for cid,adi,soyadi in liste:
            demet = (cid,adi,soyadi)
            satirNumarasi = liste.index(demet)
            self.pencere.tblArtist.setItem(satirNumarasi,0,QTableWidgetItem(str(cid)))
            self.pencere.tblArtist.setItem(satirNumarasi,1,QTableWidgetItem(adi))
            self.pencere.tblArtist.setItem(satirNumarasi,2,QTableWidgetItem(soyadi))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 