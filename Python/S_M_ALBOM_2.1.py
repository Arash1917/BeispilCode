from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QLineEdit, QApplication, QWidget, QPushButton,
                            QVBoxLayout, QHBoxLayout, QMessageBox)
import MySQLdb as mdb
##=============================================================
class Sign_in_up(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(404, 343)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 70, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 150, 151, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pushButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "sign in"))
        self.pushButton_2.setText(_translate("MainWindow", "sign up"))
#########################################################################

class Signin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(596, 269)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 20, 251, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 90, 251, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 150, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "sign in"))

#########################################################################
class SignUp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 160, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 21, 271, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 80, 271, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 150, 271, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 220, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "password"))
        self.label_3.setText(_translate("MainWindow", "Confirm"))
        self.pushButton.setText(_translate("MainWindow", "sign up"))
#######################################################################

################################################################################
class Ui_Form(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1274, 787)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(400, 10, 421, 101))
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
        self.textEdit.setMouseTracking(True)
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 230, 311, 291))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../sara-foto/s16.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(820, 240, 311, 291))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../maneli-foto/f49.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 560, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(900, 570, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "MainWindow") )
        self.pushButton.setText(_translate("MainWindow", "Sara_fotos"))
        self.pushButton_2.setText(_translate("MainWindow", "Maneli_fotos"))
###=============================================================================


class Ui_Form1(object):

    # switch_window = QtCore.pyqtSignal(str)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        #MainWindow.setMinimumSize(900, 900)
        #MainWindow.setMaximumSize(9999, 9999)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Page 1"))
#===============================================================================0

class Ui_Form2(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Page 2"))

##==============================================================================

class Ui_Form3(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Page 2"))
#=============================================================================0

class Ui_Form4(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("../m2.jpg"))



        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Main Page"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

#=============================================================================
class Ui_Form5(object):

        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.setMinimumSize(900, 900)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
            self.label.setText("")
            #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

            self.label.setScaledContents(True)
            self.label.setObjectName("label")
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
            self.pushButton.setObjectName("pushButton")
            self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
            self.pushButton_1.setObjectName("pushButton")


            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.label.setText(_translate("MainWindow", "Main Page"))
            self.pushButton.setText(_translate("MainWindow", "Next"))
            self.pushButton_1.setText(_translate("MainWindow", "Back"))

            self.label.setText(_translate("MainWindow", "Page 2"))


#===============================================================================

class Ui_Form6(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Page 2"))
#============================================================================
class Ui_Form7(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))


##===========================================================================

class Ui_Form8(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))


##===========================================================================

class Ui_Form9(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))


##===========================================================================

class Ui_Form10(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))


##===========================================================================

class Ui_Form11(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_Form12(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_Form13(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_Form14(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_Form15(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_Form16(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_Form17(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_Form18(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_Form19(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_Form20(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_Form21(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_Form22(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_Form23(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_Form24(object):

    # switch_window = QtCore.pyqtSignal(str)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        #MainWindow.setMinimumSize(900, 900)
        #MainWindow.setMaximumSize(9999, 9999)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Page 1"))
#===============================================================================0

class Ui_FormS1(object):

    # switch_window = QtCore.pyqtSignal(str)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        #MainWindow.setMinimumSize(900, 900)
        #MainWindow.setMaximumSize(9999, 9999)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Page 1"))
#===============================================================================0

class Ui_FormS2(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Page 2"))

##==============================================================================

class Ui_FormS3(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Page 2"))
#=============================================================================0

class Ui_FormS4(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("../m2.jpg"))



        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Main Page"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

#=============================================================================
class Ui_FormS5(object):

        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.setMinimumSize(900, 900)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
            self.label.setText("")
            #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

            self.label.setScaledContents(True)
            self.label.setObjectName("label")
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
            self.pushButton.setObjectName("pushButton")
            self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
            self.pushButton_1.setObjectName("pushButton")


            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.label.setText(_translate("MainWindow", "Main Page"))
            self.pushButton.setText(_translate("MainWindow", "Next"))
            self.pushButton_1.setText(_translate("MainWindow", "Back"))

            self.label.setText(_translate("MainWindow", "Page 2"))


#===============================================================================

class Ui_FormS6(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Page 2"))
#============================================================================
class Ui_FormS7(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))


##===========================================================================

class Ui_FormS8(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))


##===========================================================================

class Ui_FormS9(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))


##===========================================================================

class Ui_FormS10(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))


##===========================================================================

class Ui_FormS11(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_FormS12(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_FormS13(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_FormS14(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_FormS15(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_FormS16(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_FormS17(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_FormS18(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_FormS19(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_FormS20(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_FormS21(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_FormS22(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_FormS23(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))

        self.label.setText(_translate("MainWindow", "Page 2"))

##===============================================================================

class Ui_FormS24(object):

    # switch_window = QtCore.pyqtSignal(str)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(900, 900)
        #MainWindow.setMinimumSize(900, 900)
        #MainWindow.setMaximumSize(9999, 9999)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 481))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg"))

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 510, 93, 28))
        self.pushButton_1.setObjectName("pushButton")



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_1.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Page 1"))

###==============================================================================
class Login_in_up(QtWidgets.QWidget, Sign_in_up):

    switch_window = QtCore.pyqtSignal()


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        #pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f13.jpg")
        #self.label.setPixmap(pix)
        #self.label.move(99, 60)

        self.pushButton.clicked.connect(self.pushbutton_handler)
        self.pushButton_2.clicked.connect(self.pushbutton_handler)

    def pushbutton_handler(self):
        self.switch_window.emit()



class Login_in(QtWidgets.QWidget, Signin):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.lineEdit.text()
        self.lineEdit_2.text()

        self.pushButton.clicked.connect(self.InsertData)

    def InsertData(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        con = mdb.connect('localhost', 'root', '', 'speicher')
        #with con:
        cur = con.cursor()
        query = 'select * from data where username = %s and password = %s'
        data = cur.execute(query, (username, password))

        if (len(cur.fetchall())>0):
            self.switch_window.emit()
            #QMessageBox.about(self, 'congrats', 'you are logged in')

        else:

            m = QMessageBox.warning(None, 'WARNING', 'Bitte nochmal versuchen,Username oder Password nicht existert')
            return m



#===========================================================================0

class Login_up(QtWidgets.QWidget, SignUp):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.lineEdit.text()
        self.lineEdit_2.text()
        self.lineEdit_3.text()

        self.pushButton.clicked.connect(self.signup)

    def signup(self):

        if self.lineEdit_2.text() =='' and self.lineEdit_3.text() =='' :
            QMessageBox.warning(self, 'ERROR', 'Sie sollen hier was schriben')

        elif self.lineEdit_2.text() == self.lineEdit_3.text():
            con = mdb.connect('localhost', 'root', '', 'speicher')
            with con:

                 cur = con.cursor()
                 cur.execute("INSERT INTO data(username, password)"
                             "VALUES('%s', '%s')" % (''.join(self.lineEdit.text()),
                                                   #''.join(self.lineEdit_3.text()),
                                                 ''.join(self.lineEdit_2.text())))
                 QMessageBox.about(self, "INFORMATION", "Daten sind Erfolgrich gespeischert" )
                 self.switch_window.emit()
        else:
            #self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('')
            msg = QMessageBox.warning(None, "Error", "Der ungleiche Password oder Confirm" )
            return(msg)

##=========================================================================
class Login(QtWidgets.QWidget, Ui_Form):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        #self.shortcut_open = QShortcut(QKeySequence('Right'), self)
        self.setupUi(self)
        #pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f13.jpg")
        #self.label.setPixmap(pix)
        #self.label.move(99, 60)

        self.pushButton.clicked.connect(self.pushbutton_handler)
        self.pushButton_2.clicked.connect(self.pushbutton_handler)


    def pushbutton_handler(self):
        self.switch_window.emit()


##===========================================================0

class Login1(QtWidgets.QWidget, Ui_Form1):

    switch_window = QtCore.pyqtSignal()
    #switch_window1 = QtCore.pyqtSignal()


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.shortcut_open = QShortcut(QKeySequence('Right'), self)
        self.shortcut_close = QShortcut(QKeySequence('Left'), self)
        self.setupUi(self)
        pix = QPixmap("C:/Users/arash/OneDrive/Desktop/m1.jpg")
        self.label.setPixmap(pix)
        hbox = QVBoxLayout()

        hbox.addWidget(self.label)
        hbox.addWidget(self.pushButton)
        hbox.addWidget(self.pushButton_1)
        self.setLayout(hbox)
        #self.label.move(10, 10)

        #self.pushButton.clicked.connect(self.pushbutton_handler)
        #self.pushButton_1.clicked.connect(self.pushbutton_handler)

    #def pushbutton_handler(self):
        #self.switch_window.emit()


#===========================================================================0

class Login2(QtWidgets.QWidget, Ui_Form2):

    switch_window = QtCore.pyqtSignal()
    #switch_window1 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.shortcut_open = QShortcut(QKeySequence('Right'), self)
        self.shortcut_close = QShortcut(QKeySequence('Left'), self)
        self.setupUi(self)
        pix = QPixmap("C:/Users/arash/OneDrive/Desktop/m2.jpg")
        self.label.setPixmap(pix)
        hbox = QVBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.pushButton)
        hbox.addWidget(self.pushButton_1)
        self.setLayout(hbox)
        self.label.move(10, 10)

        #self.pushButton.clicked.connect(self.pushbutton_handler)
        #self.pushButton_1.clicked.connect(self.pushbutton_handler)

    def pushbutton_handler(self):
        self.switch_window.emit()

    #def pushbutton_handler1(self):
        #self.switch_window1.emit()

#=============================================================================

class Login3(QtWidgets.QWidget, Ui_Form3):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.shortcut_open = QShortcut(QKeySequence('Right'), self)
        self.shortcut_close = QShortcut(QKeySequence('Left'), self)
        self.setupUi(self)
        pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f1.jpg")
        self.label.setPixmap(pix)
        hbox = QVBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.pushButton)
        hbox.addWidget(self.pushButton_1)
        self.setLayout(hbox)
        self.label.move(10, 10)

        self.pushButton.clicked.connect(self.pushbutton_handler)
        self.pushButton_1.clicked.connect(self.pushbutton_handler)

    def pushbutton_handler(self):
        self.switch_window.emit()


##===========================================================0

class Login4(QtWidgets.QWidget, Ui_Form4):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.shortcut_open = QShortcut(QKeySequence('Right'), self)
        self.shortcut_close = QShortcut(QKeySequence('Left'), self)
        self.setupUi(self)
        pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli1.jpg")
        self.label.setPixmap(pix)
        hbox = QVBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.pushButton)
        hbox.addWidget(self.pushButton_1)
        self.setLayout(hbox)
        self.label.move(10, 10)

        self.pushButton.clicked.connect(self.pushbutton_handler)
        self.pushButton_1.clicked.connect(self.pushbutton_handler)

    def pushbutton_handler(self):
        self.switch_window.emit()

#============================================================================00
class Login5(QtWidgets.QWidget, Ui_Form5):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f2.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)
            self.label.move(10, 10)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()
##=========================================================================
class Login6(QtWidgets.QWidget, Ui_Form6):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f3.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)
            self.label.move(10, 10)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class Login7(QtWidgets.QWidget, Ui_Form7):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f4.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class Login8(QtWidgets.QWidget, Ui_Form8):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f5.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)
            #self.label.move(10, 10)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class Login9(QtWidgets.QWidget, Ui_Form9):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f6.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class Login10(QtWidgets.QWidget, Ui_Form10):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f7.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class Login11(QtWidgets.QWidget, Ui_Form11):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f8.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class Login12(QtWidgets.QWidget, Ui_Form12):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f9.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class Login13(QtWidgets.QWidget, Ui_Form13):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f10.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class Login14(QtWidgets.QWidget, Ui_Form14):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f11.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class Login15(QtWidgets.QWidget, Ui_Form15):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)

            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f12.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class Login16(QtWidgets.QWidget, Ui_Form16):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f13.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class Login17(QtWidgets.QWidget, Ui_Form17):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f14.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class Login18(QtWidgets.QWidget, Ui_Form18):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f15.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class Login19(QtWidgets.QWidget, Ui_Form19):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f16.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class Login20(QtWidgets.QWidget, Ui_Form20):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f17.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class Login21(QtWidgets.QWidget, Ui_Form21):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f18.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class Login22(QtWidgets.QWidget, Ui_Form22):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f19.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class Login23(QtWidgets.QWidget, Ui_Form23):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f20.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class Login24(QtWidgets.QWidget, Ui_Form24):

    switch_window = QtCore.pyqtSignal()



    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.shortcut_open = QShortcut(QKeySequence('Right'), self)
        self.shortcut_close = QShortcut(QKeySequence('Left'), self)
        self.setupUi(self)
        pix = QPixmap("C:/Users/arash/OneDrive/Desktop/maneli-foto/f24.jpg")
        self.label.setPixmap(pix)
        hbox = QVBoxLayout()
        central_widget = QWidget()
        hbox.addWidget(self.label)
        hbox.addWidget(self.pushButton)
        hbox.addWidget(self.pushButton_1)
        self.setLayout(hbox)


        self.pushButton.clicked.connect(self.pushbutton_handler)
        self.pushButton_1.clicked.connect(self.pushbutton_handler)

    def pushbutton_handler(self):
        self.switch_window.emit()

##===================================================================================

class LoginS1(QtWidgets.QWidget, Ui_FormS1):

    switch_window = QtCore.pyqtSignal()
    #switch_window1 = QtCore.pyqtSignal()


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.shortcut_open = QShortcut(QKeySequence('Right'), self)
        self.shortcut_close = QShortcut(QKeySequence('Left'), self)
        self.setupUi(self)
        pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s1.jpg")
        self.label.setPixmap(pix)
        hbox = QVBoxLayout()

        hbox.addWidget(self.label)
        hbox.addWidget(self.pushButton)
        hbox.addWidget(self.pushButton_1)
        self.setLayout(hbox)


        self.pushButton.clicked.connect(self.pushbutton_handler)
        self.pushButton_1.clicked.connect(self.pushbutton_handler)

    def pushbutton_handler(self):
        self.switch_window.emit()


#===========================================================================0

class LoginS2(QtWidgets.QWidget, Ui_FormS2):

    switch_window = QtCore.pyqtSignal()


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.shortcut_open = QShortcut(QKeySequence('Right'), self)
        self.shortcut_close = QShortcut(QKeySequence('Left'), self)
        self.setupUi(self)
        pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s2.jpg")
        self.label.setPixmap(pix)
        hbox = QVBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.pushButton)
        hbox.addWidget(self.pushButton_1)
        self.setLayout(hbox)
        self.label.move(10, 10)


    def pushbutton_handler(self):
        self.switch_window.emit()


#=============================================================================

class LoginS3(QtWidgets.QWidget, Ui_FormS3):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.shortcut_open = QShortcut(QKeySequence('Right'), self)
        self.shortcut_close = QShortcut(QKeySequence('Left'), self)
        self.setupUi(self)
        pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s3.jpg")
        self.label.setPixmap(pix)
        hbox = QVBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.pushButton)
        hbox.addWidget(self.pushButton_1)
        self.setLayout(hbox)
        self.label.move(10, 10)

        self.pushButton.clicked.connect(self.pushbutton_handler)
        self.pushButton_1.clicked.connect(self.pushbutton_handler)

    def pushbutton_handler(self):
        self.switch_window.emit()


##===========================================================0

class LoginS4(QtWidgets.QWidget, Ui_FormS4):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.shortcut_open = QShortcut(QKeySequence('Right'), self)
        self.shortcut_close = QShortcut(QKeySequence('Left'), self)
        self.setupUi(self)
        pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s4.jpg")
        self.label.setPixmap(pix)
        hbox = QVBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.pushButton)
        hbox.addWidget(self.pushButton_1)
        self.setLayout(hbox)
        self.label.move(10, 10)

        self.pushButton.clicked.connect(self.pushbutton_handler)
        self.pushButton_1.clicked.connect(self.pushbutton_handler)

    def pushbutton_handler(self):
        self.switch_window.emit()

#============================================================================00
class LoginS5(QtWidgets.QWidget, Ui_FormS5):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s5.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)
            self.label.move(10, 10)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()
##=========================================================================
class LoginS6(QtWidgets.QWidget, Ui_FormS6):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s6.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)
            self.label.move(10, 10)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class LoginS7(QtWidgets.QWidget, Ui_FormS7):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s7.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class LoginS8(QtWidgets.QWidget, Ui_FormS8):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s8.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)
            #self.label.move(10, 10)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class LoginS9(QtWidgets.QWidget, Ui_FormS9):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s9.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class LoginS10(QtWidgets.QWidget, Ui_FormS10):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s10.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class LoginS11(QtWidgets.QWidget, Ui_FormS11):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s11.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class LoginS12(QtWidgets.QWidget, Ui_FormS12):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s12.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class LoginS13(QtWidgets.QWidget, Ui_FormS13):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s13.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class LoginS14(QtWidgets.QWidget, Ui_FormS14):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s14.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class LoginS15(QtWidgets.QWidget, Ui_FormS15):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)

            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s15.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class LoginS16(QtWidgets.QWidget, Ui_FormS16):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s16.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class LoginS17(QtWidgets.QWidget, Ui_FormS17):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s17.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class LoginS18(QtWidgets.QWidget, Ui_FormS18):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s18.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class LoginS19(QtWidgets.QWidget, Ui_FormS19):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s19.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class LoginS20(QtWidgets.QWidget, Ui_FormS20):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s20.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class LoginS21(QtWidgets.QWidget, Ui_FormS21):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s21.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class LoginS22(QtWidgets.QWidget, Ui_FormS22):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s22.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================
class LoginS23(QtWidgets.QWidget, Ui_FormS23):

        switch_window = QtCore.pyqtSignal()

        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.shortcut_open = QShortcut(QKeySequence('Right'), self)
            self.shortcut_close = QShortcut(QKeySequence('Left'), self)
            self.setupUi(self)
            pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s23.jpg")
            self.label.setPixmap(pix)
            hbox = QVBoxLayout()
            hbox.addWidget(self.label)
            hbox.addWidget(self.pushButton)
            hbox.addWidget(self.pushButton_1)
            self.setLayout(hbox)

            self.pushButton.clicked.connect(self.pushbutton_handler)
            self.pushButton_1.clicked.connect(self.pushbutton_handler)

        def pushbutton_handler(self):
            self.switch_window.emit()

##===============================================================================

class LoginS24(QtWidgets.QWidget, Ui_FormS24):

    switch_window = QtCore.pyqtSignal()
    #switch_window1 = QtCore.pyqtSignal()


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.shortcut_open = QShortcut(QKeySequence('Right'), self)
        self.shortcut_close = QShortcut(QKeySequence('Left'), self)
        self.setupUi(self)
        pix = QPixmap("C:/Users/arash/OneDrive/Desktop/sara-foto/s24.jpg")
        self.label.setPixmap(pix)
        hbox = QVBoxLayout()
        central_widget = QWidget()
        hbox.addWidget(self.label)
        hbox.addWidget(self.pushButton)
        hbox.addWidget(self.pushButton_1)
        self.setLayout(hbox)
        #self.label.move(10, 10)

        self.pushButton.clicked.connect(self.pushbutton_handler)
        self.pushButton_1.clicked.connect(self.pushbutton_handler)

    def pushbutton_handler(self):
        self.switch_window.emit()



##============================================================================


class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login_inup = Login_in_up()
        self.login_inup.pushButton.clicked.connect(self.show_login_in)
        self.login_inup.pushButton_2.clicked.connect(self.show_login_up)
        self.login_inup.show()



    def show_login_in(self):
        self.login_in = Login_in()
        self.login_in.switch_window.connect(self.show_login0)

        #self.login_inup.close()
        self.login_in.show()

    def show(self):
        self.show = Login()
        self.show.show()
        self.login_in.close()


    def show_login_up(self):
        self.login_up = Login_up()
        self.login_up.switch_window.connect(self.closelog)
        #self.login_in.close()
        self.login_up.show()


    def closelog(self):
        self.login_up = Login_up()
        self.login_up.close()
        self.login_in = Login_in()
        self.login_in.show()


    def show_login0(self):
        self.login = Login()
        #self.login.shortcut_open.activated.connect(self.show_login1)
        self.login.pushButton_2.clicked.connect(self.show_login1)
        self.login.pushButton.clicked.connect(self.show_loginS1)
        self.login.show()


    def show_login1(self):
        self.login1 =  Login1()
        self.login1.shortcut_open.activated.connect(self.show_login2)
        self.login1.shortcut_close.activated.connect(self.close1)
        self.login1.pushButton.clicked.connect(self.show_login2)
        self.login1.pushButton_1.clicked.connect(self.close1)
        #self.login.close()
        #self.login1.close()
        self.login1.show()

    def close1(self):
        self.login1.close()
        self.login.show()

    def show_login2(self):
        self.login2 = Login2()
        self.login2.shortcut_open.activated.connect(self.show_login3)
        self.login2.shortcut_close.activated.connect(self.close2)
        self.login2.pushButton.clicked.connect(self.show_login3)
        self.login2.pushButton_1.clicked.connect(self.close2)
        self.login1.close()
        self.login2.show()

    def close2(self):
        self.login2.close()
        self.login1.show()


    def show_login3(self):
        self.login3 = Login3()
        self.login3.shortcut_open.activated.connect(self.show_login4)
        self.login3.shortcut_close.activated.connect(self.close3)
        self.login3.pushButton.clicked.connect(self.show_login4)
        self.login3.pushButton_1.clicked.connect(self.close3)
        self.login2.close()
        self.login3.show()

    def close3(self):
        self.login3.close()
        self.login2.show()

    def show_login4(self):
        self.login4 = Login4()
        self.login4.shortcut_open.activated.connect(self.show_login5)
        self.login4.shortcut_close.activated.connect(self.close4)
        self.login4.pushButton.clicked.connect(self.show_login5)
        self.login4.pushButton_1.clicked.connect(self.close4)
        self.login3.close()
        self.login4.show()

    def close4(self):
        self.login4.close()
        self.login3.show()

    def show_login5(self):
        self.login5 = Login5()
        self.login5.shortcut_open.activated.connect(self.show_login6)
        self.login5.shortcut_close.activated.connect(self.close5)
        self.login5.pushButton.clicked.connect(self.show_login6)
        self.login5.pushButton_1.clicked.connect(self.close5)
        self.login4.close()
        self.login5.show()

    def close5(self):
        self.login5.close()
        self.login4.show()


    def show_login6(self):
        self.login6 = Login6()
        self.login6.shortcut_open.activated.connect(self.show_login7)
        self.login6.shortcut_close.activated.connect(self.close6)
        self.login6.pushButton.clicked.connect(self.show_login7)
        self.login6.pushButton_1.clicked.connect(self.close6)
        self.login6.show()
        self.login5.close()

    def close6(self):
        self.login6.close()
        self.login5.show()

    def show_login7(self):
        self.login7 = Login7()
        self.login7.shortcut_open.activated.connect(self.show_login8)
        self.login7.shortcut_close.activated.connect(self.close7)
        self.login7.pushButton.clicked.connect(self.show_login8)
        self.login7.pushButton_1.clicked.connect(self.close7)
        self.login6.close()
        self.login7.show()

    def close7(self):
        self.login7.close()
        self.login6.show()


    def show_login8(self):
        self.login8 = Login8()
        self.login8.shortcut_open.activated.connect(self.show_login9)
        self.login8.shortcut_close.activated.connect(self.close8)
        self.login8.pushButton.clicked.connect(self.show_login9)
        self.login8.pushButton_1.clicked.connect(self.close8)
        self.login7.close()
        self.login8.show()

    def close8(self):
        self.login8.close()
        self.login7.show()

    def show_login9(self):
        self.login9 = Login9()
        self.login9.shortcut_open.activated.connect(self.show_login10)
        self.login9.shortcut_close.activated.connect(self.close9)
        self.login9.pushButton.clicked.connect(self.show_login10)
        self.login9.pushButton_1.clicked.connect(self.close9)
        self.login8.close()
        self.login9.show()

    def close9(self):
        self.login9.close()
        self.login8.show()

    def show_login10(self):
        self.login10 = Login10()
        self.login10.shortcut_open.activated.connect(self.show_login11)
        self.login10.shortcut_close.activated.connect(self.close10)
        self.login10.pushButton.clicked.connect(self.show_login11)
        self.login10.pushButton_1.clicked.connect(self.close10)
        self.login9.close()
        self.login10.show()

    def close10(self):
        self.login10.close()
        self.login9.show()


    def show_login11(self):
        self.login11 = Login11()
        self.login11.shortcut_open.activated.connect(self.show_login12)
        self.login11.shortcut_close.activated.connect(self.close11)
        self.login11.pushButton.clicked.connect(self.show_login12)
        self.login11.pushButton_1.clicked.connect(self.close11)
        self.login10.close()
        self.login11.show()

    def close11(self):
        self.login11.close()
        self.login10.show()


    def show_login12(self):
        self.login12 = Login12()
        self.login12.shortcut_open.activated.connect(self.show_login13)
        self.login12.shortcut_close.activated.connect(self.close12)
        self.login12.pushButton.clicked.connect(self.show_login13)
        self.login12.pushButton_1.clicked.connect(self.close12)
        self.login11.close()
        self.login12.show()

    def close12(self):
        self.login12.close()
        self.login11.show()

    def show_login13(self):
        self.login13 = Login13()
        self.login13.shortcut_open.activated.connect(self.show_login14)
        self.login13.shortcut_close.activated.connect(self.close13)
        self.login13.pushButton.clicked.connect(self.show_login14)
        self.login13.pushButton_1.clicked.connect(self.close13)
        self.login12.close()
        self.login13.show()

    def close13(self):
        self.login13.close()
        self.login12.show()

    def show_login14(self):
        self.login14 = Login14()
        self.login14.shortcut_open.activated.connect(self.show_login15)
        self.login14.shortcut_close.activated.connect(self.close14)
        self.login14.pushButton.clicked.connect(self.show_login15)
        self.login14.pushButton_1.clicked.connect(self.close14)
        self.login13.close()
        self.login14.show()

    def close14(self):
        self.login14.close()
        self.login13.show()


    def show_login15(self):
        self.login15 = Login15()
        self.login15.shortcut_open.activated.connect(self.show_login16)
        self.login15.shortcut_close.activated.connect(self.close15)
        self.login15.pushButton.clicked.connect(self.show_login16)
        self.login15.pushButton_1.clicked.connect(self.close15)
        self.login14.close()
        self.login15.show()

    def close15(self):
        self.login15.close()
        self.login14.show()

    def show_login16(self):
        self.login16 = Login16()
        self.login16.shortcut_open.activated.connect(self.show_login17)
        self.login16.shortcut_close.activated.connect(self.close16)
        self.login16.pushButton.clicked.connect(self.show_login17)
        self.login16.pushButton_1.clicked.connect(self.close16)
        self.login15.close()
        self.login16.show()

    def close16(self):
        self.login16.close()
        self.login15.show()

    def show_login17(self):
        self.login17 = Login17()
        self.login17.shortcut_open.activated.connect(self.show_login18)
        self.login17.shortcut_close.activated.connect(self.close17)
        self.login17.pushButton.clicked.connect(self.show_login18)
        self.login17.pushButton_1.clicked.connect(self.close17)
        self.login16.close()
        self.login17.show()

    def close17(self):
        self.login17.close()
        self.login16.show()


    def show_login18(self):
        self.login18 = Login18()
        self.login18.shortcut_open.activated.connect(self.show_login19)
        self.login18.shortcut_close.activated.connect(self.close18)
        self.login18.pushButton.clicked.connect(self.show_login19)
        self.login18.pushButton_1.clicked.connect(self.close18)
        self.login17.close()
        self.login18.show()

    def close18(self):
        self.login18.close()
        self.login17.show()

    def show_login19(self):
        self.login19 = Login19()
        self.login19.shortcut_open.activated.connect(self.show_login20)
        self.login19.shortcut_close.activated.connect(self.close19)
        self.login19.pushButton.clicked.connect(self.show_login20)
        self.login19.pushButton_1.clicked.connect(self.close19)
        self.login18.close()
        self.login19.show()

    def close19(self):
        self.login19.close()
        self.login18.show()


    def show_login20(self):
        self.login20 = Login20()
        self.login20.shortcut_open.activated.connect(self.show_login21)
        self.login20.shortcut_close.activated.connect(self.close20)
        self.login20.pushButton.clicked.connect(self.show_login21)
        self.login20.pushButton_1.clicked.connect(self.close20)
        self.login19.close()
        self.login20.show()

    def close20(self):
        self.login20.close()
        self.login19.show()


    def show_login21(self):
        self.login21 = Login21()
        self.login21.shortcut_open.activated.connect(self.show_login22)
        self.login21.shortcut_close.activated.connect(self.close21)
        self.login21.pushButton.clicked.connect(self.show_login22)
        self.login21.pushButton_1.clicked.connect(self.close21)
        self.login20.close()
        self.login21.show()

    def close21(self):
        self.login21.close()
        self.login20.show()

    def show_login22(self):
        self.login22 = Login22()
        self.login22.shortcut_open.activated.connect(self.show_login23)
        self.login22.shortcut_close.activated.connect(self.close22)
        self.login22.pushButton.clicked.connect(self.show_login23)
        self.login22.pushButton_1.clicked.connect(self.close22)
        self.login21.close()
        self.login22.show()

    def close22(self):
        self.login22.close()
        self.login21.show()

    def show_login23(self):
        self.login23 = Login23()
        self.login23.shortcut_open.activated.connect(self.show_login24)
        self.login23.shortcut_close.activated.connect(self.close23)
        self.login23.pushButton.clicked.connect(self.show_login24)
        self.login23.pushButton_1.clicked.connect(self.close23)
        self.login22.close()
        self.login23.show()

    def close23(self):
        self.login23.close()
        self.login22.show()


    def show_login24(self):
        self.login24 = Login24()
        self.login24.shortcut_open.activated.connect(self.show_login25)
        self.login24.shortcut_close.activated.connect(self.close24)
        self.login24.pushButton.clicked.connect(self.show_login25)
        self.login24.pushButton_1.clicked.connect(self.close24)
        self.login23.close()
        self.login24.show()

    def close24(self):
        self.login24.close()
        self.login23.show()
##======================================================================
    def show_login25(self):
        self.login25 = Login24()
        self.login25.shortcut_open.activated.connect(self.show_login25)
        self.login25.shortcut_close.activated.connect(self.close25)
        self.login25.pushButton.clicked.connect(self.show_login25)
        self.login25.pushButton_1.clicked.connect(self.close25)
        self.login24.close()
        #self.login24.show()

    def close25(self):
        self.login25.close()
        self.login24.show()


    def show_loginS1(self):
        self.login1 =  LoginS1()
        self.login1.shortcut_open.activated.connect(self.show_loginS2)
        self.login1.shortcut_close.activated.connect(self.closeS1)
        self.login1.pushButton.clicked.connect(self.show_loginS2)
        self.login1.pushButton_1.clicked.connect(self.closeS1)
        self.login.close()
        #self.login1.close()
        self.login1.show()

    def closeS1(self):
        self.login1.close()
        self.login.show()

    def show_loginS2(self):
        self.login2 = LoginS2()
        self.login2.shortcut_open.activated.connect(self.show_loginS3)
        self.login2.shortcut_close.activated.connect(self.closeS2)
        self.login2.pushButton.clicked.connect(self.show_loginS3)
        self.login2.pushButton_1.clicked.connect(self.closeS2)
        self.login1.close()
        self.login2.show()

    def closeS2(self):
        self.login2.close()
        self.login1.show()


    def show_loginS3(self):
        self.login3 = LoginS3()
        self.login3.shortcut_open.activated.connect(self.show_loginS4)
        self.login3.shortcut_close.activated.connect(self.closeS3)
        self.login3.pushButton.clicked.connect(self.show_loginS4)
        self.login3.pushButton_1.clicked.connect(self.closeS3)
        self.login2.close()
        self.login3.show()

    def closeS3(self):
        self.login3.close()
        self.login2.show()

    def show_loginS4(self):
        self.login4 = LoginS4()
        self.login4.shortcut_open.activated.connect(self.show_loginS5)
        self.login4.shortcut_close.activated.connect(self.closeS4)
        self.login4.pushButton.clicked.connect(self.show_loginS5)
        self.login4.pushButton_1.clicked.connect(self.closeS4)
        self.login3.close()
        self.login4.show()

    def closeS4(self):
        self.login4.close()
        self.login3.show()

    def show_loginS5(self):
        self.login5 = LoginS5()
        self.login5.shortcut_open.activated.connect(self.show_loginS6)
        self.login5.shortcut_close.activated.connect(self.closeS5)
        self.login5.pushButton.clicked.connect(self.show_loginS6)
        self.login5.pushButton_1.clicked.connect(self.closeS5)
        self.login4.close()
        self.login5.show()

    def closeS5(self):
        self.login5.close()
        self.login4.show()


    def show_loginS6(self):
        self.login6 = LoginS6()
        self.login6.shortcut_open.activated.connect(self.show_loginS7)
        self.login6.shortcut_close.activated.connect(self.closeS6)
        self.login6.pushButton.clicked.connect(self.show_loginS7)
        self.login6.pushButton_1.clicked.connect(self.closeS6)
        self.login6.show()
        self.login5.close()

    def closeS6(self):
        self.login6.close()
        self.login5.show()

    def show_loginS7(self):
        self.login7 = LoginS7()
        self.login7.shortcut_open.activated.connect(self.show_loginS8)
        self.login7.shortcut_close.activated.connect(self.closeS7)
        self.login7.pushButton.clicked.connect(self.show_loginS8)
        self.login7.pushButton_1.clicked.connect(self.closeS7)
        self.login6.close()
        self.login7.show()

    def closeS7(self):
        self.login7.close()
        self.login6.show()


    def show_loginS8(self):
        self.login8 = LoginS8()
        self.login8.shortcut_open.activated.connect(self.show_loginS9)
        self.login8.shortcut_close.activated.connect(self.closeS8)
        self.login8.pushButton.clicked.connect(self.show_loginS9)
        self.login8.pushButton_1.clicked.connect(self.closeS8)
        self.login7.close()
        self.login8.show()

    def closeS8(self):
        self.login8.close()
        self.login7.show()

    def show_loginS9(self):
        self.login9 = LoginS9()
        self.login9.shortcut_open.activated.connect(self.show_loginS10)
        self.login9.shortcut_close.activated.connect(self.closeS9)
        self.login9.pushButton.clicked.connect(self.show_loginS10)
        self.login9.pushButton_1.clicked.connect(self.closeS9)
        self.login8.close()
        self.login9.show()

    def closeS9(self):
        self.login9.close()
        self.login8.show()

    def show_loginS10(self):
        self.login10 = LoginS10()
        self.login10.shortcut_open.activated.connect(self.show_loginS11)
        self.login10.shortcut_close.activated.connect(self.closeS10)
        self.login10.pushButton.clicked.connect(self.show_loginS11)
        self.login10.pushButton_1.clicked.connect(self.closeS10)
        self.login9.close()
        self.login10.show()

    def closeS10(self):
        self.login10.close()
        self.login9.show()


    def show_loginS11(self):
        self.login11 = LoginS11()
        self.login11.shortcut_open.activated.connect(self.show_loginS12)
        self.login11.shortcut_close.activated.connect(self.closeS11)
        self.login11.pushButton.clicked.connect(self.show_loginS12)
        self.login11.pushButton_1.clicked.connect(self.closeS11)
        self.login10.close()
        self.login11.show()

    def closeS11(self):
        self.login11.close()
        self.login10.show()


    def show_loginS12(self):
        self.login12 = LoginS12()
        self.login12.shortcut_open.activated.connect(self.show_loginS13)
        self.login12.shortcut_close.activated.connect(self.closeS12)
        self.login12.pushButton.clicked.connect(self.show_loginS13)
        self.login12.pushButton_1.clicked.connect(self.closeS12)
        self.login11.close()
        self.login12.show()

    def closeS12(self):
        self.login12.close()
        self.login11.show()

    def show_loginS13(self):
        self.login13 = LoginS13()
        self.login13.shortcut_open.activated.connect(self.show_loginS14)
        self.login13.shortcut_close.activated.connect(self.closeS13)
        self.login13.pushButton.clicked.connect(self.show_loginS14)
        self.login13.pushButton_1.clicked.connect(self.closeS13)
        self.login12.close()
        self.login13.show()

    def closeS13(self):
        self.login13.close()
        self.login12.show()

    def show_loginS14(self):
        self.login14 = LoginS14()
        self.login14.shortcut_open.activated.connect(self.show_loginS15)
        self.login14.shortcut_close.activated.connect(self.closeS14)
        self.login14.pushButton.clicked.connect(self.show_loginS15)
        self.login14.pushButton_1.clicked.connect(self.closeS14)
        self.login13.close()
        self.login14.show()

    def closeS14(self):
        self.login14.close()
        self.login13.show()


    def show_loginS15(self):
        self.login15 = LoginS15()
        self.login15.shortcut_open.activated.connect(self.show_loginS16)
        self.login15.shortcut_close.activated.connect(self.closeS15)
        self.login15.pushButton.clicked.connect(self.show_loginS16)
        self.login15.pushButton_1.clicked.connect(self.closeS15)
        self.login14.close()
        self.login15.show()

    def closeS15(self):
        self.login15.close()
        self.login14.show()

    def show_loginS16(self):
        self.login16 = LoginS16()
        self.login16.shortcut_open.activated.connect(self.show_loginS17)
        self.login16.shortcut_close.activated.connect(self.closeS16)
        self.login16.pushButton.clicked.connect(self.show_loginS17)
        self.login16.pushButton_1.clicked.connect(self.closeS16)
        self.login15.close()
        self.login16.show()

    def closeS16(self):
        self.login16.close()
        self.login15.show()

    def show_loginS17(self):
        self.login17 = LoginS17()
        self.login17.shortcut_open.activated.connect(self.show_loginS18)
        self.login17.shortcut_close.activated.connect(self.closeS17)
        self.login17.pushButton.clicked.connect(self.show_loginS18)
        self.login17.pushButton_1.clicked.connect(self.closeS17)
        self.login16.close()
        self.login17.show()

    def closeS17(self):
        self.login17.close()
        self.login16.show()


    def show_loginS18(self):
        self.login18 = LoginS18()
        self.login18.shortcut_open.activated.connect(self.show_loginS19)
        self.login18.shortcut_close.activated.connect(self.closeS18)
        self.login18.pushButton.clicked.connect(self.show_loginS19)
        self.login18.pushButton_1.clicked.connect(self.closeS18)
        self.login17.close()
        self.login18.show()

    def closeS18(self):
        self.login18.close()
        self.login17.show()

    def show_loginS19(self):
        self.login19 = LoginS19()
        self.login19.shortcut_open.activated.connect(self.show_loginS20)
        self.login19.shortcut_close.activated.connect(self.closeS19)
        self.login19.pushButton.clicked.connect(self.show_loginS20)
        self.login19.pushButton_1.clicked.connect(self.closeS19)
        self.login18.close()
        self.login19.show()

    def closeS19(self):
        self.login19.close()
        self.login18.show()


    def show_loginS20(self):
        self.login20 = LoginS20()
        self.login20.shortcut_open.activated.connect(self.show_loginS21)
        self.login20.shortcut_close.activated.connect(self.closeS20)
        self.login20.pushButton.clicked.connect(self.show_loginS21)
        self.login20.pushButton_1.clicked.connect(self.closeS20)
        self.login19.close()
        self.login20.show()

    def closeS20(self):
        self.login20.close()
        self.login19.show()


    def show_loginS21(self):
        self.login21 = LoginS21()
        self.login21.shortcut_open.activated.connect(self.show_loginS22)
        self.login21.shortcut_close.activated.connect(self.closeS21)
        self.login21.pushButton.clicked.connect(self.show_loginS22)
        self.login21.pushButton_1.clicked.connect(self.closeS21)
        self.login20.close()
        self.login21.show()

    def closeS21(self):
        self.login21.close()
        self.login20.show()

    def show_loginS22(self):
        self.login22 = LoginS22()
        self.login22.shortcut_open.activated.connect(self.show_loginS23)
        self.login22.shortcut_close.activated.connect(self.closeS22)
        self.login22.pushButton.clicked.connect(self.show_loginS23)
        self.login22.pushButton_1.clicked.connect(self.closeS22)
        self.login21.close()
        self.login22.show()

    def closeS22(self):
        self.login22.close()
        self.login21.show()

    def show_loginS23(self):
        self.login23 = LoginS23()
        self.login23.shortcut_open.activated.connect(self.show_loginS24)
        self.login23.shortcut_close.activated.connect(self.closeS23)
        self.login23.pushButton.clicked.connect(self.show_loginS24)
        self.login23.pushButton_1.clicked.connect(self.closeS23)
        self.login22.close()
        self.login23.show()

    def closeS23(self):
        self.login23.close()
        self.login22.show()


    def show_loginS24(self):
        self.login24 = LoginS24()
        self.login24.shortcut_open.activated.connect(self.show_loginS25)
        self.login24.shortcut_close.activated.connect(self.closeS24)
        self.login24.pushButton.clicked.connect(self.show_loginS25)
        self.login24.pushButton_1.clicked.connect(self.closeS24)
        self.login23.close()
        self.login24.show()

    def closeS24(self):
        self.login24.close()
        self.login23.show()
##======================================================================
    def show_loginS25(self):
        self.login25 = LoginS24()
        self.login25.shortcut_open.activated.connect(self.show_loginS25)
        self.login25.shortcut_close.activated.connect(self.closeS25)
        self.login25.pushButton.clicked.connect(self.show_loginS25)
        self.login25.pushButton_1.clicked.connect(self.closeS25)
        self.login24.close()
        #self.login24.show()

    def closeS25(self):
        self.login25.close()
        self.login24.show()



def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
