# Create one module named as Arithmetic which contains 4 functions as Add()
# for Addtion, Sub() for substraction, Mult() for multiplication
# and Div() for division. All functions accepts two parameters as number
# and peform the operation. Write on python program which call all the fucntions from 
# Arithmetic module by accepting the parameters from user 
import  Assign_17_Q_1_module

def main():
    print("Enter the First number")
    Num1 = float(input())

    print("Enter the Second Number") 
    Num2 = float(input())

    iAdd = Assign_17_Q_1_module.Add(Num1, Num2)
    print("Addition is :", iAdd)

    iSub = Assign_17_Q_1_module.Sub(Num1, Num2)
    print("Substraction is :", iSub)

    iMult = Assign_17_Q_1_module.Mult(Num1, Num2)
    print("Multiplication is :", iMult)

    iDiv = Assign_17_Q_1_module.Div(Num1, Num2)
    print("Division is :", iDiv)


if __name__ == "__main__":
    main()
