# Write a Lambda function using filter() which accepts a list of numbers
# and returns list of even numbers

Check_Even = lambda Num : Num % 2 == 0

def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    
    print("Actual Data is : ",Data)
    
    FData = list(filter(Check_Even,Data))
    print("Data after filter is : ",FData)
   

if __name__ == "__main__":
    main()