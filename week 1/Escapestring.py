#The escape character allows you to use double quotes when you normally would not be allowed
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
#another
txt = "This will insert one \\ (backslash)."
print(txt)

New line
txt = "Hello\nWorld!"
print(txt) 

Carriage return
txt = "Hello\rWorld!"
print(txt) 

Tab
txt = "Hello\tWorld!"
print(txt) 

backspace
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

octal value
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

Hex
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

