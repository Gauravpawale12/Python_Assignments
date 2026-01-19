# Write a program which accepts one character and 
# checks whether it is vowel or not 
# input : a
# output : Vowel

def Check_Vowel(cValue):
    if((cValue == 'A') or (cValue == 'E') or (cValue == 'I') or (cValue == 'O') or (cValue == 'U') or (cValue == 'a') or (cValue == 'e') or (cValue == 'i') or (cValue == 'o') or (cValue == 'u')):
        return True
    else:
        return False

   


def main():
    strr = '\0'
    cRet = False

    print("Enter Character : ")
    strr = str(input())

    cRet = Check_Vowel(strr)

    if cRet == True:
        print(strr," is Vowel")
    else:
        print(strr,"is not Vowel")


if __name__ == "__main__":
    main()

'''
#include<stdio.h>
#include<stdbool.h>

bool Check_Vowel(char cValue)
{
    if((cValue == 'A') || (cValue == 'E') || (cValue == 'I') || (cValue == 'O') || (cValue == 'U') || (cValue == 'a') || (cValue == 'e') || (cValue == 'i') || (cValue == 'o') || (cValue == 'u'))
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    char ch = '\0';
    bool bRet = false;

    printf("Enter character : \n");
    scanf("%c",&ch);

    bRet = Check_Vowel(ch);

    if(bRet == true)
    {
        printf("%c is a Vowel\n",ch);
    }
    else
    {
        printf("%c is not a Vowel\n",ch);
    }

    return 0;
}


'''
