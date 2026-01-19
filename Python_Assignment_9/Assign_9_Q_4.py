# Write a program which accepts one number and prints
# cube of that number
# input : 2
# output : 8


def Cube(Value):
    Ans = 0

    Ans = Value * Value * Value

    return Ans

def main():
    
    print("Enter  Number :")
    Value1 = int(input())

    Ret = Cube(Value1)
    print("Cube of Value is :",Ret)

    
if __name__ == "__main__":

    main()


'''
// C code with same statement

#include<stdio.h>

int Display_Cube(int iValue)
{
    int Cube = iValue * iValue * iValue;
    
    printf("%d is cube of %d\n",Cube,iValue);
}
int main()
{
    int iNo = 0;
    
    printf("Enter the number : \n");
    scanf("%d",&iNo);
    
    Display_Cube(iNo);
    
    return 0;
}
