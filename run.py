#Runner-QT v.2 Copyright (c) 2017 JJ Posti <techtimejourney.net> This program comes with ABSOLUTELY NO WARRANTY;  for details see: http://www.gnu.org/copyleft/gpl.html.  This is free software, and you are welcome to redistribute it under  GPL Version 2, June 1991")
#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt  
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLineEdit, QCheckBox, QToolBar, QMenu, QMessageBox, QPushButton, QApplication
import subprocess, os, sys
class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
#Title & Layout		
        self.setWindowTitle("Runner-QT")
        self.move(QApplication.desktop().screen().rect().center()- self.rect().center())
        self.setFixedSize(540, 40)
        self.vertical = QVBoxLayout()
#Text field
        self.address=QLineEdit()
        self.address.setAlignment(Qt.AlignCenter)
        self.address.setFixedSize(440, 35)
        self.address.returnPressed.connect(self.navigatex)
#About
        self.about1 = QPushButton()
        self.about1.setObjectName("About")
        self.about1.setText("About")
        self.about1.setFixedSize(60, 35)
        self.about1.clicked.connect(self.about)              
#Toolbar & Layout
        self.toolbar=QToolBar()
        self.toolbar.addWidget(self.address)
        self.toolbar.addWidget(self.about1)
        self.addToolBar(self.toolbar)
        self.toolbar.setLayout(self.vertical)  
        self.setLayout(self.vertical)
#About messagebox
    def about(self):
        buttonReply = QMessageBox.question(self, 'Runner-QT v.2 Copyright (c) 2017 JJ Posti <techtimejourney.net>', "Runner-QT  is a dialog for running programs. The program comes with ABSOLUTELY NO WARRANTY  for details see: http://www.gnu.org/copyleft/gpl.html. This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991.\n \nRunner-QT runs programs with or without arguments (Example: firefox www.google.fi or albix", QMessageBox.Ok )
        if buttonReply == QMessageBox.Ok:
            pass
    def navigatex(self):
        location=self.address.text()
        subprocess.Popen(location, shell=True)
        self.close()                                    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show() 
    sys.exit(app.exec_())
