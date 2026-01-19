# Write a program which contains one fucntion ChkGreater()
# that accepts two numbers and prints the greater number
# input : 10 20
# output : 20 is greater


def ChkGreater(Value1,Value2):
    if Value1 > Value2:
        
            print(Value1,"is Greater")
        
    else:
        
            print(Value2,"is Greater")  
        

def main():
    
    print("Enter first Number :")
    Value1 = int(input())

    print("Enter second Number :")
    Value2 = int(input())

    ChkGreater(Value1,Value2)

    
if __name__ == "__main__":

    main()



'''
#include<stdio.h>

void ChkGreater(int iNo1,int iNo2)
{
    if(iNo1 > iNo2)
    {
        printf("%d is Greater than %d\n",iNo1,iNo2);
    }
    else
    {
        printf("%d is Smaller that %d\n",iNo2,iNo1);
    }
}

int main()
{
    int iValue1 = 0, iValue2 = 0;
    

    printf("Enter the first number : \n");
    scanf(iValue1);

    printf("Enter the second Number : \n");
    scanf(iValue2);

    ChkGreater(iValue1,iValue2);

    return 0;
}

'''
