# Write a program which accepts two numbers and 
# prints addition, substraction, multiplication and division
# input : 
# output :

def Addition(iNo1,iNo2):
    Add = 0
    Add = int(iNo1) + int(iNo2)

    return Add
    

def Substraction(iNo1,iNo2):
    Subs = 0
    Subs = int(iNo1) - int(iNo2)

    return Subs
    

def Multiplication(iNo1,iNo2):
    Mult = 0
    Mult = int(iNo1) * int(iNo2)

    return Mult
    

def Division(iNo1,iNo2):
    Div = 0
    if iNo2 == 0:
        print("Cannot divide with zero")
        return 0
    Div = int(iNo1) / int(iNo2)

    return Div
    


def main():
   iValue1 = 0
   iValue2 = 0

   print("Enter a Number: ")
   iValue1 = int(input())

   print("Enter a Number: ")
   iValue2 = int(input())

   iAdd = Addition(iValue1,iValue2)
   print("Addtion is : ",iAdd)

   iSub = Substraction(iValue1,iValue2)
   print("Substraction is : ",iSub)

   iMult = Multiplication(iValue1,iValue2)
   print("Multiplication is : ",iMult)

   iDiv = Division(iValue1,iValue2)
   print("Division is : ",iDiv)


if __name__ == "__main__":
    main()

'''
#include<stdio.h>
#include<stdbool.h>

int Addition(int iNo1,int iNo2)
{
    int Ans = 0;

    Ans = iNo1 + iNo2;

    return Sum;
}

int Substraction(int iNo1,int iNo2)
{
    int Ans = 0;

    Ans = iNo1 - iNo2;

    return Subs;
}

int Multiplication(int iNo1,int iNo2)
{
    int Ans = 0;

    Ans = iNo1 * iNo2;

    return Mult;
}

int Division(int iNo1,int iNo2)
{
if(No2 == 0)
{
    printf("Cannot divide 0 with Denominator.\n");
    return 0;
}
    int Ans = 0;

    Ans = iNo1 / iNo2;

    return Div;
}


int main()
{
    int iValue1,iValue2;

    printf("Enter first number : \n");
    scanf("%d",&iValue1);

    printf("Enter second number : \n");
    scanf("%d",&iValue2);

    iAddition = Addition(iValue1,iValue2);
    print("Addition is : %d",iAddition);

    iSubstraction = Substraction(iValue1,iValue2);
    print("Substraction is : %d",iSubstraction);

    iMultiplication = Multiplication(iValue1,iValue2);
    print("Multiplication is : %d",iMultiplication);

    iDivision = Division(iValue1,iValue2);
    print("Division is : %d",iDivision);

    return 0;
}
'''