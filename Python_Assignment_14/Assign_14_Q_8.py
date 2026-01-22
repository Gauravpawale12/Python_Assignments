# Write a Lambda function which accepts two numbers
# and returns addition

Addition = lambda iNum1,iNum2 : iNum1 + iNum2


def main():
    iNum1 = 0
    iNum2 = 0
   
    iRet = 0

    print("Enter the first number : ")
    iNum1 = int(input())

    print("Enter the second number : ")
    iNum2 = int(input())

   
    iRet = Addition(iNum1,iNum2)
    print("Addition is : ",iRet)
   

if __name__ == "__main__":
    main()