# Write a program which accepts one number and 
# prints factorial of that number
# input : 5
# output : 120


def Factorial_Number(Value):
    Fact = 1
    for i in range(1,Value+1):
        Fact = Fact * i
    print(Fact)
        

def main():
    
    print("Enter  Number :")
    Value = int(input())

    Factorial_Number(Value)
    

    
if __name__ == "__main__":

    main()

'''
#include<stdio.h>

int Fact(int iValue)
{
   int iCnt = 0, fact = 1;
   for(iCnt = 1;iCnt <= iValue;iCnt++)
   {
       fact = fact * iCnt;
   }
   printf("%d",fact);
  
}
int main()
{
    int iNo = 0;
    
    printf("Enter the number : \n");
    scanf("%d",&iNo);
    
    Fact(iNo);
    
    return 0;
}
'''
