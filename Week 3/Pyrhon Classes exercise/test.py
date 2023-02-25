class Triangle:
    def line(self):
        self.a = int(input())
    def esep(self):
        print(self.a**2 * 3**(1/2) / 4)

x = Triangle()
x.line()
x.esep()