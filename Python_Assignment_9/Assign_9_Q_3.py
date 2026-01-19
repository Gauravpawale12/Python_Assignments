# Write a program which accepts one number and prints
# square of that number
# input : 5
# output : 25


def Square(Value):
    Ans = 0

    Ans = Value * Value

    return Ans

def main():
    
    print("Enter  Number :")
    Value1 = int(input())

    Ret = Square(Value1)
    print("Square of Value is :",Ret)

    
if __name__ == "__main__":

    main()


'''
#include<stdio.h>

int Square(int iNo)
{
    int Sqr = iNo * iNo;
    printf("%d\n",Sqr);
}

int main()
{
    int iNo = 0;

    printf("Enter number : \n");
    scanf("%d",&iNo);

    Square(iNo);
    

    return 0;
}
'''

