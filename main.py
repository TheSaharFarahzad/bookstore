class Book:
    pass


book1 = Book()
book1.title = "Learning Python"
book1.price = 10
book1.quantity = 5


print(type(book1))  # Output: <class '__main__.Book'>
print(type(book1.title))  # Output: <class 'str'>
print(type(book1.price))  # Output: <class 'int'>
print(type(book1.quantity))  # Output: <class 'int'>
