'''
Compare Two Files (Command Line)

Problem Statement:
Write a program which accepts two file names through command line arguments and compares the contents of both files.

If both files contain the same contents, display Success

Otherwise display Failure

Input (Command Line):
Demo.txt Hello.txt

Expected Output:
Success OR Failure
'''

import sys

# Check if two file names are provided
if len(sys.argv) < 3:
    print("Usage: python compare_files.py <file1> <file2>")
    sys.exit()

file1 = sys.argv[1]
file2 = sys.argv[2]

try:
    with open(file1, "r") as f1, open(file2, "r") as f2:
        content1 = f1.read()
        content2 = f2.read()

    if content1 == content2:
        print("Success")
    else:
        print("Failure")

except FileNotFoundError:
    print("One or both files do not exist.")
