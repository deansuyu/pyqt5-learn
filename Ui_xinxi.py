# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python\_eric6project\xinxi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 386)
        MainWindow.setMinimumSize(QtCore.QSize(544, 386))
        MainWindow.setMaximumSize(QtCore.QSize(544, 386))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.student = QtWidgets.QRadioButton(self.centralWidget)
        self.student.setChecked(True)
        self.student.setObjectName("student")
        self.gridLayout.addWidget(self.student, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 2)
        self.del_btn = QtWidgets.QPushButton(self.centralWidget)
        self.del_btn.setObjectName("del_btn")
        self.gridLayout.addWidget(self.del_btn, 4, 1, 1, 1)
        self.add_btn = QtWidgets.QPushButton(self.centralWidget)
        self.add_btn.setObjectName("add_btn")
        self.gridLayout.addWidget(self.add_btn, 4, 0, 1, 1)
        self.table = QtWidgets.QRadioButton(self.centralWidget)
        self.table.setObjectName("table")
        self.gridLayout.addWidget(self.table, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.student.setText(_translate("MainWindow", "教师"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "类型"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "权限"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "名字"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "账号名"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "密码"))
        self.del_btn.setText(_translate("MainWindow", "删除"))
        self.add_btn.setText(_translate("MainWindow", "增加"))
        self.table.setText(_translate("MainWindow", "学生"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

