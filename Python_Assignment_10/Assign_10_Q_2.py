# Write a program which accepts one number and 
# prints sum of first N natural numbers
# input : 5
# output : 15


def Sum_N_Numbers(Value):
    Sum = 0
    for i in range(1,Value+1):
        Sum = Sum + i
    print(Sum)
        

def main():
    
    print("Enter  Number :")
    Value = int(input())

    Sum_N_Numbers(Value)
    

    
if __name__ == "__main__":

    main()

'''
#include<stdio.h>

int Sum_N_Numbers(int iValue)
{
   int iCnt = 0, Sum = 0;
   for(iCnt = 1;iCnt <= iValue;iCnt++)
   {
       Sum = Sum + iCnt;
   }
   printf("%d",Sum);
  
}
int main()
{
    int iNo = 0;
    
    printf("Enter the number : \n");
    scanf("%d",&iNo);
    
    Sum_N_Numbers(iNo);
    
    return 0;
}

'''
