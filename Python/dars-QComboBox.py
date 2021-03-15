import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel

class F(QWidget):

    def __init__(self):
        super(F, self).__init__()
        self.setUI()

    def setUI(self) :
        self.lb1 = QLabel(' ', self)
        self.lb1.resize(50, 20)
        self.lb1.move(50, 150)
        self.setGeometry(10,10,300,300)
        self.setWindowTitle('QComboBox')

        self.com1 = QComboBox(self)
        self.com1.addItem('python', self)
        self.com1.addItem('java', self)
        self.com1.addItem('c++', self)
        self.com1.addItem('pyqt5', self)

        self.com1.move(100, 100)
        self.com1.resize(100, 20)

        self.com1.activated.connect(lambda: self.combItem())
        self.show()
    def combItem(self):
        text = self.com1.currentText()
        index = self.com1.currentIndex()
        print(text, ' ', index)
        self.lb1.setText(text)

if __name__=="__main__":
   print(__name__)
   app = QApplication(sys.argv)
   ex=F()
   sys.exit(app.exec_())
