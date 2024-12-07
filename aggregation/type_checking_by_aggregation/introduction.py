"""
Type checking by aggregation in Python OOP means validating that the objects or components being used as attributes (parts) of a class
instance are of the correct or expected types. This is particularly important in object-oriented design when a class "aggregates" (i.e., contains)
instances of other classes to represent complex systems.

Aggregation represents a "has-a" relationship. For instance, an Order class has Product objects, or a Department class has Employee objects.
Type checking ensures that the components provided during runtime are valid instances of the expected types.
"""

from typing import List

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book {self.title} written by {self.author}."

class Library:
    def __init__(self, name):
        self.name = name
        self.books: List[Book] = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only objects of type 'Book' can be added to the library.")
        self.books.append(book)
        print(f"Added {book} to {self.name}.")

    def list_books(self):
        if not self.books:
            print(f"{self.name} has no books.")
        else:
            for book in self.books:
                print(f" - {book}")

try:
    library = Library("Dhaka Central Library")

    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)

    library.list_books()

    library.add_book("Random String")

except TypeError as e:
    print(f"Error - {e}")

