#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

with open('row.txt', 'r', encoding="utf-8") as file:
    text = file.read()

Pattern = "[А-Я][а-я]+"

t = re.findall(Pattern, text)

print(t)