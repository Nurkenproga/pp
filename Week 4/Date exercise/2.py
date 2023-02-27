#Write a Python program to print yesterday, today, tomorrow.
from datetime import * 

print("Yesterday:",date.today() - timedelta(days = 1))
print("Today:",date.today())
print("Tommorow:",date.today() + timedelta(days = 1))