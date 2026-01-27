# Write a Python program to implement a class named BokkStore with following specifications :
'''
# The class should contain two instace variables:
    # Name (Book Name)
    # Author (Book Author)
# The class should contain one class variable:
    # NoOfBooks(initialize it to 0)
# Define constructor(__init__) that accepts Name and Author and initialize instance variables.
# Inside the cosntructor, increment the class variable NoOfBooks by 1 whenever a new object is created.
# Implement an instance method :
    # Display() - should display book details in the format :
        <BookName> by <Author>. No of books: <NoOfBooks>

Example usage :

obj1 = BookStore("Linux System Programming", "Robert Love")
obj1.Display() # Linux System Programming by Robert Love. No of books : 1

obj2 = BookStore("C Programming", "Dennis Ritchie")
obj2.Display() # C Programming by Dennis Ritchie. No of books : 2



'''
class BookStore:
    # Class variable
    NoOfBooks = 0

    # Constructor
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author

        # Increment class variable when new object is created
        BookStore.NoOfBooks += 1

    # Instance method
    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books : {BookStore.NoOfBooks}")

