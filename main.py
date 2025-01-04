class Book:
    def calculate_total_price(self, x, y):
        return x * y


book1 = Book()
book1.title = "Learning Python"
book1.price = 10
book1.quantity = 5
print(book1.calculate_total_price(book1.price, book1.quantity))  # Output: 50

book2 = Book()
book2.title = "Two Scoops of Django"
book2.price = 30
book2.quantity = 10
print(book2.calculate_total_price(book2.price, book2.quantity))  # Output: 300
