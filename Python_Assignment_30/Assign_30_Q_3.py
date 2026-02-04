'''
Display File Line by Line

Problem Statement:
Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.

Input:
Demo.txt

Expected Output:
Display each line of Demo.txt one by one.

'''
filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print("File not found.")

