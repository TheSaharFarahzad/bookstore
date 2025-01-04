class Book:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


book1 = Book("Learning Python", 10, 5)
book2 = Book("Two Scoops of Django", 30, 10)

print(book1.title)  # Output: Learning Python
print(book1.price)  # Output: 10
print(book1.quantity)  # Output: 5
print(book1.calculate_total_price())  # Output: 50

print(book2.title)  # Output: Two Scoops of Django
print(book2.price)  # Output: 30
print(book2.quantity)  # Output: 10
print(book2.calculate_total_price())  # Output: 300
