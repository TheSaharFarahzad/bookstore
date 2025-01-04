import csv


class Book:
    all = []
    discount_rate = 0.2

    def __init__(self, title: str, price: float, quantity: int = 0):
        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

        self.__title = title
        self.price = price
        self.quantity = quantity

        Book.all.append(self)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) > 10:
            raise Exception("The title is too long")
        else:
            self.__title = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * (1 - self.discount_rate)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.title}', {self.price}, {self.quantity})"
        )

    @classmethod
    def instantiate_from_csv(cls):
        with open("books.csv", "r") as f:
            reader = csv.DictReader(f)
            books = list(reader)

        for book in books:
            Book(
                title=book.get("Title"),
                price=float(book.get("Price")),
                quantity=int(book.get("Quantity")),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
