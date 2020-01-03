#Runner-QT v.6 Copyright (c) 2017 JJ Posti <techtimejourney.net> This program comes with ABSOLUTELY NO WARRANTY;  for details see: http://www.gnu.org/copyleft/gpl.html.  This is free software, and you are welcome to redistribute it under  GPL Version 2, June 1991")
#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt  
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QToolBar, QMessageBox
import os, sys
class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
#Title & Layout	& Label	
        self.setWindowTitle("Enter program")
        self.setStyleSheet("color:#ffffff; background-color:#353535;font-size: 12px;")
        self.move(QApplication.desktop().screen().rect().center()- self.rect().center())
        self.setFixedSize(400, 36)          
#Text field
        self.address=QLineEdit()
        self.address.setStyleSheet("QLineEdit{color:#ffffff; background-color:#2a2a2a; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QLineEdit:focus{background-color:#353535;}")          
        self.address.setAlignment(Qt.AlignCenter)
        self.address.setFixedSize(340, 35)
        self.address.returnPressed.connect(self.navigatex)
#About button
        self.about1 = QPushButton()
        self.about1.setStyleSheet("QPushButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QPushButton:hover{background-color:#5c5c5c;}")  
        self.about1.setObjectName("About")
        self.about1.setText("About")
        self.about1.setFixedSize(40, 35)
        self.about1.clicked.connect(self.about)                
#Toolbar & Layout
        self.toolbar=QToolBar()
        self.toolbar.addWidget(self.address)
        self.toolbar.addWidget(self.about1)
        self.addToolBar(self.toolbar)
#About messagebox
    def about(self):
        buttonReply = QMessageBox.information(self, 'Runner-QT v.6 Copyright (c) 2017 JJ Posti <techtimejourney.net>', "Runner-QT  is a dialog for running programs. The program comes with ABSOLUTELY NO WARRANTY  for details see: http://www.gnu.org/copyleft/gpl.html. This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991.\n \nRunner-QT runs programs with or without arguments (Example: firefox www.google.fi or albix _____________________________________________________________________________________________\n\n", QMessageBox.Ok )
        if buttonReply == QMessageBox.Ok:
            pass    
#Open program    
    def navigatex(self):
        try:
            location=self.address.text()
            self.process = QtCore.QProcess()
            self.process.startDetached(str(location))
            self.close();
        except Exception as e: 
            print (e);
            self.close()
#Quit program - Notice that this is the main window. We can pass the ESC event directly into it - since we only destroy/exit the Gui.
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show() 
    sys.exit(app.exec_())
