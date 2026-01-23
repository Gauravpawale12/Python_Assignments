# Write a program which accepts N numbers from user and 
# Accept one another number from user and return frequency of that number
# input : Number of elements : 11
# input elements : 13   5   45  7   4   56      5   34  2   5   65  
# input to search : 5
# output : 3


def Frequency(arr, iSearch):
    iCnt = 0

    for i in arr:
        if i == iSearch:
            iCnt = iCnt + 1

    return iCnt


def main():
    print("Enter number of elements:")
    iSize = int(input())

    arr = []

    print("Enter the elements:")
    for i in range(iSize):
        no = int(input())
        arr.append(no)

    print("Enter the number to search:")
    iValue = int(input())

    iResult = Frequency(arr, iValue)
    print("Frequency is:", iResult)


if __name__ == "__main__":
    main()

