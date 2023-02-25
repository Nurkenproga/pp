#Write a Python program to convert degree to radian.
from math import *
def convert(a):
   
    return(pi * a / 180)


a = int(input("Input degree:"))
print("Output radian:",convert(a))