# Write a program which accepts marks and displays grades 
# >= 75 -> Distinction
# >= 60 -> First Class
# >= 50 -> Second Class
# < 50 -> Fail
 
def Display_Grades(Marks):

    if(Marks >= 75.00 and Marks<= 100.00):   
       return Marks
   
    elif(Marks <= 60 and Marks >= 74.99):
       return Marks
   
    elif(Marks >= 50.00 and Marks <= 59.00):
       return Marks
    else:
        return Marks
      

def main():
    Marks = 0
    fRet = 0

    print("Enter the Marks : ")
    Marks = float(input())

    fRet = Display_Grades(Marks)

    if(fRet >= 75.00 and fRet <= 100.00):
         print("Passed in : Distinction\n")

    elif(fRet >= 60.00 and fRet <= 74.99):
         print("Passed in : First Class\n")

    elif(fRet >= 50.00 and fRet <= 59.00):
         print("Passed in Second Class \n")

    else:
         print("You have : Failed\n")
         

if __name__ == "__main__":
    main()

    '''

#include <stdio.h>

float Display_Grades(float Marks)

{
     if(Marks >= 75.00 && Marks<= 100.00)
   {
       return Marks;
   }
   else if(Marks <= 60 && Marks >= 74.99)
   {
       return Marks;
   }
   else if(Marks >= 50.00 && Marks <= 59.00)
   {
       return Marks;
   }
}
int main() {
   float Marks  = 0;
   float fRet = 0;
   printf("Enter the marks : \n");
   scanf("%f",&Marks);
   
   fRet = Display_Grades(Marks);
   
   if(fRet >= 75.00 && fRet <= 100.00)
   {
       printf("Passed in : Distinction\n");
   }
   else if(fRet <= 60 && fRet >= 74.99)
   {
       printf("Passed in : First Class\n");
   }
   else if(fRet >= 50.00 && fRet <= 59.00)
   {
       printf("Passed in Second Class \n");
   }
   else
   {
       printf("You have : Failed.\n");
   }
    return 0;
}    
    '''