# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisUI(object):
    def setupUi(self, jarvisUI):
        jarvisUI.setObjectName("jarvisUI")
        jarvisUI.resize(1210, 875)
        self.centralwidget = QtWidgets.QWidget(jarvisUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1211, 831))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("livegui.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1080, 770, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(950, 770, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -30, 431, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("initiating.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(520, 10, 340, 61))
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"font-size:20px;\n"
"color:white;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(860, 10, 341, 61))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"font-size:20px;\n"
"color:white;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        jarvisUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(jarvisUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1210, 26))
        self.menubar.setObjectName("menubar")
        jarvisUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(jarvisUI)
        self.statusbar.setObjectName("statusbar")
        jarvisUI.setStatusBar(self.statusbar)

        self.retranslateUi(jarvisUI)
        QtCore.QMetaObject.connectSlotsByName(jarvisUI)

    def retranslateUi(self, jarvisUI):
        _translate = QtCore.QCoreApplication.translate
        jarvisUI.setWindowTitle(_translate("jarvisUI", "MainWindow"))
        self.pushButton.setText(_translate("jarvisUI", "RUN"))
        self.pushButton_2.setText(_translate("jarvisUI", "STOP"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisUI = QtWidgets.QMainWindow()
    ui = Ui_jarvisUI()
    ui.setupUi(jarvisUI)
    jarvisUI.show()
    sys.exit(app.exec_())
'''