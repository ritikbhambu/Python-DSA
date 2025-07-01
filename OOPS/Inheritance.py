
class Shape():

    def calculate_area(self):
        print("it is the base class")   


class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print(f"Area of Rectangle is {self.length*self.width}")
   

class Triangle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        print(f"Area of Circle is{self.radius*self.radius*3.14}")    



Shape_obj = Shape()
Shape_obj.calculate_area()
Rectangle_obj = Rectangle(20,10)
Rectangle_obj.calculate_area()
Triangle_obj = Triangle(10)
Triangle_obj.calculate_area()
