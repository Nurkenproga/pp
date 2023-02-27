#Write a Python program to calculate two date difference in seconds.

from datetime import *

a = datetime.now()
b = datetime.now() - timedelta(days = 10)

c = a - b 
print(c.total_seconds())