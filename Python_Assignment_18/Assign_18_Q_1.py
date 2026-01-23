# Write a program which accepts N numbers from user and 
# store it into List. Return addition of all elements from that list
# input : Number of elements : 6
# input elements : 13   5   45  7   4   56
# output : 130


def AddList(arr):
    iSum = 0

    for i in arr:
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

    iResult = AddList(arr)
    print("Addition of all elements is:", iResult)


if __name__ == "__main__":
    main()
