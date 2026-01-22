# Write a Lambda function using reduce() which accepts a list of numbers
# and returns product of all elements

from functools import reduce

Add_Data = lambda Data: reduce(lambda iNo1, iNo2: iNo1 * iNo2, Data)


def main():
    Data = [1, 2, 3, 4, 5]
    
    print("Actual Data is : ", Data)
    
    RData = Add_Data(Data)
    print("Product of all elements is : ", RData)
   

if __name__ == "__main__":
    main()
