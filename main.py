from book import Book

book1 = Book("Python Basics", 75)

print(book1.price)  # Output: 75

book1.apply_discount(0.2)
print(book1.price)  # Output: 60.0 (20% discount applied)

book1.apply_increment(0.1)
print(book1.price)  # Output: 66.0 (10% increment applied)
