# Write a program which accepts radius of circle 
# and prints area of circle
# input : radius = 4
# output : 50.27

PI = 3.14159

def Circle_Area(Radius):
    Area = PI * Radius * Radius

    return Area

def main():

    print("Enter the Radius : ")
    Radius = float(input())

    iRet = Circle_Area(Radius)
    print("Area of circle is : ",iRet)

if __name__ == "__main__":
    main()

    '''
    #include<stdio.h>
    #define PI 3.14159

    float Circle_Area(float Radius)
    {
        float Area = 0;

        Area = PI * Radius * Radius;

        return Area;
    }
   
    int main()
    {
        int Area = 0;
        float Radius = 0;

        printf("Enter the Radius : \n");
        scanf("%f",&Radius);

        float iRet = Circle_Area(Radius);
        printf("Area of circle is : %f ",iRet);      


        return 0;
    }

    
    
    '''