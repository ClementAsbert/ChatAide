
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class App(QWidget):

    def __init__(self,image):
        super().__init__()
        self.title = 'PyQt5 image'
        self.image = image
        self.initUI()
        
    
    def initUI(self):
        self.setWindowTitle(self.title)
        
        
    
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap(self.image)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.setMinimumSize(pixmap.width(),pixmap.height())
        self.setMaximumSize(pixmap.width(),pixmap.height())
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())