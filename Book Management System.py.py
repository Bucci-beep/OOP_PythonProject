class Book:
    all = []  # Class variable to store all book instances

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False  # Track if the book is borrowed

        # Add this book instance to the class-level list `all`
        Book.all.append(self)

    def display_book_details(self):
        return f"'{self.title}', '{self.author}', '{self.year}'"

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"The book '{self.title}' has been borrowed.🙂"
        else:
            return f"Sorry, the book '{self.title}' is already borrowed.🏾"

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"The book '{self.title}' has been returned.😉"
        else:
            return f"The book '{self.title}' is not currently borrowed.😎"

    @staticmethod
    def display_all_books():
        if Book.all:
            for book in Book.all:
                print(book.display_book_details())
        else:
            print("No books in the library currently.")

# Creating book instances
book1 = Book('Kill Bill', 'Quentin Tarantino', 1997)
book2 = Book('Pulp Fiction', 'Quentin Tarantino', 1994)
book3 = Book('Django Unchained', 'Quentin Tarantino', 2012)

# Displaying all books in the library
Book.display_all_books()
