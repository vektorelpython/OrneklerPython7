import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Örnekler'
        self.left = 25
        self.top = 25
        self.width = 320
        self.height = 200
        self.initUI()     
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        dugme = QPushButton("Tıkla Yazdır",self)
        dugme.move(30,40)
        dugme.clicked.connect(self.on_click)

        dugme2 = QPushButton("Kapat",self)
        dugme2.move(30,70)
        dugme2.clicked.connect(self.close)
        self.show()        
    @pyqtSlot()
    def on_click(self):
        mesaj = self.textbox.text()
        dugmeCevap = QMessageBox.information(self,"Mesaj Başlık",mesaj,
        QMessageBox.Yes | QMessageBox.Retry | QMessageBox.No, QMessageBox.Retry)
        if dugmeCevap == QMessageBox.Yes:
            print(mesaj)
        elif dugmeCevap == QMessageBox.No:
            self.textbox.setText("Hayır Dedi")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 
