from pricing import PriceStrategy, NEW_RELEASE, REGULAR, CHILDREN

class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title, price_code: PriceStrategy):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code

    def get_price_code(self) -> PriceStrategy:
        # get the price code
        return self.price_code

    def get_price(self, days: int) -> float:
        return self.price_code.get_price(days)

    def get_rental_points(self, days: int) -> int:
        return self.price_code.get_rental_points(days)

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
