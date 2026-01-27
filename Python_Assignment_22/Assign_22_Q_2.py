# Write a python program to implement a class named Circle with following requirenments :
'''
# The class should contain three instance variables : Radius, Area and Circumstance
# The class should contain on e class variable named PI, initialized to 3.14
# Define constructor(__init__) that initializes all the instances to 0.0
# Implement the following instance methods
    # Accept() - accepts the radius of circle from user
    # CalculateArea() - calculates the area of the circle and stores it in Area variable
    # CalculateCircumference() - calculates the circumference of the circle and stores it in the Circumference variable
    # Display() - Displays the values of Radius, Area and Circumference
    # Create multiple objects of Circle class and invoke all the instance methods for each object 
     
'''


class Circle:
    # Class variable
    PI = 3.14

    # Constructor
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    # Accept radius from user
    def Accept(self):
        self.Radius = float(input("Enter radius of circle: "))

    # Calculate area
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    # Calculate circumference
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    # Display values
    def Display(self):
        print("Radius        :", self.Radius)
        print("Area          :", self.Area)
        print("Circumference :", self.Circumference)
        print("----------------------------")


# Creating multiple objects
obj1 = Circle()
obj2 = Circle()

# Invoking methods for first object
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

# Invoking methods for second object
obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()
