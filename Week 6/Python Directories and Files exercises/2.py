#Write a Python program to check for access to a specified path. 
#Test the existence, readability, writability and executability of the specified path

import os

print('Exist:', os.access('C://Users//nurke//OneDrive//Рабочий стол//гпа 4.00//pp2//for github//Week 6', os.F_OK))
print('Readable:', os.access('C://Users//nurke//OneDrive//Рабочий стол//гпа 4.00//pp2//for github//Week 6', os.R_OK))
print('Writable:', os.access('C://Users//nurke//OneDrive//Рабочий стол//гпа 4.00//pp2//for github//Week 6', os.W_OK))
print('Executable:', os.access('C://Users//nurke//OneDrive//Рабочий стол//гпа 4.00//pp2//for github//Week ', os.X_OK))
