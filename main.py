class Book:
    all = []
    discount_rate = 0.2

    def __init__(self, title: str, price: float, quantity: int = 0):
        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

        self.title = title
        self.price = price
        self.quantity = quantity

        Book.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * (1 - self.discount_rate)

    def __repr__(self):
        return f"Book('{self.title}', {self.price}, {self.quantity})"


book1 = Book("Learning Python", 10, 5)
book2 = Book("Two Scoops of Django", 30, 10)
book3 = Book("Clean Code", 25, 7)
book4 = Book("Design Patterns in Python", 40, 3)
book5 = Book("Fluent Python", 60, 2)


for instance in Book.all:
    print(instance.title)
