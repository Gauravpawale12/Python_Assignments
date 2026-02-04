'''
Copy File Contents into a New File (Command Line)

Problem Statement:
Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.

Input (Command Line):
ABC.txt

Expected Output:
Create Demo.txt and copy contents of ABC.txt into Demo.txt.

'''
import sys

# Check if filename is provided
if len(sys.argv) < 2:
    print("Usage: python copy_file.py <source_file>")
    sys.exit()

source_file = sys.argv[1]
destination_file = "Demo.txt"

try:
    with open(source_file, "r") as src:
        data = src.read()

    with open(destination_file, "w") as dest:
        dest.write(data)

    print(f"Contents of {source_file} copied into {destination_file} successfully.")

except FileNotFoundError:
    print(f"{source_file} does not exist.")
