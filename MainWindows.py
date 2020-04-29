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
        MainWindow.resize(649, 502)
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labInfo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.labInfo.sizePolicy().hasHeightForWidth())
        self.labInfo.setSizePolicy(sizePolicy)
        self.labInfo.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.labInfo.setObjectName("labInfo")
        self.verticalLayout.addWidget(self.labInfo)
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setContentsMargins(200, -1, 200, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnStartWork = QtWidgets.QPushButton(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStartWork.sizePolicy().hasHeightForWidth())
        self.btnStartWork.setSizePolicy(sizePolicy)
        self.btnStartWork.setMaximumSize(QtCore.QSize(16777215, 70))
        self.btnStartWork.setBaseSize(QtCore.QSize(0, 0))
        self.btnStartWork.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnStartWork.setObjectName("btnStartWork")
        self.verticalLayout_2.addWidget(self.btnStartWork)
        self.verticalLayout.addWidget(self.verticalWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labInfo.setText(_translate("MainWindow", "Czas do zakończenia przerwy:"))
        self.btnStartWork.setText(_translate("MainWindow", "Rozpocznij prace"))
