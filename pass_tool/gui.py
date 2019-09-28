# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 577)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.caesarGo = QtWidgets.QPushButton(Form)
        self.caesarGo.setObjectName("caesarGo")
        self.verticalLayout_2.addWidget(self.caesarGo)
        self.caeserEdit = QtWidgets.QLineEdit(Form)
        self.caeserEdit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.caeserEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.caeserEdit.setObjectName("caeserEdit")
        self.verticalLayout_2.addWidget(self.caeserEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.subtractBtn = QtWidgets.QToolButton(Form)
        self.subtractBtn.setObjectName("subtractBtn")
        self.horizontalLayout_2.addWidget(self.subtractBtn)
        self.plusBtn = QtWidgets.QToolButton(Form)
        self.plusBtn.setObjectName("plusBtn")
        self.horizontalLayout_2.addWidget(self.plusBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.inputEdit = QtWidgets.QTextEdit(Form)
        self.inputEdit.setObjectName("inputEdit")
        self.horizontalLayout.addWidget(self.inputEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.resultEdit = QtWidgets.QTextEdit(Form)
        self.resultEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.resultEdit.setObjectName("resultEdit")
        self.verticalLayout.addWidget(self.resultEdit)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.plusBtn.clicked.connect(Form.plusBtnClicked)
        self.subtractBtn.clicked.connect(Form.subBtnClicked)
        self.pushButton_3.clicked.connect(Form.b64en)
        self.pushButton.clicked.connect(Form.b64de)
        self.pushButton_2.clicked.connect(self.inputEdit.clear)
        self.pushButton_2.clicked.connect(self.resultEdit.clear)
        self.caesarGo.clicked.connect(Form.caesarBtnClicked)
        self.pushButton_4.clicked.connect(Form.changeBtnClicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pass_Tool"))
        self.caesarGo.setText(_translate("Form", "凯撒"))
        self.caeserEdit.setText(_translate("Form", "13"))
        self.subtractBtn.setText(_translate("Form", "-"))
        self.plusBtn.setText(_translate("Form", "+"))
        self.pushButton_3.setText(_translate("Form", "base64加密"))
        self.pushButton.setText(_translate("Form", "base64解密"))
        self.pushButton_2.setText(_translate("Form", "清空数据"))
        self.pushButton_4.setText(_translate("Form", "数据交换"))
        self.label.setText(_translate("Form", "Password tool v1.2 By Jerrita"))

import ic_rc
