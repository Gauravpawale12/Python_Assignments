'''
Count Words in a File

Problem Statement:
Write a program which accepts a file name from the user and counts the total number of words in that file.

Input:
Demo.txt

Expected Output:
Total number of words in Demo.txt.

'''
filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        print("Total number of words in", filename, ":", len(words))
except FileNotFoundError:
    print("File not found.")
