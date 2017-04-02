This code is written in python 3.5. 

rename_files.py

This script is to remove initial numbers present at the begining of many files within a folder.

Important methods to note - os.listdir("path"), 
os.rename(src, dest), 
bytes.maketrans(b"present digits", b"to be replaced with")
string.translate()