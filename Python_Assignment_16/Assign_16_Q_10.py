# Write a program which accepts name from user and display length of its name
# input : Marvellous    output : 10

def Display_Length(Name):
    # print(len(Name))
    iCnt = 0

    for ch in Name:
        iCnt = iCnt + 1

    return iCnt


def main():
    Name = ""

    print("Enter your name : ")
    Name = input()

    iRet = Display_Length(Name)
    print("Length of name is :", iRet)


if __name__ == "__main__":
    main()
