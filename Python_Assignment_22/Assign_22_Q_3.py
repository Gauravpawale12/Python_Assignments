# Write a python program to implement a class named Arithmetic with following characteristics:
'''
# The class should contain two instance variables : Value1 and Value2
# Define a constructor(__init__) that initializes all the instance variable to 0
# Implement following instance methods:
    # Accept() - accepts values for Value1 and Value2 from the user
    # Addition() - returns the addition of Value1 and Value2
    # Substraction() - returns the substraction of Value1 and Value2
    # Multiplication() - returns the multiplication of Value1 and Value2
    # Division() - returns the division of Value1 and Value2 (handle division by zero properly)
# Create multiple objects of Arithmetic class and invoke all the instance methods.
'''


class Arithmetic:
    # Constructor
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    # Accept values from user
    def Accept(self):
        self.Value1 = int(input("Enter first number: "))
        self.Value2 = int(input("Enter second number: "))

    # Addition
    def Addition(self):
        return self.Value1 + self.Value2

    # Substraction
    def Substraction(self):
        return self.Value1 - self.Value2

    # Multiplication
    def Multiplication(self):
        return self.Value1 * self.Value2

    # Division (with zero handling)
    def Division(self):
        if self.Value2 == 0:
            return "Error: Division by zero is not allowed"
        return self.Value1 / self.Value2


# Creating multiple objects
obj1 = Arithmetic()
obj2 = Arithmetic()

# First object
obj1.Accept()
print("Addition       :", obj1.Addition())
print("Substraction   :", obj1.Substraction())
print("Multiplication:", obj1.Multiplication())
print("Division       :", obj1.Division())
print("-----------------------------")

# Second object
obj2.Accept()
print("Addition       :", obj2.Addition())
print("Substraction   :", obj2.Substraction())
print("Multiplication:", obj2.Multiplication())
print("Division       :", obj2.Division())
