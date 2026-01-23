# Write a program which contains filter(),map(),reduce() in it.
# Python application one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all prime numbers.
# Map function will multiply each number by 2.
# Reduce will return Maximum number from that numbers.
# use normal fucntions 
# input list : [2,70,11,10,17,23,31,77]
# list after filter : [2,11,17,23,31]
# list after map : [4,22,34,46,62]
# output of reduce : 62

from functools import reduce

# Function to check prime number
def ChkPrime(iNo):
    if iNo <= 1:
        return False

    for i in range(2, (iNo // 2) + 1):
        if iNo % i == 0:
            return False

    return True


# Map function: multiply by 2
def MultByTwo(iNo):
    return iNo * 2


# Reduce function: return maximum
def Maximum(a, b):
    if a > b:
        return a
    else:
        return b


def main():
    print("Enter number of elements:")
    iSize = int(input())

    arr = []
    print("Enter the elements:")
    for i in range(iSize):
        no = int(input())
        arr.append(no)

    # Filter: prime numbers
    FData = list(filter(ChkPrime, arr))
    print("List after filter:", FData)

    # Map: multiply each by 2
    MData = list(map(MultByTwo, FData))
    print("List after map:", MData)

    # Reduce: maximum number
    RData = reduce(Maximum, MData)
    print("Output of reduce:", RData)


if __name__ == "__main__":
    main()
