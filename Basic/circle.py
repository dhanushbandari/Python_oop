class Circle:
    pi = 3.14159   # Class attribute

    def __init__(self, radius):
        self.radius = radius   # Instance attribute

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)   # Alternative constructor

    @staticmethod
    def info():
        print("Circle calculations are useful in geometry, engineering, and physics.")

    def calculate_area(self):
        return Circle.pi * (self.radius ** 2)
c1 = Circle(5)
print("Area using radius:", c1.calculate_area())
c2 = Circle.from_diameter(10)
print("Area using diameter:", c2.calculate_area())
Circle.info()

