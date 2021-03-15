


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

#####==================================================matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random as rn


class F(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setUI()
    
    def setUI(self) :
        self.setGeometry(10,10,300,300)
        self.setWindowTitle('arash')

        push1=QPushButton('hist', self)
        push2=QPushButton('hist.close', self)
        push3=QPushButton('exit', self)

        push1.setGeometry(10,10,300,100)
        push2.setGeometry(10,150,300,100)
        push3.setGeometry(10,300,300,100)
        

        #mat=Plot_data(self, width=5, high=4)
        #mat.move(300,300)


        push1.clicked.connect(lambda : mat.plot())
        push2.clicked.connect(lambda : plt.close())
        push3.clicked.connect(lambda : self.close())

        mat = Plot_data()
        #mat.move(300,300)

        
        self.showFullScreen()
####=================================matlab_python

class Plot_data(FigureCanvas):


    def __init__(self):
        #fig=Figure(figsize=(width, height), dpi=dpi)
        #self.axes=fig.add_subplot(111)

        self.data=[]

        #self.close()
        #self.plot()


    def plot(self):
       for i in list(range(200)):
           self.data.append(rn.randint(0,i))
           t1, t2, t3 = plt.hist(self.data,5,facecolor='blue', alpha=0.5)
           plt.show()


           
if __name__=="__main__":
   print(__name__)
   app = QApplication(sys.argv)
   ex=F()
   ex.showFullScreen()
   sys.exit(app.exec_())
        
        
