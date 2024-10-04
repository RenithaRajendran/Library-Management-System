# Define the Library class
class Library:
    # Constructor to initialize the library attributes
    def __init__(self, name):
        self.name = name
        self.books = []  # List to store available books
        self.members = []  # List to store library members

    # Method to add a new book to the library
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' has been added to the library.")

    # Method to lend a book to a member
    def lend_book(self, book, member):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' has been lent to {member}.")
        else:
            print(f"Sorry, the book '{book}' is not available.")

    # Method to display all available books
    def display_books(self):
        if self.books:
            print("Available books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books are currently available in the library.")

# Create a Library object
library = Library("City Library")

# Adding books to the library
library.add_book("The Great Gatsby")
library.add_book("To Kill a Mockingbird")
library.add_book("1984")

# Display the available books
library.display_books()

# Lending books to members
library.lend_book("1984", "Alice")
library.lend_book("The Great Gatsby", "Bob")

# Display the available books after lending
library.display_books()

# Trying to lend a book that's already lent out
library.lend_book("1984", "Charlie")
