####>>>>>progressbar<<<<<<<<


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
######baray ijad vaghfe dar frayand danlod module zir ra import mikonim
import time as tm


class F(QWidget):
    
    def __init__(self):
        super(F, self).__init__()
        self.setUI()
    
    def setUI(self) :
        self.setGeometry(10,10,300,300)
        self.setWindowTitle('arash')
        self.setFixedSize(300, 300)

        self.prog = QProgressBar(self)
        self.prog.setGeometry(40, 40, 250, 10)

        self.btn = QPushButton('download', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(lambda: self.download())
        self.list = list(range(101))
        self.show()


    def download(self):

        for i in self.list:
            tm.sleep(.5)
            print(type(i))
            self.prog.setValue(i)
           

        
        
if __name__=="__main__":
   print(__name__)
   app = QApplication(sys.argv)
   ex=F()
   sys.exit(app.exec_())
