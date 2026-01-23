# Write a program which accepts one number from user and retrun its factorial
# input : 5
# Output : 120
def Factorial(iNum):
    Fact = 1
    while iNum != 1:
        Fact = Fact * iNum
        iNum -=1
    return Fact
    
def main():
    iNum = 0

    print("Enter the number :")
    iNum = int(input())

    iFact = Factorial(iNum)
    print("Factorial of ",iNum,"is :",iFact)

if __name__ == "__main__":
    main()

    '''
    #include<stdio.h>
    int Factorial(int iNo)
    {
        int Facto = 1;

        while(iNo != 1)
        {
            Facto = Facto * iNo;
            iNo--;
        }
    
    }
    int main()
    {
        int iNum = 0;

        printf("Enter the number : \n");
        scanf("%d",&iNum);

        int Fact = Factorial(iNum);
        printf("%d is the Factorial.",Fact);

    return 0;
    }
    
    '''