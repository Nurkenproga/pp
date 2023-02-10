class Shape:
    helper = 0

    def area(self):
        print(self.helper)


class Rectangle(Shape):
    def __init__(self, lenght, wight):
        self.lenght = lenght
        self.wight = wight
    
    def area(self):
        print(self.lenght * self.wight)

c = input()
d = input()
a = Shape()
b = Rectangle(int(c), int(d))

a.area()
b.area()