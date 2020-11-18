# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from mainwindow import Ui_MainWindow
from Utilisateur import Utilisateur
from Bot import Bot
from PyQt5 import QtWidgets

class Chat(QtWidgets.QMainWindow):
    def __init__(self, title = "Default", parent = None):
        super(Chat, self).__init__(parent)
        self.main = QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.utilisateur = Utilisateur()
        self.bot = Bot()
        self.ui.setupUi(self)
        self._initSlotButton()
        
        
    def _initSlotButton (self):
        self.ui.envoyer.clicked.connect(self.Envoyer)
        self.ui.textUtilisateur.returnPressed.connect(self.Envoyer)

    def Envoyer(self):
        self.msg =self.utilisateur.name + " : " + self.ui.textUtilisateur.text()
        self.ui.textEdit.append(self.msg)
        self.ui.textEdit.append("")
        self.ui.textUtilisateur.clear()
        self.respondBot()



    def respondBot(self):
        rsp = self.bot.name + " : "

        if "Bonjour" in self.msg:
            rsp += "Bonjour comment ça va ?"
        elif "maths" in self.msg:
            rsp += "Voici les exos de maths !"
            self.image()
        else:
            rsp += " Je ne comprend pas !"
        
        self.ui.textEdit.append(rsp)
        self.ui.textEdit.append("")

        
    def image(self):
        self.img = self.ui.textEdit.toHtml() + "<img src = \"../img/maths.png\" alt =\"\"/>"
        self.ui.textEdit.setHtml(self.img)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Chat()
    w.show()
    sys.exit(app.exec_())

        


