#Write a Python program to split a string at uppercase letters.
import re

def snake_to_camel(words):
    ans = ""
    ans += words[0]
    for i in range(1,len(words)):
        ans += words[i].capitalize()
    return ans
    


text = "my_super_var" 

words = re.split("_", text)

print(snake_to_camel(words))