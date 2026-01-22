# write a program accepts number from user and check whether that number is positive or negative or zero
# input : 11   output : Positive Number
# input : -8   output : Negative Number
# input : 0    output : Zero

def Check_Num(Num):
    if Num > 0:
        print("Positive Number.")
    elif Num < 0:
        print("Negative Number.")
    else:
        print("Zero")
        
def main():
   Num = 0

   print("Enter the number :")
   Num = int(input())

   iRet = Check_Num(Num)

  
if __name__ == "__main__":
    main()