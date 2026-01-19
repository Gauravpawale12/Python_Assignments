# Write a program which accepts one number and 
# prints multiplication table of that number
# input : 4
# output : 4    8   12  16  20  24  28  32  36  40


def Mult_Table(Value):

    for i in range(1,11):
        Ans = Value * i
        print(Ans)
        

def main():
    
    print("Enter  Number :")
    Value = int(input())

    Mult_Table(Value)
    

    
if __name__ == "__main__":

    main()


'''
#include<stdio.h>

int Multiplication(int iValue)
{
   int iCnt = 1;
   for(iCnt = 1;iCnt <= 10;iCnt++)
   {
       int Mult = iValue * iCnt;
        printf("%d\t",Mult);
   }
  
}
int main()
{
    int iNo = 0;
    
    printf("Enter the number : \n");
    scanf("%d",&iNo);
    
    Multiplication(iNo);
    
    return 0;
}

'''
