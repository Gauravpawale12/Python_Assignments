# Write a program to implement a class named Demo with following specifications:
# The class should contain two instance variable as No1 and No2
# The class should contain one class varible named Value
# Define constructor (__init__) that accepts two parameters and initializes the instance variables
# Implement two instance methods 
    # Fun() - Displays the values of instance variables No1 and No2
    # Gun() - Displays the values of instance variable No1 and No2
# Create two objects of Demo class as follows 
# obj1 = Demo(11,21)
# obj2 = Demo(51,101)
# Call the instance methods in the given sequence 
'''
obj1.Fun()

obj2.Fun()
obj2.Gun()
obj2.Gun()
'''

class Demo:
    # Class variable
    Value = 0

    # Constructor
    def __init__(self, No1, No2):
        self.No1 = No1
        self.No2 = No2

    # Instance method Fun
    def Fun(self):
        print("Value of No1 :", self.No1)
        print("Value of No2 :", self.No2)

    # Instance method Gun
    def Gun(self):
        print("Value of No1 :", self.No1)
        print("Value of No2 :", self.No2)


# Creating objects
obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

# Calling methods in given sequence
obj1.Fun()

obj2.Fun()
obj2.Gun()
obj2.Gun()
