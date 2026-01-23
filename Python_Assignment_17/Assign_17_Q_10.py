# Write a program which accepts number from user and return 
# addtion of digits in that number
# input : 5187934 
# output : 37

def SumOfDigits(iNo):
    iSum = 0

    while iNo != 0:
        iDigit = iNo % 10
        iSum = iSum + iDigit
        iNo = iNo // 10

    return iSum


def main():
    print("Enter the number:")
    iValue = int(input())

    iResult = SumOfDigits(iValue)
    print("Addition of digits is:", iResult)


if __name__ == "__main__":
    main()
