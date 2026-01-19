# Write a program which accepts one number and prints
# cube of that number
# input : 2
# output : 8


def Cube(Value):
    Ans = 0

    Ans = Value * Value * Value

    return Ans

def main():
    
    print("Enter  Number :")
    Value1 = int(input())

    Ret = Cube(Value1)
    print("Cube of Value is :",Ret)

    
if __name__ == "__main__":
    main()