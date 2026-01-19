# Write a program which accepts one number and 
# prints all the odd numbers till that number
# input : 10
# output : 1    3   5   7   9   


def Even_Number(Value):
    
    for num in range(1,Value+1):
        if(num % 2 != 0):
            print(num)
           
        

def main():
    
    print("Enter  Number :")
    Value = int(input())

    Even_Number(Value)
    
    

    
if __name__ == "__main__":

    main()

'''
#include<stdio.h>

int Odd_Number(int iValue)
{
   int iCnt = 0;
   for(iCnt = 1;iCnt <= iValue;iCnt++)
   {
       if(iCnt % 2 != 0)
       {
           printf("%d\n",iCnt);
       }
   }
 }
int main()
{
    int iNo = 0;
    
    printf("Enter the number : \n");
    scanf("%d",&iNo);
    
    Odd_Number(iNo);
    
    return 0;
}

'''
