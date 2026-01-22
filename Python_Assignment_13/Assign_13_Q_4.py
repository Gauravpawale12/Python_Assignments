# Write a program which accepts one number 
# and prints equivalent binary
# input : 
# output :  

def Decimal_To_Binary(iNo):
    iCnt = 0
    iRem = 0
    iBin = ""

    if iNo == 0:
        return "0"

    while iNo > 0:
        iRem = iNo % 2
        iBin = str(iRem) + iBin
        iNo = iNo // 2

    return iBin


def main():
    iNo = 0
    iBinary = ""

    iNo = int(input("Enter the number : "))

    iBinary = Decimal_To_Binary(iNo)

    print(f"Binary equivalent is : {iBinary}")


if __name__ == "__main__":
    main()

    '''
  #include <stdio.h>

void Decimal_To_Binary(int iNo)
{
    int iCnt = 0;
    int iRem = 0;
    int iBin[32];   // array to store binary digits

    if (iNo == 0)
    {
        printf("Binary equivalent is : 0\n");
        return;
    }

    while (iNo > 0)
    {
        iRem = iNo % 2;
        iBin[iCnt] = iRem;
        iCnt++;
        iNo = iNo / 2;
    }

    printf("Binary equivalent is : ");

    // print in reverse order
    for (iCnt = iCnt - 1; iCnt >= 0; iCnt--)
    {
        printf("%d", iBin[iCnt]);
    }

    printf("\n");
}

int main()
{
    int iNo = 0;

    printf("Enter the number : \n");
    scanf("%d", &iNo);

    Decimal_To_Binary(iNo);

    return 0;
}

    
    
    '''