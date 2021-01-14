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
        self.utilisateur = Utilisateur("Thierry","CE1")
        self.bot = Bot()
        self.ui.setupUi(self)
        self._initSlotButton()
        
        
        
        


        
    def connectDB(self):
        """Connection à la base de donnée Local"""

        try : 
            self.db = mdb.connect('localhost', 'root', 'root', 'chatbot')
            self.cursor = self.db.cursor()
            QMessageBox.about(self, 'Connexion', 'Successfully Connected to database')
            
        except mdb.Error as e :
            QMessageBox.about(self, 'Connexion', 'Unable to connect to the database')
            sys.exit(1)

    


    def _initSlotButton (self):
        """Initialise les Slots"""
        self.ui.envoyer.clicked.connect(self.Envoyer)
        self.ui.textUtilisateur.returnPressed.connect(self.Envoyer)
        #self.salutationBot()
       


    def Envoyer(self):
        """Envoie le message tapé par l'utilisateur"""
        

        self.msg = self.ui.textUtilisateur.text()   #récupération du texte dans la textbox
        
        """Mise en forme général"""
        self.ui.textEdit.setFontPointSize(16)       
        self.ui.textEdit.setFontWeight(1000)
        self.ui.textEdit.setTextColor(QtGui.QColor(255,255,255))    #Mise en forme du texte en blanc
        
        """Mise en forme de la bulle utilisateur"""
        self.ui.textEdit.setAlignment(Qt.AlignRight)                #Alignement du texte à droite
        self.ui.textEdit.setTextBackgroundColor(QtGui.QColor(84,130,53))#Fond en vert
        
        if self.msg == "":
            self.msg = "..."
        self.ui.textEdit.append(self.msg)   #copie du message dans la bulle
        self.ui.textEdit.append("")         #Mise en forme des bulles
        
        self.ui.textUtilisateur.clear() #effacement de la textbox
        
        """Réponse du bot"""
        
        self.respondBot()



    def respondBot(self):
        """ Envoi la réponsse du bot en fonction de la demande de l'utilisateur"""

        rsp = ""

        """Mise en forme de la réponse du bot"""
        self.ui.textEdit.setAlignment(Qt.AlignLeft)
        self.ui.textEdit.setTextBackgroundColor(QtGui.QColor(68,114,196))
        #met la chaine de caractère en minuscule pour ne pas tenir compte de la casse"
        self.msg = self.msg.lower()

        rsp = self.bot.respond(self.msg,self.cursor,self.utilisateur)
        self.ui.textEdit.append(rsp)
        self.ui.textEdit.append("")

    def salutationBot(self):
        """Mise en forme de la réponse du bot"""
        self.ui.textEdit.setFontPointSize(16)       
        self.ui.textEdit.setFontWeight(1000)
        self.ui.textEdit.setTextColor(QtGui.QColor(255,255,255))    #Mise en forme du texte en blanc
        self.ui.textEdit.setAlignment(Qt.AlignLeft)
        self.ui.textEdit.setTextBackgroundColor(QtGui.QColor(68,114,196))
            
        rsp = "Salut "+self.utilisateur.name+", je m'appelle ChatAide et je suis là pour t'aider. Demande moi une matière parmis laquelle tu voudrait t'améliorer."
        self.ui.textEdit.append(rsp)
        self.ui.textEdit.append("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Chat()
    w.setWindowTitle(w.utilisateur.name+' - '+w.utilisateur.niveau)
    w.show()
    w.connectDB()
    w.salutationBot()

    sys.exit(app.exec_())




