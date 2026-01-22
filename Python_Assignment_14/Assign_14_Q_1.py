# Write a Lambda function which accepts a number
# and return a square of that number

Square = lambda Num : Num * Num


def main():
    iNum = 0
    iRet = 0

    print("Enter the number : ")
    iNum = int(input())

    iRet = Square(iNum)
    print("Square of", iNum,"is :",iRet)


if __name__ == "__main__":
    main()