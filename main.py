class Book:
    discount_rate = 0.2

    def __init__(self, title: str, price: float, quantity: int = 0):
        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

        self.title = title
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * (1 - self.discount_rate)


book1 = Book("Learning Python", 10, 5)
book2 = Book("Two Scoops of Django", 30, 10)

book1.apply_discount()
print(book1.price)  # Output: 8.0

book2.discount_rate = 0.1
book2.apply_discount()
print(book2.price)  # Output: 27.0
