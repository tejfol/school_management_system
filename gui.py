# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(637, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.insert_data_btn = QtWidgets.QPushButton(self.centralwidget)
        self.insert_data_btn.setGeometry(QtCore.QRect(260, 10, 113, 32))
        self.insert_data_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.insert_data_btn.setObjectName("insert_data_btn")
        self.update_data_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_data_btn.setGeometry(QtCore.QRect(370, 10, 113, 32))
        self.update_data_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.update_data_btn.setObjectName("update_data_btn")
        self.delete_data_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_data_btn.setGeometry(QtCore.QRect(480, 10, 113, 32))
        self.delete_data_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_data_btn.setObjectName("delete_data_btn")
        self.FirstName_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.FirstName_entry.setGeometry(QtCore.QRect(120, 10, 113, 21))
        self.FirstName_entry.setObjectName("FirstName_entry")
        self.LastName_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.LastName_entry.setGeometry(QtCore.QRect(120, 40, 113, 21))
        self.LastName_entry.setObjectName("LastName_entry")
        self.Grade_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Grade_entry.setGeometry(QtCore.QRect(120, 70, 113, 21))
        self.Grade_entry.setObjectName("Grade_entry")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 70, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 420, 241, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 621, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.insert_data_btn.setText(_translate("MainWindow", "Insert"))
        self.update_data_btn.setText(_translate("MainWindow", "Update"))
        self.delete_data_btn.setText(_translate("MainWindow", "Delete"))
        self.label.setText(_translate("MainWindow", "First Name:"))
        self.label_2.setText(_translate("MainWindow", "Last Name:"))
        self.label_3.setText(_translate("MainWindow", "Grade:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First_Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Last_Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Grade"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))


