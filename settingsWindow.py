# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(532, 187)
        Dialog.setStyleSheet("QLabel{\n"
"font-size:20px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spin_time_for_long_break = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_time_for_long_break.sizePolicy().hasHeightForWidth())
        self.spin_time_for_long_break.setSizePolicy(sizePolicy)
        self.spin_time_for_long_break.setMinimum(1)
        self.spin_time_for_long_break.setMaximum(1000)
        self.spin_time_for_long_break.setObjectName("spin_time_for_long_break")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spin_time_for_long_break)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spin_shor_break_time = QtWidgets.QSpinBox(Dialog)
        self.spin_shor_break_time.setMinimum(1)
        self.spin_shor_break_time.setMaximum(1000)
        self.spin_shor_break_time.setObjectName("spin_shor_break_time")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spin_shor_break_time)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spin_time_to_short_break = QtWidgets.QSpinBox(Dialog)
        self.spin_time_to_short_break.setMinimum(1)
        self.spin_time_to_short_break.setMaximum(1000)
        self.spin_time_to_short_break.setObjectName("spin_time_to_short_break")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spin_time_to_short_break)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spin_time_to_long_break = QtWidgets.QSpinBox(Dialog)
        self.spin_time_to_long_break.setMinimum(1)
        self.spin_time_to_long_break.setMaximum(1000)
        self.spin_time_to_long_break.setObjectName("spin_time_to_long_break")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spin_time_to_long_break)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ustawienia"))
        self.label.setText(_translate("Dialog", "Czas długiej przerwy(minuty)"))
        self.label_2.setText(_translate("Dialog", "Czas krótkiej przerwy(sekundy)"))
        self.label_3.setText(_translate("Dialog", "Czas pomiędzy krótkimi przerwam(minuty)"))
        self.label_4.setText(_translate("Dialog", "Czas pomiędzy długimi przerwami(minuty)"))
