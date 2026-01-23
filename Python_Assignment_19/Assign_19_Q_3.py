# Write a program which contains filter(),map(),reduce() in it.
# Python application one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
# Map function will increase each number by 10. Reduce will return product of all that numbers.

# input list : [4,34,36,76,68,24,89,23,86,90,45,70]
# list after filter : [76,89,86,90,70]
# list after map : [86,99,96,100,80]
# output of reduce : 6538752000


from functools import reduce

def main():
    print("Enter number of elements:")
    iSize = int(input())

    arr = []
    print("Enter the elements:")
    for i in range(iSize):
        no = int(input())
        arr.append(no)

    # Filter: numbers between 70 and 90 (inclusive)
    FData = list(filter(lambda x: x >= 70 and x <= 90, arr))
    print("List after filter:", FData)

    # Map: increase each number by 10
    MData = list(map(lambda x: x + 10, FData))
    print("List after map:", MData)

    # Reduce: product of all numbers
    RData = reduce(lambda x, y: x * y, MData)
    print("Output of reduce:", RData)


if __name__ == "__main__":
    main()
