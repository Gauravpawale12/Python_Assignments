# Write a program which accepts one number and 
# prints that many numbers in reverse order
# input : 5
# output : 5    4   3   2   1   

def Display(iValue):
    
    while iValue > 0:
        print(iValue)
        iValue -= 1

    

def main():
   iNo = 0

   print("Enter the number : ")
   iNo = int(input())

   Display(iNo)


if __name__ == "__main__":
    main()

'''
#include<stdio.h>
#include<stdbool.h>

void Display(int iNo)
{
    int iCnt = 0;
    while(iNo > iCnt)
    {
        printf("%d\t",iNo);
        iNo--;
    }
    
}
int main()
{
   int iNo = 0;

   printf("Enter the number : \n");
   scanf("%d",&iNo);

   Display(iNo);


    return 0;
}
'''