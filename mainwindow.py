# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 690)
        MainWindow.setMinimumSize(QtCore.QSize(640, 690))
        MainWindow.setMaximumSize(QtCore.QSize(640, 690))
        MainWindow.setStyleSheet("background-Color: rgb(191, 191, 191);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textUtilisateur = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textUtilisateur.setGeometry(QtCore.QRect(5, 630, 531, 41))
        self.textUtilisateur.setStyleSheet("background-Color: rgb(255, 255, 255);"
        "border-radius: 15px;")
        self.textUtilisateur.setObjectName("textUtilisateur")
        self.envoyer = QtWidgets.QPushButton(self.centralwidget)
        self.envoyer.setGeometry(QtCore.QRect(550, 630, 75, 41))
        self.envoyer.setIcon(QtGui.QIcon("Send.png"))
        self.envoyer.setIconSize(QtCore.QSize(self.envoyer.size()))
        self.envoyer.setObjectName("envoyer")
        self.envoyer.setStyleSheet("Color: rgb(191, 191, 191);")
        self.listMessages = QtWidgets.QListView(self.centralwidget)
        self.listMessages.setGeometry(QtCore.QRect(5, 5, 630, 621))
        self.listMessages.setStyleSheet("background-Color: rgb(191, 191, 191);")
        self.listMessages.setObjectName("listMessages")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChatBot"))
        
