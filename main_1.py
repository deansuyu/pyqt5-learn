# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtWidgets, QtCore, QtWinExtras
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_main_1 import Ui_Form
import time
class Mythread(QThread):
    
    def __init__(self, label):
        super(Mythread, self).__init__()
        self.label=label
    def run(self):
        print("开始")
        time.sleep(5)
        print("结束")
        self.label.setText("结束")

class Form(QWidget, Ui_Form):

    def __init__(self, parent=None):
    
        super(Form, self).__init__(parent)
        self.setupUi(self)
        self.Mythread=Mythread(self.label)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.Mythread.start()
        self.label.setText("开始")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Form()
    ui.show()
    sys.exit(app.exec_())
    
    
