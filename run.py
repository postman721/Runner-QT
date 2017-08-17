#Runner-QT v.3.0.1 Copyright (c) 2017 JJ Posti <techtimejourney.net> This program comes with ABSOLUTELY NO WARRANTY;  for details see: http://www.gnu.org/copyleft/gpl.html.  This is free software, and you are welcome to redistribute it under  GPL Version 2, June 1991")
#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt  
from PyQt5.QtWidgets import *
import subprocess, os, sys
from subprocess import Popen
class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
#Title & Layout		
        self.setWindowTitle("Runner-QT")
        self.setStyleSheet("color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;")
        self.move(QApplication.desktop().screen().rect().center()- self.rect().center())
        self.setFixedSize(540, 43)
#Text field
        self.address=QLineEdit()
        self.address.setStyleSheet("QLineEdit{color:#ffffff; background-color:#2a2a2a; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QLineEdit:focus{background-color:#5c5c5c;}")          
        self.address.setAlignment(Qt.AlignCenter)
        self.address.setFixedSize(440, 35)
        self.address.returnPressed.connect(self.navigatex)
#About
        self.about1 = QPushButton()
        self.about1.setStyleSheet("QPushButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QPushButton:hover{background-color:#5c5c5c;}")  
        self.about1.setObjectName("About")
        self.about1.setText("About")
        self.about1.setFixedSize(60, 35)
        self.about1.clicked.connect(self.about)                
#Toolbar & Layout
        self.toolbar=QToolBar()
        self.toolbar.addWidget(self.address)
        self.toolbar.addWidget(self.about1)
        self.addToolBar(self.toolbar)
#About messagebox
    def about(self):
        buttonReply = QMessageBox.information(self, 'Runner-QT v.3.0.1 Copyright (c) 2017 JJ Posti <techtimejourney.net>', "Runner-QT  is a dialog for running programs. The program comes with ABSOLUTELY NO WARRANTY  for details see: http://www.gnu.org/copyleft/gpl.html. This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991.\n \nRunner-QT runs programs with or without arguments (Example: firefox www.google.fi or albix", QMessageBox.Ok )
        if buttonReply == QMessageBox.Ok:
            pass
    def navigatex(self):
        location=self.address.text()
        run=subprocess.Popen(location, shell=True)
        self.close()                                    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show() 
    sys.exit(app.exec_())
