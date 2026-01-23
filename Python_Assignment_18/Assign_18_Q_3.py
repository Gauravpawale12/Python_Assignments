# Write a program which accepts N numbers from user and 
# store it into List. Return Minumum number from that list
# input : Number of elements : 4
# input elements : 13   5   45  7   
# output : 5
def Minimum(arr):
    iMin = arr[0]

    for i in arr:
        if i < iMin:
            iMin = i

    return iMin


def main():
    print("Enter number of elements:")
    iSize = int(input())

    arr = []

    print("Enter the elements:")
    for i in range(iSize):
        no = int(input())
        arr.append(no)

    iResult = Minimum(arr)
    print("Minimum number is:", iResult)


if __name__ == "__main__":
    main()
