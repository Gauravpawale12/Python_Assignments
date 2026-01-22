# Write a Lambda function using filter() which accepts a list of numbers
# and returns count of even numbers

Add_Data = lambda Data: len(list(filter(lambda iNo: iNo % 2 == 0, Data)))


def main():
    Data = [1, 2, 3, 4, 5]
    
    print("Actual Data is : ", Data)
    
    RData = Add_Data(Data)
    print("Count of even numbers is : ", RData)
   

if __name__ == "__main__":
    main()
