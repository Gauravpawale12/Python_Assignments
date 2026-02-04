'''
Search a Word in File

Problem Statement:
Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.

Input:
Demo.txt Marvellous

Expected Output:
Display whether the word Marvellous is found in Demo.txt or not.
'''
filename = input("Enter file name: ")
search_word = input("Enter word to search: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    if search_word in content:
        print(f"Word '{search_word}' found in {filename}")
    else:
        print(f"Word '{search_word}' not found in {filename}")
except FileNotFoundError:
    print("File not found.")


