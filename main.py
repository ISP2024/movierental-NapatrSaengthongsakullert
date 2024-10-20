# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import MovieCatalog
from pricing import NEW_RELEASE, REGULAR, CHILDREN
from rental import Rental
from customer import Customer


def make_movies(catalog):
    """Some sample movies."""
    movies = [
        catalog.get_movie("Air"),
        catalog.get_movie("Oppenheimer"),
        catalog.get_movie("Frozen"),
        catalog.get_movie("Bitconned"),
        catalog.get_movie("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    catalog = MovieCatalog()
    customer = Customer("Edward Snowden")
    movies = make_movies(catalog)
    price_codes = [NEW_RELEASE, REGULAR, CHILDREN, NEW_RELEASE, REGULAR]
    days = 1
    for i in range(len(movies)):
        if movies[i]:
            customer.add_rental(Rental(movies[i], days, price_codes[i]))
        days = (days + 2) % 5 + 1
    print(customer.statement())
