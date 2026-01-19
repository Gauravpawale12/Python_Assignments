# Write a program which accepts one number and 
# prints sum of digits in that number
# input : 123
# output : 6

def Sum_Digit(No):
    iCnt = 0
    iSum = 0
        # return len(str(No))
    while No != 0:
        iDigit = No % 10
        iSum = iSum + iDigit
        No = No // 10        
    return iSum


def main():
    No = int(input("Enter Number: "))

    iRet = Sum_Digit(No)
    print("Sum of Digits is :",iRet)

if __name__ == "__main__":
    main()

'''
#include<stdio.h>

int SumDigits(int iNo)
{
    int iSum = 0;
    int iDigit = 0;

    while(iNo != 0)
    {
        iDigit = iNo % 10;
        iSum = iSum + iDigit;
        iNo = iNo / 10;
    }
    return iSum;
}

int main()
{
    int iValue = 0, iRet = 0;

    printf("Enter number : \n");
    scanf("%d",&iValue);

    iRet = SumDigits(iValue);
    printf("Sum of digits are : %d\n",iRet);

    return 0;
}


'''