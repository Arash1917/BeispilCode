import sys
from PyQt5.QtWidgets import QApplication, QWidget



class F(QWidget):


  def __init__(self):
      super().__init__()
      self.setUI()

  def setUI(self):
      self.setGeometry(10, 10, 300, 300)
      self.setWindowTitle("arash")
      self.show()


if  __name__=="__main__":
     print(__name__)
     app = QApplication(sys.argv)
     ex = F()
     sys.exit(app.exec_())
