#Write a Python program to calculate the area of a trapezoid.
def Area(a,b,h):
    return((a+b) / 2 * h)



h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

print("Expected Output:",Area(a,b,h))
