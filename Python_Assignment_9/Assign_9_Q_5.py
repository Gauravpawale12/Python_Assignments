# Write a program which accepts one number and 
# checks whether it is divisible by 3 and 5
# input : 15
# output : Divisible by 3 and 5


def CheckDivisible(Value):
    if((Value % 3 == 0)  and (Value % 5 == 0)):
        
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")
         
        

def main():
    
    print("Enter  Number :")
    Value1 = int(input())

    CheckDivisible(Value1)
    

    
if __name__ == "__main__":
    main()