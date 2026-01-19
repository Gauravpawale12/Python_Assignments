# Write a program which accepts one number and 
# checks whether it is prime or not
# input : 11
# output : prime number

def Check_Prime(No):
    if No < 2:          # 0 and 1 are NOT prime
        return False
    if No == 2:         # 2 is prime
        return True
    if No % 2 == 0:     # even numbers > 2 are not prime
        return False
    
    # Check all numbers from 3 to No-1
    for i in range(3, No):
        if No % i == 0:  # divisible
            return False
    
    return True          # no divisor found → prime

def main():
    No = int(input("Enter Number: "))

    iRet = Check_Prime(No)
    if iRet:
        print("Prime Number", No)
    else:
        print("NOT Prime Number")

if __name__ == "__main__":
    main()


'''

#include <stdio.h>
#include <stdbool.h>  // for bool type

bool Check_Prime(int No)
{
    if (No < 2)         // 0 and 1 are NOT prime
        return false;
    if (No == 2)        // 2 is prime
        return true;
    if (No % 2 == 0)    // even numbers > 2 are not prime
        return false;

    // Check all numbers from 3 to No-1
    for (int i = 3; i < No; i++)
    {
        if (No % i == 0)  // divisible
            return false;
    }

    return true;  // no divisor found → prime
}

int main()
{
    int No;
    printf("Enter Number: ");
    scanf("%d", &No);

    if (Check_Prime(No))
        printf("Prime Number %d\n", No);
    else
        printf("NOT Prime Number\n");

    return 0;
}

'''