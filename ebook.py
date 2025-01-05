from book import Book


class EBook(Book):
    discount_rate = 0.5

    def __init__(self, title: str, price: float, quantity=0):
        super().__init__(title, price, quantity)
