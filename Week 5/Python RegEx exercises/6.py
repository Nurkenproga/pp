#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

with open('row.txt', 'r', encoding="utf-8") as file:
    text = file.read()

Pattern = "\s|,"

t = re.sub(Pattern, ":", text)

print(t)