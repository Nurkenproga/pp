#Write a Python program to calculate the area of regular polygon.
from math import *
def Area(n,L):
    P = n * L
    a = L / (2 * tan(pi/n))
    return(P * a /2)


n = int(input("Input number of sides: "))
L = int(input("Input the length of a side: "))

print("The area of the polygon is:",int(Area(n,L)))