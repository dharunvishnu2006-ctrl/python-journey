class Shape:
    def area(self):
        print("Calculating area...")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle Area:", 3.14 * self.radius * self.radius)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Rectangle Area:", self.length * self.width)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print("Triangle Area:", 0.5 * self.base * self.height)

shapes = [Circle(7), Rectangle(5, 10), Triangle(6, 8)]

for shape in shapes:
    shape.area()