# Write a Lambda function which accepts a number
# and return a cube of that number

Cube = lambda Num : Num * Num * Num


def main():
    iNum = 0
    iRet = 0

    print("Enter the number : ")
    iNum = int(input())

    iRet = Cube(iNum)
    print("Cube of", iNum,"is :",iRet)


if __name__ == "__main__":
    main()