# Write a program which accepts N numbers from user and store it in list.
# Return addtion of all prime numbers from that list. Main python file accepts N numbers from user and 
# pass each number to ChkPrime() function which is part of our user defined module named MarvellousNum.
# Name of the function from main python file should be ListPrime()
# input : Number of elements : 11
# input elements : 13   5   45  7   4   56  10  34  2   5   8  
# output : 54(13+5+7+2+5)

def ChkPrime(iNo):
    if iNo <= 1:
        return False

    for i in range(2, (iNo // 2) + 1):
        if iNo % i == 0:
            return False

    return True
