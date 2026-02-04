'''
Display File Contents

Problem Statement:
Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.

Input:
Demo.txt

Expected Output:
Display contents of Demo.txt on console.

'''

# Accept file name from user
filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        contents = file.read()
        print("File contents:\n")
        print(contents)
except FileNotFoundError:
    print(f"{filename} does not exist.")
