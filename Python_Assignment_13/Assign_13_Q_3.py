# Write a program which accepts one number 
# and checks whether it is perfect or not
# input : 6
# output : perfect number 

def Sum_Factors(iNo):
    Factor = 0 
    Sum = 0
    iCnt = 0

    for iCnt in range(1, (iNo // 2) + 1):
        if iNo % iCnt == 0:
            print(f"Factors are : {iCnt}", end="\t")
            Sum = Sum + iCnt

    print()
    return Sum


def main():
    iNo = 0
    iSum = 0

    iNo = int(input("Enter the number : "))

    iSum = Sum_Factors(iNo)
    print(f"Sum is {iSum}")

    if iNo == iSum:
        print(f"{iNo} is perfect number")
    else:
        print(f"{iNo} is NOT perfect number")


if __name__ == "__main__":
    main()

    '''
  #include<stdio.h>
    
    int Sum_Factors(int iNo)
    {
        int Factor = 0, Sum = 0, iCnt = 0;
        
        for(iCnt = 1; iCnt <= (iNo / 2); iCnt++)
        {
            if(iNo % iCnt == 0)
            {
                printf("Factors are : %d \t",iCnt);
                Sum = Sum + iCnt;
            }
        }
        return Sum;
    }
    
   
    int main()
    {
       int iNo = 0, iSum = 0;
       
       printf("Enter the number : \n");
       scanf("%d",&iNo);
       
       iSum = Sum_Factors(iNo);
       printf("Sum is %d \n",iSum);
      
       
       if (iNo == iSum)
       {
           printf("%d is perfect number\n",iNo);
       }
       else
       {
           printf("%d is NOT perfect number\n",iNo);
       }
       
        return 0;
    }
    
    
    '''