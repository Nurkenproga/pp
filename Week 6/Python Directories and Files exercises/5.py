#Write a Python program to write a list to a file.
items = ["I", "am", "KBTU", "student"]
file = open('sample.txt','w')
for item in items:
	file.write(item+"\n")
file.close()