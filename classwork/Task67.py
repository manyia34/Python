"""
Instance methods: Rectangle area and perimeters 
Problem: Create a Rectangle class with length and breadth. Use instance methods to calculate
its area and perimeter
"""

class Rectangle: 
    def __init__(self,len,bre):
        self.length = len
        self.breadth = bre
        
    def area_rectangle(self):
        area_of_rectangle = self.length * self.breadth
        print(f"Area of rectangle: {area_of_rectangle}.00")
        
    def perimeter_rectangle(self):
        perimeter_of_rectangle = 2 * (self.length + self.breadth)
        print(f"Perimeter of rectangle: {perimeter_of_rectangle}.00")
    
shape = Rectangle(10,10)
shape.area_rectangle()
shape.perimeter_rectangle()
