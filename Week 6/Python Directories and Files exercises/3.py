#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

import os
 
a =  'C://Users//nurke//OneDrive//Рабочий стол//гпа 4.00//pp2//for github//Week 6'

print(os.path.exists(a))
print(os.path.basename(a))
print(os.path.dirname(a))
