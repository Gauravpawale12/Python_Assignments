# Write a program which accepts number from user and return 
# number of digits in that number
# input : 5187934 
# output : 7


def CountDigits(iNo):
    iCnt = 0

    if iNo == 0:
        return 1

    while iNo != 0:
        iCnt = iCnt + 1
        iNo = iNo // 10

    return iCnt


def main():
    print("Enter the number:")
    iValue = int(input())

    iResult = CountDigits(iValue)
    print("Number of digits is:", iResult)


if __name__ == "__main__":
    main()
