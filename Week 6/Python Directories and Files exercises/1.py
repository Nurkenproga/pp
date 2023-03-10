#Write a Python program to list only directories, files and all directories, files in a specified path.

import os

path = "C://Users//nurke//OneDrive//Рабочий стол//гпа 4.00//pp2//for github//Week 6"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
print(dir_list)