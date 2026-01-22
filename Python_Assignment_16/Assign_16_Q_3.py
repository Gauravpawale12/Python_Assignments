# Write a program which contain one function named as Add().
# which accepts two numbers from user and return addtion of that two numbers


def Add(Num1,Num2):

    Sum = Num1 + Num2
    return Sum


def main():
    Num1 = 0
    Num2 = 0

    print("Enter the first number : ")
    Num1 = int(input())

    print("Enter the second number : ")
    Num2 = int(input())

    iRet = Add(Num1,Num2)
    print("Addition is :",iRet)


if __name__ == "__main__":
    main()