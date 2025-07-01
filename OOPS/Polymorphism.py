
class Shape():
   
    def calculate_area(self): 
        print("it is the base class") 

    # def calculate_area(self,side=5):           #python doesnt support method overloading
    #     print(f"ared of square is {self.side*self.side }")

    # def calculate_area(self,side,height=5):
    #     print(f"area of triangle is  {0.5*self.side*self.height}")          


class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self): # Method overriding 
        print(f"Area of Rectangle is {self.length*self.width}")
   

Shape_obj = Shape()
Rectangle_obj = Rectangle(20,10)
Shape_obj.calculate_area()
Rectangle_obj.calculate_area()
 
