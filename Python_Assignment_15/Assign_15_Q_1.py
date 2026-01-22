# Write a Lambda function using map() which accepts a list of numbers
# and returns list of squares of each number

Squares = lambda Num : Num * Num

def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    
    print("Actual Data is : ",Data)
    
    MData = list(map(Squares,Data))
    print("Data after map is : ",MData)
   

if __name__ == "__main__":
    main()