# Write a Lambda function using reduce() which accepts a list of numbers
# and returns addition of all numbers

from functools import reduce

Add_Data = lambda Data: reduce(lambda iNo1, iNo2: iNo1 + iNo2, Data)


def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    
    print("Actual Data is : ", Data)
    
    RData = Add_Data(Data)   
    print("Addition is  : ", RData)
   

if __name__ == "__main__":
    main()
