class Shape():
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print(f"area is {self.length*self.width}") 

Rectangel = Shape(10,20)
Rectangel.calculate_area()           