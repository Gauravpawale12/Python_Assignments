# Write a program which contains one lambda function which accepts one parameter and return power of two 
# input : 4    output : 16 
# input : 6    output : 64


Power = lambda iNo: 2 ** iNo

def main():
    print("Enter the number:")
    iValue = int(input())

    iResult = Power(iValue)
    print("Power of two is:", iResult)


if __name__ == "__main__":
    main()
