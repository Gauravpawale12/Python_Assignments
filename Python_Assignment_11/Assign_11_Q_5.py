# Write a program which accepts one number and 
# checks whether it is pallindrome or not 
# input : 121
# output : pallindrome

def pallindrome(iNo):
    iDigit = 0
    iReverse = 0
    iTemp = iNo

    if iNo < 0:
        iNo = -iNo

    while iNo != 0:
        iDigit = iNo % 10
        iReverse = (iReverse * 10) + iDigit
        iNo = iNo // 10  

    if iReverse == iTemp:
        return True
    else:
        return False


def main():
    iValue = 0
    bRet = False

    iValue = int(input("Enter number : "))

    bRet = pallindrome(iValue)

    if bRet == True:
        print("Pallindrome")
    else:
        print("NOT Pallindrome")

if __name__ == "__main__":
    main()

'''
#include<stdio.h>
#include<stdbool.h>

bool CheckPallindrome(int iNo)
{
    int iDigit = 0;
    int iReverse = 0;
    int iTemp = iNo;

    while(iNo != 0)
    {
        iDigit = iNo % 10;
        iReverse = (iReverse * 10)+iDigit;
        iNo = iNo / 10;
    }

    if(iReverse == iTemp)
    {
        return true;
    }
    else
    {   
        return false;
    }
}

int main()
{
    int iValue = 0;
    bool bRet = false;

    printf("Enter number : \n");
    scanf("%d",&iValue);

    bRet = CheckPallindrome(iValue);

    if(bRet == true)
    {
        printf("%d is a pallindrome number\n",iValue);
    }
    else
    {
        printf("%d is not a pallindrome number\n",iValue);
    }
    
    return 0;
}


'''