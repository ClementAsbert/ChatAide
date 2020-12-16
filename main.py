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
        self.utilisateur = Utilisateur("Thierry","CM2")
        #self.main.setWindowTitle(self.utilisateur.name);
        self.bot = Bot()
        self.ui.setupUi(self)
        self._initSlotButton()
        
        


        
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
        

        self.msg = self.ui.textUtilisateur.text()   #récupération du texte dans la textbox
        
        """Mise en forme général"""
        self.ui.textEdit.setFontPointSize(16)       
        self.ui.textEdit.setFontWeight(1000)
        self.ui.textEdit.setTextColor(QtGui.QColor(255,255,255))    #Mise en forme du texte en blanc
        
        """Mise en forme de la bulle utilisateur"""
        self.ui.textEdit.setAlignment(Qt.AlignRight)                #Alignement du texte à droite
        self.ui.textEdit.setTextBackgroundColor(QtGui.QColor(84,130,53))#Fond en vert
        
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

        #Regarde en premier si un gros mot est contenue dans la chaine de caractère
        if self.grosmots()==True:
            rsp += "Surveille ton langage"
        #Reponsse simple du bot 
        
        elif "bonjour" in self.msg:
            rsp += "Bonjour comment ça va ?"

        elif "maths" in self.msg:
            print(w.utilisateur.niveau)
            self.cursor.execute("SELECT enonce FROM exercice WHERE idMatiere = 1 AND classe = "+"'"+w.utilisateur.niveau+"'"+";") #attribue au curseur la valeur de l'exercice qui a pour matiere maths
            data = self.cursor.fetchone()       #va chercher le contenue du curseur
            self.cursor.execute("SELECT reponse FROM exercice WHERE idEx = 7;") #attribue au curseur la valeur de la réponse correspondant à l'exercice
            reponse = self.cursor.fetchone()    #va chercher le contenue du curseur
            rsp += "%s" % data
            
            if self.msg == reponse:
                rsp += "Bravo tu à trouvé"
            else :
                rsp += "Essaye encore"

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
    w.setWindowTitle(w.utilisateur.name+' - '+w.utilisateur.niveau);
    w.show()
    w.connectDB()

    sys.exit(app.exec_())

        


