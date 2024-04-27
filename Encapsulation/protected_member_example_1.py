class Book:
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._is_borrowed = False

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_isbn(self):
        return self._isbn

    def is_borrowed(self):
        return self._is_borrowed

    def _set_borrowed_status(self, status):
        self._is_borrowed = status

    def borrow_book(self):
        if not self._is_borrowed:
            self._set_borrowed_status(True)
            print(f"{self._title} by {self._author} has been borrowed.")
        else:
            print(f"{self._title} by {self._author} is already borrowed.")

    def return_book(self):
        if self._is_borrowed:
            self._set_borrowed_status(False)
            print(f"{self._title} by {self._author} has been returned.")
        else:
            print(f"{self._title} by {self._author} is not borrowed")

class Patron:
    def __init__(self, name):
        self._name = name
        self._borrowed_books = []

    def get_name(self):
        return self._name

    def borrow_book(self, book):
        if book.is_borrowed():
            print(f"Sorry {book.get_title()} by {book.get_author()} is already borrowed.")
        else:
            self._borrowed_books.append(book)
            book.borrow_book()

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book.return_book()
            print(f"{self._name} has returned {book.get_title()} by {book.get_author()}.")
        else:
            print(f"{self._name} hasn't borroweed {book.get_title()} by {book.get_author()}.")

book1 = Book("Html", "Monim", "100")
book2 = Book("C++", "Nahid", "101")

patron1 = Patron("Anik")
patron2 = Patron("Sourov")

patron1.borrow_book(book1)
patron1.borrow_book(book2)
patron2.borrow_book(book1)

patron1.return_book(book1)
patron1.return_book(book2)
patron2.return_book(book1)

# Access Outside
print(book1._title)
print(book1._author)
print(book1._isbn)

book1._set_borrowed_status(True)
print(book1._is_borrowed)
