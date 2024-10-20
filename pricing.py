from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""
    _instance = None

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class NewRelease(PriceStrategy):
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        return 3 * days

    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        return days


class RegularPrice(PriceStrategy):
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount

    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        return 1


class ChildrenPrice(PriceStrategy):
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount

    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        return 1


NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrenPrice()