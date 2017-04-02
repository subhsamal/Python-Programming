import os
import string
#from string import maketrans

def rename_files():
    #(1) get filenames from the respective folder
    file_lists = os.listdir(r"E:\Python_Programming\Udacity\prank")
    #print (file_lists)

    #(2) check the current working directory and change it to the directory
    #where the file actually resides.
    path = os.getcwd()
    print ("current directory is" + path )
    os.chdir(r"E:\Python_Programming\Udacity\prank")

    #(2) for each file, rename the filename
    transtab = bytes.maketrans(b"123456789", b"         ")
    for file_name in file_lists:
        os.rename(file_name, file_name.translate(transtab))



rename_files()
