import sys
from PyQt5.QtWidgets import QApplication, QWidget,QTableWidget, QTableWidgetItem, QVBoxLayout

class F(QTableWidget):

    def __init__(self):
        super(F, self).__init__()
        self.setUI()

    def setUI(self):
        self.setGeometry(10,10,300,300)
        self.setWindowTitle('New')
        self.table()
        self.lay = QVBoxLayout()
        self.lay.addWidget(self.tw)
        self.setLayout(self.lay)
        self.show()


    def table(self):
        self.tw = QTableWidget()
        self.tw.setRowCount(4)
       #setRowCount, baray khane hay ofoghi jadval ast
        self.tw.setColumnCount(3)
       #baray nveshtan chizi dar jadval az tabee zir estefade mikonim
        self.tw.setItem(0, 1, QTableWidgetItem('soton 1'))
        self.tw.setItem(0, 2, QTableWidgetItem('soton 2'))
        self.tw.setItem(1, 0, QTableWidgetItem('soton 1'))
        self.tw.setItem(2, 0, QTableWidgetItem('soton 2'))
        self.tw.setItem(3, 0, QTableWidgetItem('soton 3'))
####================mikhahim kari konim ke mogheyat har khane ba klik roy an moshakhas shavad
        self.tw.clicked.connect(self.khane_ra_printkon)

    def khane_ra_printkon(self):
        for cell in self.tw.selectedItems():
            print(cell.text())


if __name__=="__main__":
   print(__name__)
   app = QApplication(sys.argv)
   ex=F()
   sys.exit(app.exec_())
