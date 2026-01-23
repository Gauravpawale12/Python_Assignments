# Write a program which accepts one number and display below pattern.
# input : 5
# output :      *   *   *   *   *
#               *   *   *   *   *
#               *   *   *   *   *
#               *   *   *   *   *
#               *   *   *   *   *

def Display(iNo):

    for i in range(1,iNo + 1):
        for j in range(1,iNo + 1):
            print("*\t", end="")
        print()   # new line after inner loop

def main():              
    print("Enter the number :")
    iNo = int(input())

    Display(iNo)

if __name__ == "__main__":
    main()



'''
#include<stdio.h>

int main()
{
    int i = 0;
    int j = 0;
    int iNo = 0;
    printf("Enter the number : \n");
    scanf("%d",&iNo);
    
    for(i = 1; i <= iNo;i++)
    {
        for(j = 1; j <= iNo; j++)
        {
            printf("*\t",j);
        }
        printf("\n");
    }
    
    return 0;
}
'''