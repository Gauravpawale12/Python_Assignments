# Write a program which contain one function named as ChkNum().
# which accepts one parameter as number. If number is even then it should display
# "Even Number" otherwise display "Odd Number" on console

def ChkNum(Num):
    if Num % 2 == 0:
        return True
    else:
        return False

def main():
    Num = 0

    print("Enter the number : ")
    Num = int(input())

    iRet = ChkNum(Num)
    if iRet == True:
        print(Num,"is Even Number.")
    else:
        print(Num,"is Odd Number.")

if __name__ == "__main__":
    main()