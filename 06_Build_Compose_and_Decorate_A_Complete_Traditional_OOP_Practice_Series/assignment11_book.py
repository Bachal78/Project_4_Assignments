"""Create a class Book with a class variable total_books.
Add a class method increment_book_count() to increase
the count when a new book is added."""

class Book:
    total_books = 0

    def __init__(self):
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example
b1 = Book()
b2 = Book()
print(Book.total_books)
