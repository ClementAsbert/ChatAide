# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from mainwindow import Ui_MainWindow
from Utilisateur import Utilisateur
from PyQt5 import QtWidgets

class Chat(QtWidgets.QMainWindow):
    def __init__(self, title = "Default", parent = None):
        super(Chat, self).__init__(parent)
        self.main = QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.utilisateur = Utilisateur()
        self.ui.setupUi(self)
        self._initSlotButton()
        
        
    def _initSlotButton (self):
        self.ui.envoyer.clicked.connect(self.Envoyer)


    def Envoyer(self):
        msg = self.ui.textUtilisateur.toPlainText()
        self.ui.labelUtilisateur.setText(self.utilisateur.name)
        self.ui.textEdit.append(self.ui.labelUtilisateur.text())
        self.ui.textEdit.insertPlainText(" > ")
        self.ui.textEdit.append(msg)
        self.ui.textEdit.append("")
        self.ui.textUtilisateur.clear()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Chat()
    w.show()
    sys.exit(app.exec_())

        


