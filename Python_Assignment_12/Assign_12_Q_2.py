# Write a program which accepts  and 
#  prints its factors
# input : a
# output : Vowel

def DisplayFactors(iNo):
    Cnt = 1
    for i_cnt in range(1,(iNo // 2)+1):
        if iNo % i_cnt == 0:
            print(i_cnt)
   

def main():
   iValue = 0

   print("Enter a Number: ")
   iValue = int(input())

   DisplayFactors(iValue)

if __name__ == "__main__":
    main()

'''
#include<stdio.h>
#include<stdbool.h>

int main()
{
    int iValue = 0;
    int Factors = 0;
    int iCnt = 0;

    printf("Enter a number : \n);
    scanf("%d",&iValue);

    for(iCnt = 1; iValue >= iCnt ; iCnt++)
    {
        if(iValue / iCnt == 0)
            {
                printf("%d\t",iCnt);
            }
    }
    
    return 0;
}
'''