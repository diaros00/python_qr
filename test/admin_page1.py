# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_page1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(702, 530)
        Dialog.setMaximumSize(QtCore.QSize(800, 600))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setModal(True)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 661, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_16.setGeometry(QtCore.QRect(50, 770, 121, 31))
        self.lineEdit_16.setAutoFillBackground(False)
        self.lineEdit_16.setStyleSheet("")
        self.lineEdit_16.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_16.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_17.setGeometry(QtCore.QRect(250, 770, 121, 31))
        self.lineEdit_17.setAutoFillBackground(False)
        self.lineEdit_17.setStyleSheet("")
        self.lineEdit_17.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_17.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_18.setGeometry(QtCore.QRect(470, 770, 121, 31))
        self.lineEdit_18.setAutoFillBackground(False)
        self.lineEdit_18.setStyleSheet("")
        self.lineEdit_18.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_18.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 70, 421, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.table_part_kanban = QtWidgets.QTextBrowser(self.layoutWidget)
        self.table_part_kanban.setObjectName("table_part_kanban")
        self.horizontalLayout.addWidget(self.table_part_kanban)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 360, 421, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_Part_ID = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_Part_ID.setAutoFillBackground(False)
        self.lineEdit_Part_ID.setStyleSheet("")
        self.lineEdit_Part_ID.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_Part_ID.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_Part_ID.setObjectName("lineEdit_Part_ID")
        self.horizontalLayout_3.addWidget(self.lineEdit_Part_ID)
        self.lineEdit_Part_NO = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_Part_NO.setAutoFillBackground(False)
        self.lineEdit_Part_NO.setStyleSheet("")
        self.lineEdit_Part_NO.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_Part_NO.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_Part_NO.setObjectName("lineEdit_Part_NO")
        self.horizontalLayout_3.addWidget(self.lineEdit_Part_NO)
        self.lineEdit_Kanban_ID = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_Kanban_ID.setAutoFillBackground(False)
        self.lineEdit_Kanban_ID.setStyleSheet("")
        self.lineEdit_Kanban_ID.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_Kanban_ID.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_Kanban_ID.setObjectName("lineEdit_Kanban_ID")
        self.horizontalLayout_3.addWidget(self.lineEdit_Kanban_ID)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(260, 390, 171, 25))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_part_kanban_Add = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_part_kanban_Add.setObjectName("pushButton_part_kanban_Add")
        self.horizontalLayout_4.addWidget(self.pushButton_part_kanban_Add)
        self.pushButton_part_kanban_Del = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_part_kanban_Del.setObjectName("pushButton_part_kanban_Del")
        self.horizontalLayout_4.addWidget(self.pushButton_part_kanban_Del)
        self.search_part_kanban = QtWidgets.QLineEdit(self.tab)
        self.search_part_kanban.setGeometry(QtCore.QRect(10, 40, 421, 20))
        self.search_part_kanban.setObjectName("search_part_kanban")
        self.lineEdit_Line = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Line.setGeometry(QtCore.QRect(440, 361, 201, 20))
        self.lineEdit_Line.setAutoFillBackground(False)
        self.lineEdit_Line.setStyleSheet("")
        self.lineEdit_Line.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_Line.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_Line.setObjectName("lineEdit_Line")
        self.table_line = QtWidgets.QTextBrowser(self.tab)
        self.table_line.setGeometry(QtCore.QRect(440, 70, 201, 281))
        self.table_line.setObjectName("table_line")
        self.search_line = QtWidgets.QLineEdit(self.tab)
        self.search_line.setGeometry(QtCore.QRect(440, 40, 201, 20))
        self.search_line.setObjectName("search_line")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(470, 390, 171, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Line_Add = QtWidgets.QPushButton(self.widget)
        self.pushButton_Line_Add.setObjectName("pushButton_Line_Add")
        self.horizontalLayout_2.addWidget(self.pushButton_Line_Add)
        self.pushButton_Line_Del = QtWidgets.QPushButton(self.widget)
        self.pushButton_Line_Del.setObjectName("pushButton_Line_Del")
        self.horizontalLayout_2.addWidget(self.pushButton_Line_Del)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 10, 341, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 10, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 631, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(520, 390, 121, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(10, 50, 631, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 20, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.raise_()
        self.label_2.raise_()
        self.pushButton_3.raise_()

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Program Qrcode Generator"))
        self.label_2.setText(_translate("Dialog", "ADMIN PAGE"))
        self.label.setText(_translate("Dialog", "Edit Data"))
        self.lineEdit_16.setPlaceholderText(_translate("Dialog", "PART ID"))
        self.lineEdit_17.setPlaceholderText(_translate("Dialog", "PART ID"))
        self.lineEdit_18.setPlaceholderText(_translate("Dialog", "PART ID"))
        self.lineEdit_Part_ID.setPlaceholderText(_translate("Dialog", "PART ID"))
        self.lineEdit_Part_NO.setPlaceholderText(_translate("Dialog", "PART NO"))
        self.lineEdit_Kanban_ID.setPlaceholderText(_translate("Dialog", "KABAN ID"))
        self.pushButton_part_kanban_Add.setText(_translate("Dialog", "Add"))
        self.pushButton_part_kanban_Del.setText(_translate("Dialog", "Delete"))
        self.search_part_kanban.setPlaceholderText(_translate("Dialog", "Search . . ."))
        self.lineEdit_Line.setPlaceholderText(_translate("Dialog", "LINE"))
        self.search_line.setPlaceholderText(_translate("Dialog", "Search . . ."))
        self.pushButton_Line_Add.setText(_translate("Dialog", "Add"))
        self.pushButton_Line_Del.setText(_translate("Dialog", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Edit Data"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Add Employee ID"))
        self.pushButton_2.setText(_translate("Dialog", "Add"))
        self.label_3.setText(_translate("Dialog", "ADD Employee ID"))
        self.pushButton_6.setText(_translate("Dialog", "Delete"))
        self.lineEdit_9.setPlaceholderText(_translate("Dialog", "Search . . ."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Add admin"))
        self.pushButton_3.setText(_translate("Dialog", "back"))
