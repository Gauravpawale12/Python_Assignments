# Write a program which accepts one number and 
# prints sum of first N natural numbers
# input : 5
# output : 15


def Sum_N_Numbers(Value):
    Sum = 0
    for i in range(1,Value+1):
        Sum = Sum + i
    print(Sum)
        

def main():
    
    print("Enter  Number :")
    Value = int(input())

    Sum_N_Numbers(Value)
    

    
if __name__ == "__main__":
    main()