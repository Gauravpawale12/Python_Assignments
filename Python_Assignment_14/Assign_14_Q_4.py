# Write a Lambda function which accepts two numbers
# and returns minimum number

Check_Min = lambda Num1,Num2 : (Num1 < Num2)


def main():
    iNum1 = 0
    iNum2 = 0
    iRet = 0

    print("Enter the first number : ")
    iNum1 = int(input())

    print("Enter the first number : ")
    iNum2 = int(input())

    iRet = Check_Min(iNum1,iNum2)
    
    if(iRet == True):
        print(iNum1," is Minimum.")
    else:
        print(iNum2," is Minimum")

if __name__ == "__main__":
    main()