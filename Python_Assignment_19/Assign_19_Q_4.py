# Write a program which contains filter(),map(),reduce() in it.
# Python application one list of numbers. List contains the numbers which are accepted from user.
# Filter should out all such numbers which are even. 
# Map fucntion will calculate its square.
# Reduce will return addition of all that numbers
# input list : [5,2,3,4,3,4,1,2,8.10]
# list after filter : [2,4,4,2,8,10]
# list after map : [4,16,16,4,64,100]
# output of reduce : 204


from functools import reduce

def main():
    print("Enter number of elements:")
    iSize = int(input())

    arr = []
    print("Enter the elements:")
    for i in range(iSize):
        no = int(input())
        arr.append(no)

    # Filter: even numbers
    FData = list(filter(lambda x: x % 2 == 0, arr))
    print("List after filter:", FData)

    # Map: square of each number
    MData = list(map(lambda x: x * x, FData))
    print("List after map:", MData)

    # Reduce: addition of all numbers
    RData = reduce(lambda x, y: x + y, MData)
    print("Output of reduce:", RData)


if __name__ == "__main__":
    main()
