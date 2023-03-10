import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("x: " + self.x)
        print("y: " + self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        print(math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2))

a = Point(2, 4)
b = Point(4, 5)

a.dist(b)