from book import Book
from printed_book import PrintedBook


book1 = Book("short", 10)  # Initialize with a short title
print(book1.title)  # Output: short

book1.title = "acceptable"  # New title, length is <= 10
print(book1.title)  # Output: acceptable

book1.title = "this_title_is_too_long"  # Raises Exception: The title is too long
