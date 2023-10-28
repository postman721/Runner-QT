
#### Runner-QT is a simple Python application that presents a graphical user interface to execute commands or launch applications on a Linux system. The program is built using the PyQt5 framework and provides a minimalistic, modern interface for entering commands or application names.


Features

    Simple and intuitive graphical user interface.
    Checks for the existence of a program before trying to execute it.
    Provides error messages to the user if a command fails or if the program doesn't exist.
    Modern and stylish look.
    Can be easily closed using the Escape key with traditional way of pressing the close button.
    Automatically closes if a program is found and executed by the system.

Dependencies

To use run.py, the following packages are required:

python3
python3-pyqt5

For Debian-based distributions (like Ubuntu), you can install these dependencies using:


		sudo apt-get update
		sudo apt-get install python3 python3-pyqt5

Usage

    Ensure that the script has executable permissions:


		chmod +x run.py

Run the script:

		./run.py
OR

		python3 run.py

    Enter the command or application name in the presented text field and press Enter to execute.
    If the entered command or application name is invalid or doesn't exist, an error message will be displayed.

##### Runner-QT v.8 Copyright (c) 2017 JJ Posti <techtimejourney.net> This program comes with ABSOLUTELY NO WARRANTY;  for details see: http://www.gnu.org/copyleft/gpl.html.  This is free software, and you are welcome to redistribute it under  GPL Version 2, June 1991")
