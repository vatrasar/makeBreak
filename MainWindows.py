# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#MainWindow{\n"
"background:rgb(85, 87, 83);\n"
"}\n"
"#centralwidget{\n"
"background:rgb(85, 87, 83);\n"
"}\n"
"\n"
"QLabel{\n"
"color:rgb(13, 198, 86);\n"
"font-size:30px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background:rgb(233, 185, 110);\n"
"font-size:19px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.end = QtWidgets.QPushButton(self.centralwidget)
        self.end.setGeometry(QtCore.QRect(350, 350, 131, 51))
        self.end.setObjectName("end")
        self.btnStartWork = QtWidgets.QPushButton(self.centralwidget)
        self.btnStartWork.setGeometry(QtCore.QRect(310, 250, 211, 61))
        self.btnStartWork.setObjectName("btnStartWork")
        self.labInfo = QtWidgets.QLabel(self.centralwidget)
        self.labInfo.setGeometry(QtCore.QRect(220, 100, 501, 61))
        self.labInfo.setObjectName("labInfo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.end.setText(_translate("MainWindow", "End"))
        self.btnStartWork.setText(_translate("MainWindow", "Rozpocznij prace"))
        self.labInfo.setText(_translate("MainWindow", "Czas do zakończenia przerwy:"))
