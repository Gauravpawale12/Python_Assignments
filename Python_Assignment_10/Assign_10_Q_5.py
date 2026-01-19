# Write a program which accepts one number and 
# prints all the odd numbers till that number
# input : 10
# output : 1    3   5   7   9   


def Even_Number(Value):
    
    for num in range(1,Value+1):
        if(num % 2 != 0):
            print(num)
           
        

def main():
    
    print("Enter  Number :")
    Value = int(input())

    Even_Number(Value)
    
    

    
if __name__ == "__main__":
    main()