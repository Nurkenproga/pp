#Write a Python program to drop microseconds from datetime.


from datetime import * 

today = datetime.now()
today = str(today)
a = today.split(".")
print(a[0])
