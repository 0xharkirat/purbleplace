# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 392)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 30, 1001, 351))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("\n"
"background-color: rgb(208, 208, 208);\n"
"border-radius:16px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 160, 941, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_2.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_3.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_4.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 120, 937, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setStyleSheet("background-color: rgb(149, 149, 149);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setStyleSheet("background-color: rgb(149, 149, 149);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setStyleSheet("background-color: rgb(149, 149, 149);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setStyleSheet("background-color: rgb(149, 149, 149);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(370, 240, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border-radius:0px;\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(85, 170, 127);\n"
"}\n"
"background-color: rgb(85, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "-- select base shape --"))
        self.comboBox.setItemText(1, _translate("MainWindow", "round"))
        self.comboBox.setItemText(2, _translate("MainWindow", "box"))
        self.comboBox.setItemText(3, _translate("MainWindow", "heart"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "-- select base color  --"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "choco"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "pink"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "yellow"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "-- select top color  --"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "choco"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "pink"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "yellow"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "-- select cherry  --"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "triple"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "smiley"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "heart"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "leaf"))
        self.label.setText(_translate("MainWindow", "Base Shape: "))
        self.label_4.setText(_translate("MainWindow", "Base Color:"))
        self.label_3.setText(_translate("MainWindow", "Top Color:"))
        self.label_2.setText(_translate("MainWindow", "Cherry:"))
        self.pushButton.setText(_translate("MainWindow", "Start Baking"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
