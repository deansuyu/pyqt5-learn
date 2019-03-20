# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import *
from PyQt5 import QtGui, QtWidgets, QtCore, QtWinExtras
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_login import Ui_Dialog
from xinxi import MainWindow_1


class Dialog(QDialog, Ui_Dialog):
    
    def __init__(self, parent=None):
       
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        
    @pyqtSlot()
    def on_ok_clicked(self):
        username=self.user.text()
        password=self.password.text()
        
        if username == '':
            QMessageBox.information(self, "提示", " 用户名不能为空",QMessageBox.Ok, QMessageBox.Ok)
        else:
            if password == '':
                QMessageBox.information(self, "提示", " 密码不能为空",QMessageBox.Ok, QMessageBox.Ok)
            else:
                if username=="admin" and password =="admin":
                    self.hide()
                    self.mainwindow=MainWindow_1()
                    self.mainwindow.show()
                else:
                    QMessageBox.information(self, "提示", " 密码错误",QMessageBox.Ok, QMessageBox.Ok)
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
#    Dialog = QtWidgets.QDialog()
    ui = Dialog()
#    ui.setupUi(Dialog)
    ui.show()
    sys.exit(app.exec_())
    
    
