# Write a Lambda function which accepts one number
# and returns True if number is even otherwise False

Check_Even = lambda Num1 : (Num1 % 2 == 0)


def main():
    iNum1 = 0
   
    iRet = 0

    print("Enter the first number : ")
    iNum1 = int(input())

   
    iRet = Check_Even(iNum1)
    
    if(iRet == True):
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()