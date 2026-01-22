# Write a program which contains one function that accepts
# one number from user and returns true if number is divisible by 5 
# otherwise returns false
# input : 8        output : False
# input : 25       output : True

def Check_Divisible(Num):
    if Num % 5 == 0:
        return True
    else:
        return False
    
def main():
   Num = 0

   print("Enter the number :")
   Num = int(input())

   iRet = Check_Divisible(Num)
   if iRet == True:
       print(True)
   else:
       print(False)
       

  
if __name__ == "__main__":
    main()