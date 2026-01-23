# Write a program which accepts one number from user 
# and prints below pattern
# input : 5
# output :      1   2   3   4   5
#               1   2   3   4   5 
#               1   2   3   4   5   
#               1   2   3   4   5  
#               1   2   3   4   5


def Display(iNo):
    for i in range(1, iNo + 1):          # rows
        for j in range(1, iNo + 1):      # columns
            print(j, "\t", end="")
        print()


def main():
    print("Enter the number:")
    iValue = int(input())

    Display(iValue)


if __name__ == "__main__":
    main()
