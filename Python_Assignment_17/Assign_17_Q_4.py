# Write a program which accepts one number from user and retrun 
# addition of its factors
# input : 12
# Output : 16           (1+2+3+4+6)

def SumOfFactors(iNo):
    iSum = 0

    for i in range(1, (iNo // 2) + 1):
        if iNo % i == 0:
            iSum = iSum + i

    return iSum


def main():
    print("Enter the number:")
    iValue = int(input())

    iResult = SumOfFactors(iValue)
    print("Addition of factors is:", iResult)


if __name__ == "__main__":
    main()

    '''
   #include <stdio.h>

int SumOfFactors(int iNo)
{
    int i = 0;
    int iSum = 0;

    for(i = 1; i <= (iNo / 2); i++)
    {
        if(iNo % i == 0)
        {
            iSum = iSum + i;
        }
    }

    return iSum;
}

int main()
{
    int iValue = 0;
    int iResult = 0;

    printf("Enter the number:\n");
    scanf("%d", &iValue);

    iResult = SumOfFactors(iValue);
    printf("Addition of factors is: %d\n", iResult);

    return 0;
}

    '''