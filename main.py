from printed_book import PrintedBook
from ebook import EBook

printed_book1 = PrintedBook("Python Basics", 75, 3)
printed_book1.apply_discount()
print(printed_book1.price)  # Output: 60.0


ebook1 = EBook("Python Basics", 75, 3)
ebook1.apply_discount()
print(ebook1.price)  # Output: 37.5
