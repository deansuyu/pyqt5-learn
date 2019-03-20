# -*- coding: utf-8 -*-

"""
Module implementing MainWindow_1.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtWidgets, QtCore, QtWinExtras
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_xinxi import Ui_MainWindow
import login  

class MainWindow_1(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow_1, self).__init__(parent)
        self.setupUi(self)
#        self.Dialog_1=login.Dialog(self)
#        self.Dialog_1.exec_()
        
    @pyqtSlot()
    def on_add_btn_clicked(self):
        print("123",self.Dialog_1)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    ui = MainWindow_1()
#    ui.setupUi(MainWindow)
    ui.show()
    sys.exit(app.exec_())
    
    
