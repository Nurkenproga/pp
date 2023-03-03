#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

with open('row.txt', 'r', encoding="utf-8") as file:
    text = file.read()

Pattern = "а.*б"

t = re.findall(Pattern, text)

print(t)