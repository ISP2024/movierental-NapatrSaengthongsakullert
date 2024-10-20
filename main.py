# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import MovieCatalog
from pricing import price_code_for_movie
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
    days = 1
    for movie in movies:
        if movie:
            customer.add_rental(Rental(movie, days))
        days = (days + 2) % 5 + 1
    print(customer.statement())
