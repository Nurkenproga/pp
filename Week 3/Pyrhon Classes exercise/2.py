class Shape:
    ar = 0
   
    def area(self):
        print(self.ar)

class Square(Shape):
    def __init__(self, lenght):
        self.lenght = lenght

    def area(self):
        print(self.lenght * self.lenght)

c = input()
a = Shape()
b = Square(int(c))

a.area()
b.area()