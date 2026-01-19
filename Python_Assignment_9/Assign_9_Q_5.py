# Write a program which accepts one number and 
# checks whether it is divisible by 3 and 5
# input : 15
# output : Divisible by 3 and 5


def CheckDivisible(Value):
    if((Value % 3 == 0)  and (Value % 5 == 0)):
        
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")
         
        

def main():
    
    print("Enter  Number :")
    Value1 = int(input())

    CheckDivisible(Value1)
    

    
if __name__ == "__main__":

    main()


'''
#include<stdio.h>

int Check_Divisible(int iValue)
{
    if((iValue % 3 == 0) && (iValue % 5 == 0))
    {
        
        printf("%d is Divisible by 3 and 5\n",iValue);
    }
    else
    {
        printf("%d is NOT Divisible by 3 and 5\n");
    }
}
int main()
{
    int iNo = 0;
    
    printf("Enter the number : \n");
    scanf("%d",&iNo);
    
    Check_Divisible(iNo);
    
    return 0;
}

'''
