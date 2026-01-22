# Write a program which accepts number from user and print 
# that number of * on screen 

def Display(Num):
    while Num != 0:
        print("*",end="\t")
        Num -=1

def main():
   Num = 0

   print("Enter the number :")
   Num = int(input())

   iRet = Display(Num)
   
       

  
if __name__ == "__main__":
    main()