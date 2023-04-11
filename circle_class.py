import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


circle = Circle(90)
print("Circle area: ", circle.area())
print("Circle perimeter: ", circle.perimeter())