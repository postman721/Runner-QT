#!/usr/bin/env python3
# Runner-QT v.9
# Copyright (c) 2017 JJ Posti <techtimejourney.net>
# This program comes with ABSOLUTELY NO WARRANTY;  
# For details see: http://www.gnu.org/copyleft/gpl.html.  
# This is free software, and you are welcome to redistribute it under  
# GPL Version 2, June 1991
# This version uses either PyQt5 or PyQt6 depending on, which one is used by the system. PyQt5 is served as a fallback if PyQt6 is not found.

import os
import sys
import subprocess
import shutil

# Try PyQt6 first, fall back to PyQt5
try:
    from PyQt6 import QtCore
    from PyQt6.QtCore import Qt
    from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox
    print("Using PyQt6")

    USING_QT6 = True

except ImportError:
    from PyQt5 import QtCore
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox
    print("Using PyQt5")

    USING_QT6 = False


class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)

        # A bit more modern outlook
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2E3A3A;
            }
            
            QLineEdit {
                border: 2px solid #555;
                border-radius: 15px;
                padding: 5px;
                background-color: #333;
                color: #EEE;
            }
            
            QMessageBox {
                background-color: #2E3A3A;
            }
            
            QLabel {
                color: #EEE;
            }
            
            QPushButton {
                color: #EEE;
                background-color: #555;
                border-radius: 5px;
                padding: 5px 15px;
            }
            
            QPushButton:hover {
                background-color: #666;
            }
        """)

        # Text
        self.address = QLineEdit(self)
        if USING_QT6:
            self.address.setAlignment(Qt.AlignmentFlag.AlignCenter)
        else:
            self.address.setAlignment(Qt.AlignCenter)

        self.address.setFixedSize(320, 35)
        self.address.returnPressed.connect(self.navigatex)

        # Set main window size to fit just the QLineEdit
        self.setFixedSize(self.address.width(), self.address.height())

        # Center the application on the screen
        screen_geo = QApplication.primaryScreen().geometry()
        window_geo = self.geometry()
        self.move((screen_geo.width() - window_geo.width()) // 2,
                  (screen_geo.height() - window_geo.height()) // 2)

        # Frameless window (optional)
        #if USING_QT6:
        #    self.frameless = QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint
        #else:
        #    self.frameless = QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint
        #self.setWindowFlags(self.frameless)

    def navigatex(self):
        self.location = self.address.text().split()[0]  # First word = program name

        if shutil.which(self.location):
            try:
                self.process = subprocess.Popen(self.address.text(), shell=True)
                self.close()
            except Exception as e:
                QMessageBox.critical(
                    self, "Execution Error",
                    f"Failed to execute '{self.location}': {str(e)}"
                )
        else:
            QMessageBox.critical(
                self, "Error",
                f"'{self.location}' does not exist or is not executable."
            )

    # Quit program
    def keyPressEvent(self, event):
        if USING_QT6:
            if event.key() == Qt.Key.Key_Escape:
                self.close()
        else:
            if event.key() == Qt.Key_Escape:
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec() if USING_QT6 else app.exec_())
