# Write a Python program to implement a class named Numbers with the following  requrenments :
'''
# The class should contain one instance variable :
    # Value
# Define a constructor (__init__) that accepts a number from the user and initializes Value
# Implement the following instance methods :
    # ChkPrime() - returns True if the number is prime, otherwise returns False
    # ChkPerfect() - returns True if the number is perfert, otherwise returns False
    # Factors() - displays all factors of the number
    # SumFactors() - returns the sum of all factors 
    (You may use this method as helper ChkPerfect() if required)
# Create multiple objects and call all methods
'''


class Numbers:
    # Constructor
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    # Check prime number
    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                return False
        return True

    # Display factors
    def Factors(self):
        print("Factors of", self.Value, "are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    # Return sum of factors
    def SumFactors(self):
        sum_factors = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum_factors += i
        return sum_factors

    # Check perfect number
    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        return False


# Creating multiple objects
obj1 = Numbers()
obj2 = Numbers()

# First object
print("Is Prime   :", obj1.ChkPrime())
print("Is Perfect :", obj1.ChkPerfect())
obj1.Factors()
print("Sum of Factors :", obj1.SumFactors())
print("----------------------------")

# Second object
print("Is Prime   :", obj2.ChkPrime())
print("Is Perfect :", obj2.ChkPerfect())
obj2.Factors()
print("Sum of Factors :", obj2.SumFactors())
