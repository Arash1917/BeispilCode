import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QColorDialog, QPushButton
from PyQt5.QtGui import QColor




class F(QWidget):

    def __init__(self):
        super(F, self).__init__()
        self.setUI()

    def setUI(self) :
        self.setGeometry(10,10,300,300)
        self.setWindowTitle('New')
        self.setFixedSize(500, 500)

        p1 = QPushButton('آموزش پایتون', self)
        p1.move(50, 10)
        p1.resize(200, 200)
        p1.clicked.connect(lambda: self.rangha(p1))

        p2 = QPushButton('آموزش پایتون', self)
        p2.move(250, 10)
        p2.resize(200, 200)
        p2.clicked.connect(lambda: self.rangha(p2))

        p3 = QPushButton('آموزش پایتون', self)
        p3.move(50, 250)
        p3.resize(200, 200)
        p3.clicked.connect(lambda: self.rangha(p3))

        p4 = QPushButton('آموزش پایتون', self)
        p4.move(250, 250)
        p4.resize(200, 200)
        p4.clicked.connect(lambda: self.rangha(p4))

        self.show()


    def rangha(self, push):
        QC = QColorDialog()
        c = QC.getColor()
###========================baray taghir rang aval bayad code zir ra be tabee ezafe konim
        C1 = c.name()
####=============================setting marbot be rangha baray pushbutton
        palette = push.palette()
        role = push.foregroundRole()
        role1 = push.backgroundRole()
        palette.setColor(role, QColor(C1))
        palette.setColor(role1, QColor(C1))
        push.setPalette(palette)
        push.setAutoFillBackground(True)


if __name__=="__main__":
   print(__name__)
   app = QApplication(sys.argv)
   ex=F()
   sys.exit(app.exec_())
