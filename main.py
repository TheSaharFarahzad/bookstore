import csv


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


class PrintedBook(Book):
    def __init__(self, title: str, price: float, quantity=0, damaged_copies=0):
        super().__init__(title, price, quantity)

        assert (
            damaged_copies >= 0
        ), f"Damaged copies {damaged_copies} is not greater or equal to zero"

        self.damaged_copies = damaged_copies


printed_book1 = PrintedBook("Introduction to Algorithms", 25, 7, 1)
printed_book2 = PrintedBook("Advanced Data Structures", 40, 3, 2)

print(Book.all)
print(PrintedBook.all)
