# deine a circle class to create a circle with radius r using the constructor
# define the area method of the class which claculates the area of the circle
# define a perimeter() method of the class which allows you to claculate the perimeter of the circle

class circle:
    def __init__(self,r):
        self.radius = r

    def area(self):
        area = 3.14*self.radius*self.radius
        print("the area of the circle is: ",area)
    
    def perimeter(self):
        perimeter = 2*3.14*self.radius
        print("the perimter of the circle is:",perimeter)

circle1 = circle(3)
circle1.perimeter()
circle1.area()
