# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_confirm(object):
    def setupUi(self, confirm):
        confirm.setObjectName("confirm")
        confirm.resize(240, 318)
        self.buttonBox = QtWidgets.QDialogButtonBox(confirm)
        self.buttonBox.setGeometry(QtCore.QRect(10, 270, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(confirm)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 10, 101, 256))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label2_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label2_2.setFont(font)
        self.label2_2.setText("")
        self.label2_2.setObjectName("label2_2")
        self.gridLayout.addWidget(self.label2_2, 1, 0, 1, 1)
        self.label8_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label8_2.setFont(font)
        self.label8_2.setText("")
        self.label8_2.setObjectName("label8_2")
        self.gridLayout.addWidget(self.label8_2, 7, 0, 1, 1)
        self.label1_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label1_2.setFont(font)
        self.label1_2.setText("")
        self.label1_2.setObjectName("label1_2")
        self.gridLayout.addWidget(self.label1_2, 0, 0, 1, 1)
        self.label4_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label4_2.setFont(font)
        self.label4_2.setText("")
        self.label4_2.setObjectName("label4_2")
        self.gridLayout.addWidget(self.label4_2, 3, 0, 1, 1)
        self.label9_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label9_2.setFont(font)
        self.label9_2.setText("")
        self.label9_2.setObjectName("label9_2")
        self.gridLayout.addWidget(self.label9_2, 8, 0, 1, 1)
        self.label7_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label7_2.setFont(font)
        self.label7_2.setText("")
        self.label7_2.setObjectName("label7_2")
        self.gridLayout.addWidget(self.label7_2, 6, 0, 1, 1)
        self.label3_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label3_2.setFont(font)
        self.label3_2.setText("")
        self.label3_2.setObjectName("label3_2")
        self.gridLayout.addWidget(self.label3_2, 2, 0, 1, 1)
        self.label5_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label5_2.setFont(font)
        self.label5_2.setText("")
        self.label5_2.setObjectName("label5_2")
        self.gridLayout.addWidget(self.label5_2, 4, 0, 1, 1)
        self.label6_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label6_2.setFont(font)
        self.label6_2.setText("")
        self.label6_2.setObjectName("label6_2")
        self.gridLayout.addWidget(self.label6_2, 5, 0, 1, 1)
        self.label10_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label10_2.setFont(font)
        self.label10_2.setText("")
        self.label10_2.setObjectName("label10_2")
        self.gridLayout.addWidget(self.label10_2, 9, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(confirm)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 92, 256))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label1 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1)
        self.label2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.verticalLayout.addWidget(self.label2)
        self.label3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.verticalLayout.addWidget(self.label3)
        self.label4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.verticalLayout.addWidget(self.label4)
        self.label5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.verticalLayout.addWidget(self.label5)
        self.label6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.verticalLayout.addWidget(self.label6)
        self.label7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label7.setFont(font)
        self.label7.setObjectName("label7")
        self.verticalLayout.addWidget(self.label7)
        self.label8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label8.setFont(font)
        self.label8.setObjectName("label8")
        self.verticalLayout.addWidget(self.label8)
        self.label9 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label9.setFont(font)
        self.label9.setObjectName("label9")
        self.verticalLayout.addWidget(self.label9)
        self.label10 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label10.setFont(font)
        self.label10.setObjectName("label10")
        self.verticalLayout.addWidget(self.label10)

        self.retranslateUi(confirm)
        self.buttonBox.accepted.connect(confirm.accept)
        self.buttonBox.rejected.connect(confirm.reject)
        QtCore.QMetaObject.connectSlotsByName(confirm)

    def retranslateUi(self, confirm):
        _translate = QtCore.QCoreApplication.translate
        confirm.setWindowTitle(_translate("confirm", "confirm"))
        self.label1.setText(_translate("confirm", "รหัสพนักงาน"))
        self.label2.setText(_translate("confirm", "Line"))
        self.label3.setText(_translate("confirm", "Shift"))
        self.label4.setText(_translate("confirm", "KANBAN ID"))
        self.label5.setText(_translate("confirm", "Part No."))
        self.label6.setText(_translate("confirm", "Part ID"))
        self.label7.setText(_translate("confirm", "Select Date :"))
        self.label8.setText(_translate("confirm", "Select Time : "))
        self.label9.setText(_translate("confirm", "จำนวนที่ต้องการ"))
        self.label10.setText(_translate("confirm", "เริ่มที่"))
