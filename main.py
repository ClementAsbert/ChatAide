# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets

class Chat(QtWidgets.QMainWindow):
    def __init__(self, title = "Default", parent = None):
        super(Chat, self).__init__(parent)
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._initSlotButton()
        
        
    def _initSlotButton (self):
        self.ui.envoyer.clicked.connect(self.textEnvoyer)

    def textEnvoyer(self):
        msg = self.ui.textUtilisateur.toPlainText()
        print()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Chat()
    w.show()
    sys.exit(app.exec_())

        


