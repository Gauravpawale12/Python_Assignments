# Write a program which accepts N numbers from user and store it in list.
# Return addtion of all prime numbers from that list. Main python file accepts N numbers from user and 
# pass each number to ChkPrime() function which is part of our user defined module named MarvellousNum.
# Name of the function from main python file should be ListPrime()
# input : Number of elements : 11
# input elements : 13   5   45  7   4   56  10  34  2   5   8  
# output : 54(13+5+7+2+5)

import MarvellousNum

def ListPrime(arr):
    iSum = 0

    for i in arr:
        if MarvellousNum.ChkPrime(i):
            iSum = iSum + i

    return iSum


def main():
    print("Enter number of elements:")
    iSize = int(input())

    arr = []

    print("Enter the elements:")
    for i in range(iSize):
        no = int(input())
        arr.append(no)

    iResult = ListPrime(arr)
    print("Addition of prime numbers is:", iResult)


if __name__ == "__main__":
    main()
