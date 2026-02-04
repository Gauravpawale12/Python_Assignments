'''
Q1) Check File Exists in Current Directory

Problem Statement:
Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

Input:
Demo.txt

Expected Output:
Display whether Demo.txt exists or not.
'''


import os

# Accept file name from user
filename = input("Enter file name: ")

# Check if file exists in the current directory
if os.path.isfile(filename):
    print(f"{filename} exists in the current directory.")
else:
    print(f"{filename} does not exist in the current directory.")
