# Write a Lambda function using reduce() which accepts a list of numbers
# and returns maximum element

from functools import reduce

Add_Data = lambda Data: reduce(
    lambda iNum1, iNum2: iNum1 if iNum1 >= iNum2 else iNum2,
    Data
)

def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    
    print("Actual Data is : ", Data)
    
    RData = Add_Data(Data)
    print("Maximum element is : ", RData)
   

if __name__ == "__main__":
    main()
