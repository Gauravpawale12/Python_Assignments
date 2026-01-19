# Write a program which accepts one number and 
# prints count of digits in that number
# input : 45778
# output : 5

def Count_Check(No):
    iCnt = 0
        # return len(str(No))
    while No != 0:
        iCnt += 1
        No = No // 10
        
    return iCnt


def main():
    No = int(input("Enter Number: "))

    iRet = Count_Check(No)
    print("Count is :",iRet)

if __name__ == "__main__":
    main()

'''
#include<stdio.h>

int CountDigits(int iNo)
{
    int iDigit = 0;
    int iCnt = 0;

    while(iNo != 0)
    {
        iDigit = iNo % 10;
        iCnt++;
        iNo = iNo / 10;
    }
    return iCnt;
}

int main()
{
    int iValue = 0, iRet = 0;

    printf("Enter number : \n");
    scanf("%d",&iValue);

    iRet = CountDigits(iValue);
    printf("Number of digits are : %d\n",iRet);

    return 0;
}
'''