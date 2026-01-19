# Write a program which accepts one number and 
# prints all the even numbers till that number
# input : 10
# output : 2    4   6   8   10


def Even_Number(Value):
    
    for num in range(1,Value+1):
        if(num % 2 == 0):
            print(num)
           
        

def main():
    
    print("Enter  Number :")
    Value = int(input())

    Even_Number(Value)
    
    

    
if __name__ == "__main__":
    main()