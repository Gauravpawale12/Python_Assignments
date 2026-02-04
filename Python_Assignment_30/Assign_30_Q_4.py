'''
Copy File Contents into Another File

Problem Statement:
Write a program which accepts two file names from the user.

First file is an existing file

Second file is a new file

Copy all contents from the first file into the second file.

Input:
ABC.txt Demo.txt

Expected Output:
Contents of ABC.txt copied into Demo.txt.
'''

source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

try:
    with open(source_file, "r") as src:
        content = src.read()

    with open(destination_file, "w") as dest:
        dest.write(content)

    print("Contents of", source_file, "copied into", destination_file)
except FileNotFoundError:
    print("Source file not found.")
