# Write a program which accepts N numbers from user and 
# store it into List. Return Maximum number from that list
# input : Number of elements : 7
# input elements : 13   5   45  7   4   56  34
# output : 56

def Maximum(arr):
    iMax = arr[0]

    for i in arr:
        if i > iMax:
            iMax = i

    return iMax


def main():
    print("Enter number of elements:")
    iSize = int(input())

    arr = []

    print("Enter the elements:")
    for i in range(iSize):
        no = int(input())
        arr.append(no)

    iResult = Maximum(arr)
    print("Maximum number is:", iResult)


if __name__ == "__main__":
    main()
