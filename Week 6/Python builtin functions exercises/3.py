#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
a = list(input())
b = list(reversed(a))
if b == a:
    print("Yes")
else:
    print("NO")