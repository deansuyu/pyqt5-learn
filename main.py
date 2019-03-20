# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import *
from PyQt5 import QtGui, QtWidgets, QtCore, QtWinExtras
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from  Ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.mybutton=MyPushButton(self)
        self.mybutton1=MyPushButton(self)
        self.mybutton1.setGeometry(QtCore.QRect(70, 100, 80, 20))
        self.mybutton1.setText("我不是按钮")
        
        self.a=0
        self.pushButton.clicked.connect(self.showText)
        
    def showText(self):
        self.a+=1
        self.label.setText(str(self.a))
        print(self.a)
class MyPushButton(QPushButton):
    def __init__(self, parent=None):
        super(MyPushButton, self).__init__(parent)
        
        self.setText("我是按钮")
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
