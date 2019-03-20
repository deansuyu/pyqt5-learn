# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python\_eric6project\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(235, 113)
        Dialog.setMinimumSize(QtCore.QSize(235, 113))
        Dialog.setMaximumSize(QtCore.QSize(235, 113))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(9, 9, 36, 16))
        self.label.setObjectName("label")
        self.user = QtWidgets.QLineEdit(Dialog)
        self.user.setGeometry(QtCore.QRect(51, 9, 159, 20))
        self.user.setClearButtonEnabled(True)
        self.user.setObjectName("user")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(9, 35, 36, 16))
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(51, 35, 159, 20))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 70, 158, 25))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ok = QtWidgets.QPushButton(self.widget)
        self.ok.setObjectName("ok")
        self.gridLayout.addWidget(self.ok, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(self.password.clear)
        self.pushButton_2.clicked.connect(self.user.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "用户名"))
        self.user.setPlaceholderText(_translate("Dialog", "请输入用户名"))
        self.label_2.setText(_translate("Dialog", "密  码"))
        self.password.setPlaceholderText(_translate("Dialog", "请输入密码"))
        self.ok.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "重置"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

