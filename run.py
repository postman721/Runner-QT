#Runner-QT v.7 Copyright (c) 2017 JJ Posti <techtimejourney.net> This program comes with ABSOLUTELY NO WARRANTY;  for details see: http://www.gnu.org/copyleft/gpl.html.  This is free software, and you are welcome to redistribute it under  GPL Version 2, June 1991")
#!/usr/bin/env python3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt  
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QToolBar
import os, sys,subprocess
from subprocess import Popen
class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
#Title & Layout	& Label	
        self.setStyleSheet("color:#ffffff; background-color:#353535;font-size: 12px;")
        self.move(QApplication.desktop().screen().rect().center()- self.rect().center())
        self.setFixedSize(340, 45)
#Make a Frameless window & Disable grip
        self.frameless = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(self.frameless)
#Text
        self.address=QLineEdit()      
        self.address.setAlignment(Qt.AlignCenter)
        self.address.setFixedSize(320, 35)
        self.address.returnPressed.connect(self.navigatex)               
#Tool & Layout
        self.tool=QToolBar()
        self.tool.addWidget(self.address)
        self.addToolBar(self.tool)
#Open program    
    def navigatex(self):
        self.location=self.address.text()
        self.process = subprocess.Popen(self.location,shell=True)
        self.close();               
#Quit program - Notice that this is the main window. We can pass the ESC event directly into it - since we only destroy/exit the Gui.
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show() 
    sys.exit(app.exec_())
