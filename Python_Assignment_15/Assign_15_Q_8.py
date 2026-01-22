# Write a Lambda function using filter() which accepts a list of numbers
# and returns list of numbers divisible by both 3 and 5

Add_Data = lambda Data: list(filter(lambda iNo: (iNo % 3 == 0 and iNo % 5 == 0), Data))


def main():
    Data = [10, 15, 20, 30, 45, 50, 60, 75, 90]
    
    print("Actual Data is : ", Data)
    
    RData = Add_Data(Data)
    print("Data after filter is : ", RData)
   

if __name__ == "__main__":
    main()
