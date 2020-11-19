# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtSql import QSqlDatabase


class Ui_MainWindow(object): 
    """Classe de l'affichage principale avec tous les élement de l'affichage"""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 700)
        MainWindow.setMinimumSize(QtCore.QSize(640, 700))
        MainWindow.setMaximumSize(QtCore.QSize(640, 700))
        MainWindow.setStyleSheet("background-color:rgb(191,191,191);")
        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        

        #QLineEdit
        self.textUtilisateur = QtWidgets.QLineEdit(self.centralwidget)
        self.textUtilisateur.setGeometry(QtCore.QRect(13, 630, 521, 41))
        self.textUtilisateur.setObjectName("textUtilisateur")
        self.textUtilisateur.setStyleSheet("background-color: white;"
        "border-radius : 15px")

        #QLabel
        self.labelUtilisateur = QtWidgets.QLabel()
        self.labelUtilisateur.setObjectName("labelUtilisateur")
        self.labelBot = QtWidgets.QLabel()
        self.labelBot.setObjectName("LabelBot")

        #QButton
        self.envoyer = QtWidgets.QPushButton(self.centralwidget)
        self.envoyer.setGeometry(QtCore.QRect(540, 630, 66, 41))
        self.envoyer.setObjectName("envoyer")
        self.envoyer.setStyleSheet("background-color: rgb(255,217,102);"
        "color: Black;"
        "border-radius: 15px;")

        #QTextEdit
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(13, 20, 591, 601))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet("background-color: rgb(191,191,191);"
        "border: None;")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Connextion à la base de donnée
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        self.db.setDatabaseName("ChatBot")
        self.db.setUserName("root")
        self.db.setPassword("root")

        #Requete Sql


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.envoyer.setText(_translate("MainWindow", "Envoyer"))
