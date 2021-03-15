# darbare MESSAGEBOX

import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QMainWindow, QMessageBox

class F(QMainWindow):

    def __init__(self):
        super(F, self).__init__()
        self.setUI()

    def setUI(self) :
        self.setGeometry(10,10,300,300)
        self.setWindowTitle('QMessageBox')
        btn = QPushButton('close', self)

        btn.move(100, 100)
        btn.clicked.connect(self.exit)
        #self.statusBar().showMessage('first')
        self.show()


    def exit(self):
        p = QMessageBox.question(self, 'Message', 'می خواهید پنجره را ببندید؟',QMessageBox.Yes |QMessageBox.No | QMessageBox.Help)
        #return(p)
        if p == QMessageBox.Yes:
            
            self.close()


        else:
            pass


if __name__=="__main__":
   print(__name__)
   app = QApplication(sys.argv)
   ex=F()
   sys.exit(app.exec_())
