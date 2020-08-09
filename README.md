# Runner-QT
Runner-QT is a program launcher dialog for Linux/Unix.

![screen](https://user-images.githubusercontent.com/29865797/89737715-dbb31280-da7b-11ea-80d0-9548fc5d8a64.jpg)

Runner-QT v.7 has 40 lines of code. The program has a new outlook via CSS, which brings colours  and element highlighting. 

#Runner-QT v.4 Copyright (c) 2017 JJ Posti <techtimejourney.net>
This program comes with ABSOLUTELY NO WARRANTY;
for details see: http://www.gnu.org/copyleft/gpl.html.
This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991″)

Changes in v.4:
When Runner-QT exits(from v.4 onwards) it prints an error to the cli if a program it tried to execute did not exist. Runner-QT v.4 quits with an ESC key - automatic exit functionality remains as a feature.

Dependencies:

sudo apt-get install python-pyqt5 python python3

Usage information:

Runner-QT will try to execute every command you write – via Python´s subprocess.Popen. If the command does not exist on the system then the program just closes and you can restart it. If the command exists then the program or argument will get executed. Security note. Be careful about what you type since Runner-QT accepts shell arguments. Never write something like: rm -r this_path, unless you are absolutely certain what you are doing.

Executing:

Run the program: python /home/some_person/some_folder/something.py

If needed make the program executable with: chmod +x /home/some_person/some_folder/something.py

__________________________
Original post is at:
http://www.techtimejourney.net/runner-qt-v-3/
