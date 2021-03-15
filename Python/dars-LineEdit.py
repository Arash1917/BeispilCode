import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
                           
class F(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setUI()
    
    def setUI(self) :
        self.setGeometry(10,10,300,300)
        self.setWindowTitle('arash')
        btn = QPushButton('copy', self)
        
        btn.move(100, 100)
        btn.clicked.connect(self.exit)
#####===================================for LineEdit
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(10, 10)
        self.textbox1.resize(200, 20)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(10, 35)
        self.textbox2.resize(200, 20)
        self.show()
        

    def exit(self):
        T1 = self.textbox1.text()
        self.textbox2.setText(T1)

    


    

        
if __name__=="__main__":
   print(__name__)
   app = QApplication(sys.argv)
   ex=F()
   sys.exit(app.exec_())
