'''
Frequency of a String in File

Problem Statement:
Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.

Input:
Demo.txt
Marvellous

Expected Output:
Count how many times "Marvellous" appears in Demo.txt.
'''
# Accept inputs from user
filename = input("Enter file name: ")
search_string = input("Enter string to search: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    count = content.count(search_string)

    print(f'"{search_string}" appears {count} times in {filename}.')

except FileNotFoundError:
    print(f"{filename} does not exist.")
