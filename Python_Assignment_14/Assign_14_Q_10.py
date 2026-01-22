# Write a Lambda function which accepts three numbers
# and returns largest number

Largest_Number = lambda iNum1,iNum2,iNum3 : (
    iNum1 if (iNum1 >= iNum2 and iNum1 >= iNum3)
    else iNum2 if (iNum2 >= iNum1 and iNum2 >= iNum3)
    else iNum3
)

def main():
    iNum1 = 0
    iNum2 = 0
    iNum3 = 0
   
    iRet = 0

    print("Enter the first number : ")
    iNum1 = int(input())

    print("Enter the second number : ")
    iNum2 = int(input())

    print("Enter the third number : ")
    iNum3 = int(input())

   
    iRet = Largest_Number(iNum1,iNum2,iNum3)
    print("Largest number is : ",iRet)
   

if __name__ == "__main__":
    main()