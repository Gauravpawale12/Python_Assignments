# Write a program which accepts length and width 
# of rectangle and print area.
# input : length = 4, width = 5 
# output : 20

def Area(length,width):
    AreaX = 0

    AreaX = length * width
    return AreaX


def main():
    length = 0
    width = 0

    print("Enter the length : ")
    length = float(input())

    print("Enter the width : ")
    width = float(input())

    iRet = Area(length,width)
    print("Area is  : ",iRet)


if __name__ == "__main__":
    main()

    '''
    #include<stdio.h>

    float Area(float length, float width)
    {
        float Area = 0;

        Area = length * width;
        return Area;
    
    }

    int main()
    {
        float length = 0;
        float width = 0;

        printf("Enter the Length : \n");
        scanf("%f",&length);

        printf("Enter the width : \n");
        scanf("%f",&width);

        float iRet = Area(length,width);
        printf("Area is : %f",iRet);


        return 0;
    }

    
    
    '''