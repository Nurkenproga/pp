#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

with open('row.txt', 'r', encoding="utf-8") as file:
    text = file.read()

Pattern = "a{2-3}b"

t = re.findall(Pattern, text)

print(t)