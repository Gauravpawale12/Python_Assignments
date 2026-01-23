# Write a program which contains one lambda function
# which accepts two parameter and return it's multiplication 
# input : 4   3   output : 12 
# input : 6   3   output : 18

Mult = lambda iNo1, iNo2: iNo1 * iNo2

def main():
    print("Enter first number:")
    iValue1 = int(input())

    print("Enter second number:")
    iValue2 = int(input())

    iResult = Mult(iValue1, iValue2)
    print("Multiplication is:", iResult)


if __name__ == "__main__":
    main()
