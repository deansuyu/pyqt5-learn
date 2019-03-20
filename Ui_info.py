# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python\_eric6project\info.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(343, 378)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.sex = QtWidgets.QComboBox(Form)
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.verticalLayout.addWidget(self.sex)
        self.promisser = QtWidgets.QCheckBox(Form)
        self.promisser.setChecked(True)
        self.promisser.setObjectName("promisser")
        self.verticalLayout.addWidget(self.promisser)
        self.user = QtWidgets.QLineEdit(Form)
        self.user.setObjectName("user")
        self.verticalLayout.addWidget(self.user)
        self.PassW = QtWidgets.QLineEdit(Form)
        self.PassW.setObjectName("PassW")
        self.verticalLayout.addWidget(self.PassW)
        self.OK_btn = QtWidgets.QPushButton(Form)
        self.OK_btn.setObjectName("OK_btn")
        self.verticalLayout.addWidget(self.OK_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name.setPlaceholderText(_translate("Form", "姓名"))
        self.sex.setItemText(0, _translate("Form", "男"))
        self.sex.setItemText(1, _translate("Form", "女"))
        self.promisser.setText(_translate("Form", "权限"))
        self.user.setPlaceholderText(_translate("Form", "用户名"))
        self.PassW.setPlaceholderText(_translate("Form", "密码"))
        self.OK_btn.setText(_translate("Form", "确定"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

