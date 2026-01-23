# Create one module named as Arithmetic which contains 4 functions as Add()
# for Addtion, Sub() for substraction, Mult() for multiplication
# and Div() for division. All functions accepts two parameters as number
# and peform the operation. Write on python program which call all the fucntions from 
# Arithmetic module by accepting the parameters from user 
def Add(iNum1, iNum2):
    return iNum1 + iNum2

def Sub(iNum1, iNum2):
    return iNum1 - iNum2

def Mult(iNum1, iNum2):
    return iNum1 * iNum2

def Div(iNum1, iNum2):
    if iNum2 == 0:
        return "Division by zero not allowed"
    return iNum1 / iNum2

