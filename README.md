# Runner-QT
Runner-QT is a program launcher dialog for Linux/Unix.

![run3](https://user-images.githubusercontent.com/29865797/29373412-d973584c-82b6-11e7-8cd0-da8f58903d4a.jpg)

Runner-QT v.3 has 49 lines of code. The program has a new outlook via CSS, which brings colours  and element highlighting. 

#Runner-QT v.3 Copyright (c) 2017 JJ Posti <techtimejourney.net>
This program comes with ABSOLUTELY NO WARRANTY;
for details see: http://www.gnu.org/copyleft/gpl.html.
This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991″)

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
