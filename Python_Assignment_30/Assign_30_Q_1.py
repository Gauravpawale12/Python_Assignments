'''
Count Lines in a File

Problem Statement:
Write a program which accepts a file name from the user and counts how many lines are present in the file.

Input:
Demo.txt

Expected Output:
Total number of lines in Demo.txt.

'''
filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()
        print("Total number of lines in", filename, ":", len(lines))
except FileNotFoundError:
    print("File not found.")
