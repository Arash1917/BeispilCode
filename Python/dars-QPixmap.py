import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap

class F(QWidget):

    def __init__(self):
        super(F, self).__init__()
        self.setUI()

    def setUI(self) :
        self.setGeometry(30,30,400,400)
        self.setWindowTitle('New')
        lb = QLabel(self)
        pix = QPixmap('C:/Users/arash/OneDrive/Desktop/Python1.jpg')

        lb.setPixmap(pix)
######======================label ba dastor move() makanash avaz misavad
        lb.move(50, 50)

        #bt = QPushButton('faradars', self)
        #bt.move(20, 20)
        #bt.resize(70, 55)




        self.show()

if __name__=="__main__":
   print(__name__)
   app = QApplication(sys.argv)
   ex=F()
   sys.exit(app.exec_())
