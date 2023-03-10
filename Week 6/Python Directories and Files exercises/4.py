#Write a Python program to count the number of lines in a text file.
import os

with open("text.txt", "r") as file:
    line = file.readlines()
    print(line)
