import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QSlider
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import random as rn

class F(QWidget):

    def __init__(self):
        super(F, self).__init__()
        self.setUI()

    def setUI(self) :
        self.setGeometry(10,10,500,500)
        self.setWindowTitle('arash')
        self.setFixedSize(500, 500)

        self.qf = QFrame(self)
        self.qf.setGeometry(100, 10, 300, 300)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(100, 320, 300, 15)
        self.slider.valueChanged.connect(lambda: self.change_slider())
#####======================================setColor
        self.palette = self.qf.palette()
        role = self.qf.backgroundRole()
        self.palette.setColor(role, QColor(215, 113, 180))
        self.qf.setPalette(self.palette)
        self.qf.setAutoFillBackground(True)

        self.show()

    def change_slider(self):

        #RGB = (2(bit)^8)*(2(bit)^8)*(2(bit)^8) = 256*256*256=16777216
        #R=[a,b,c,d,...]#0-255==>>len(G)=100
        #B=[a2,b2,c2,d2,]#0-255==>>len(G)=100
        #B=[a3,b3,c3,d3,]#0-255==>>len(B)=100
        #LIST_COLOR=[R[0] G[0] B[0]], [R[1] G[1] B[1]],[.....],.....]=[[a,a2,a3],[b,b2,b3],[....],.....]

        color:change=self.slider.value()

        Red=[]
        Green=[]
        Blue=[]

        for i in list(range(100)):
            Red.append(rn.randit(0,255))
            Green.append(rn.randit(0,255))
            Blue.append(rn.randit(0,255))


        loop = list(range(100))
        LIST_COLOR=[]

        #self.palette=self.qf.palette()
        #role=self.qf.backgroundRole()

        for i in loop:
            arg=[Red[i],Green[i],Blue[i]]
            LIST_COLOR.append(arg)
            print(LIST_COLOR)


if __name__=="__main__":
   print(__name__)
   app = QApplication(sys.argv)
   ex=F()
   sys.exit(app.exec_())
