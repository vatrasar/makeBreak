# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './progress_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, 30, 20, 60)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.progress_short_interval = QtWidgets.QProgressBar(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_short_interval.sizePolicy().hasHeightForWidth())
        self.progress_short_interval.setSizePolicy(sizePolicy)
        self.progress_short_interval.setProperty("value", 24)
        self.progress_short_interval.setObjectName("progress_short_interval")
        self.verticalLayout.addWidget(self.progress_short_interval)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progress_long_interval = QtWidgets.QProgressBar(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_long_interval.sizePolicy().hasHeightForWidth())
        self.progress_long_interval.setSizePolicy(sizePolicy)
        self.progress_long_interval.setProperty("value", 24)
        self.progress_long_interval.setObjectName("progress_long_interval")
        self.verticalLayout.addWidget(self.progress_long_interval)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.btn_result = QtWidgets.QDialogButtonBox(Dialog)
        self.btn_result.setOrientation(QtCore.Qt.Horizontal)
        self.btn_result.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.btn_result.setCenterButtons(True)
        self.btn_result.setObjectName("btn_result")
        self.verticalLayout_2.addWidget(self.btn_result)

        self.retranslateUi(Dialog)
        self.btn_result.rejected.connect(Dialog.reject)
        self.btn_result.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Akutalny plan"))
        self.label_2.setText(_translate("Dialog", "Wykonanie krótkiego czasu pracy"))
        self.label.setText(_translate("Dialog", "Wykonnanie długiego czasu pracy"))
