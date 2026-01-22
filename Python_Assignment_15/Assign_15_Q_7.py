# Write a Lambda function using filter() which accepts a list of strings
# and returns list of strings having length greater than 5

Add_Data = lambda Data: list(filter(lambda Str: len(Str) > 5, Data))


def main():
    Data = ["India", "Marvellous", "Python", "Programming", "AI", "MachineLearning"]
    
    print("Actual Data is : ", Data)
    
    RData = Add_Data(Data)
    print("Data after filter is : ", RData)
   

if __name__ == "__main__":
    main()
