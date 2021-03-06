# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PyQt5.QtCore import pyqtSlot

from PyQt5.QtCore import *
from PyQt5 import QtGui, QtWidgets, QtCore, QtWinExtras
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Ui_info import Ui_Form


class Form(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Form, self).__init__(parent)
        self.setupUi(self)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    ui = Form()
#    ui.setupUi(Form)
    ui.show()
    sys.exit(app.exec_())
