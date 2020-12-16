# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from mainwindow import Ui_MainWindow
from Utilisateur import Utilisateur
from Bot import Bot
from PyQt5 import QtSql, QtWidgets
from PyQt5.QtSql import QSqlDatabase
import MySQLdb as mdb
from PyQt5.QtCore import *
from PyQt5 import QtGui
from Image import App


class Chat(QtWidgets.QMainWindow):
    def __init__(self, title = "Default", parent = None):
        super(Chat, self).__init__(parent)
        """Construteur de la classe"""
        self.main = QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.utilisateur = Utilisateur()
        self.bot = Bot()
        self.ui.setupUi(self)
        self._initSlotButton()
        self.connectDB()
        


        
    def connectDB(self):
        """Connection à la base de donnée Local"""

        try : 
            self.db = mdb.connect('localhost', 'root', 'root', 'chatbot')
            self.cursor = self.db.cursor()
            QMessageBox.about(self, 'Connextion', 'Successfully Connected to db')
            
        except mdb.Error as e :
            QMessageBox.about(self, 'Connextion', 'Not Connected Successfully')
            sys.exit(1)

    


    def _initSlotButton (self):
        """Initialise les Slots"""

        self.ui.envoyer.clicked.connect(self.Envoyer)
        self.ui.textUtilisateur.returnPressed.connect(self.Envoyer)


    def Envoyer(self):
        """Envoie le message taper par l'utilisateur"""

        #self.msg =self.utilisateur.name + " : " + self.ui.textUtilisateur.text()
        self.msg = self.ui.textUtilisateur.text()
        self.ui.textEdit.setFontPointSize(16)
        self.ui.textEdit.setFontWeight(1000)
        self.ui.textEdit.setTextColor(QtGui.QColor(255,255,255))    #Text en blanc
        self.ui.textEdit.setAlignment(Qt.AlignRight)            #Text à droite
        self.ui.textEdit.setTextBackgroundColor(QtGui.QColor(84,130,53))#Fond en vert
        self.ui.textEdit.append(self.msg)
        self.ui.textEdit.append("")
        self.ui.textUtilisateur.clear()
        self.ui.textEdit.setAlignment(Qt.AlignLeft)
        self.ui.textEdit.setTextBackgroundColor(QtGui.QColor(68,114,196))
        self.respondBot()



    def respondBot(self):
        """ Envoi la réponsse du bot en fonction de la demande de l'utilisateur"""

        rsp = ""

        #met la chaine de caractère en minuscule pour ne pas tenir compte de la casse"
        self.msg = self.msg.lower()

        #Regarde si un gros mot en contenue dans la chaine de caractère
        if self.grosmots()==True:
            rsp += "Surveille ton langage"
        #Reponsse simple du bot 
        elif "bonjour" in self.msg:
            rsp += "Bonjour comment ça va ?"

        elif "maths" in self.msg:
            self.cursor.execute("SELECT enonce FROM exercice WHERE idEx = 7;")
            data = self.cursor.fetchone()
            rsp += "%s" % data

        elif "français" in self.msg:
            self.cursor.execute("SELECT enonce FROM exercice WHERE idEx= 1;")
            data = self.cursor.fetchone()
            rsp += "%s" % data
        elif "image" in self.msg :
            self.image = App()
        else:
            rsp += " Je ne comprend pas !"
        
        self.ui.textEdit.append(rsp)
        self.ui.textEdit.append("")

    
    def grosmots(self):
        """Fonction qui gère les gros mots"""
        grm = ['girafe', 'tigre', 'singe', 'souris']
        for f in grm:
            if f in self.msg:
                return True
        return False



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Chat()
    w.show()
    sys.exit(app.exec_())

        


