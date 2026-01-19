# Write a program which accepts one number and 
# prints that many numbers starting from 1
# input : 5
# output : 1    2   3   4   5

def Display(iValue):
    for i in range(1,iValue+1):
        print(i)

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

int main()
{
   int iNo = 0;

   printf("Enter the number : \n");
   scanf("%d",&iNo);

   Display(iNo);


    return 0;
}
'''