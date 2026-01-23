# Write a program which accepts one number from user and check
# whether number is prime or not 
# input : 5
# Output : It is prime number

def CheckPrime(iNo):
    if iNo <= 1:
        return False

    for i in range(2, (iNo // 2) + 1):
        if iNo % i == 0:
            return False

    return True

def main():
    print("Enter the number:")
    iValue = int(input())

    iResult = CheckPrime(iValue)
    if iValue == True:
        print("It is Prime Number")
    else:
        print("It is NOT Prime Number")


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