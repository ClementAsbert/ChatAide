import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class util(QWidget):

    

    def __init__(self):
        super().__init__()
        self.title = 'Profil'
        self.initUI()
        self.nom=""
        self.niveau=""
        
        
    
    def initUI(self):
        self.setWindowTitle(self.title)
        
        # Create widget
        self.resize(300,150)
        #self.setMinimumSize(300,100)
        #self.setMaximumSize(300,100)
        self.setStyleSheet("background-color:rgb(191,191,191);")
        
        #Label Nom
        self.Nom = QLabel(self)
        self.Nom.setText("Nom")
        self.Nom.move(50, 25)

        #Premiere textbox
        self.textNom = QtWidgets.QLineEdit(self)
        self.textNom.setGeometry(QtCore.QRect(90, 20, 200, 20))
        self.textNom.setObjectName("textNom")
        self.textNom.setStyleSheet("background-color: white;"
        "border-radius : 1px")


        #Label Nom
        self.Nom = QLabel(self)
        self.Nom.setText("Classe")
        self.Nom.move(50, 65)

        #Deuxieme textbox
        self.textNiveau = QtWidgets.QLineEdit(self)
        self.textNiveau.setGeometry(QtCore.QRect(90, 60, 200, 20))
        self.textNiveau.setObjectName("textNiveau")
        self.textNiveau.setStyleSheet("background-color: white;"
        "border-radius : 1px")
        
        self.button = QPushButton('OK', self)
        self.button.clicked.connect(self.clickMethod)
        self.button.resize(60,32)
        self.button.move(90, 100)        

        self.show()

    def clickMethod(self):
       self.nom = self.textNom.text()
       self.niveau = self.textNiveau.text()
       self.close()

    def quitter(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = util()
    sys.exit(app.exec_()) 