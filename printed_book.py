from book import Book


class PrintedBook(Book):
    def __init__(self, title: str, price: float, quantity=0, damaged_copies=0):
        super().__init__(title, price, quantity)

        assert (
            damaged_copies >= 0
        ), f"Damaged copies {damaged_copies} is not greater or equal to zero"

        self.damaged_copies = damaged_copies
