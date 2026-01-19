# Write a program which contains one fucntion ChkGreater()
# that accepts two numbers and prints the greater number
# input : 10 20
# output : 20 is greater


def ChkGreater(Value1,Value2):
    if Value1 > Value2:
        
            print(Value1,"is Greater")
        
    else:
        
            print(Value2,"is Greater")  
        

def main():
    
    print("Enter first Number :")
    Value1 = int(input())

    print("Enter second Number :")
    Value2 = int(input())

    ChkGreater(Value1,Value2)

    
if __name__ == "__main__":
    main()