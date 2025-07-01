class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other): # here + is used to add two objects
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)

result = p1 + p2  # Internally calls p1.__add__(p2)
print(result)     # Output: (4, 6)
