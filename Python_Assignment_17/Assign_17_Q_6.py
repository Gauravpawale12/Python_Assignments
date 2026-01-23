# Write a program which accepts one number from user 
# and prints below pattern
# input : 5
# output :      *   *   *   *   *
#               *   *   *   *   
#               *   *   *   
#               *   *   
#               *

def Display(iNo):
    for i in range(iNo, 0, -1):        # rows
        for j in range(1, i + 1):      # columns
            print("*\t", end="")
        print()                         # new line


def main():
    print("Enter the number:")
    iValue = int(input())

    Display(iValue)


if __name__ == "__main__":
    main()
