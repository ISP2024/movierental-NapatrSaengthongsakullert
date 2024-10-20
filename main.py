# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from pricing import NEW_RELEASE, REGULAR, CHILDREN
from rental import Rental
from customer import Customer

def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air", 2023, ["Drama","Biography"]),
        Movie("Oppenheimer", 2023, ["Biography", "Drama"]),
        Movie("Frozen", 2013, ["Animation", "Adventure","Musical","Fantasy","Comedy"]),
        Movie("Bitconned", 2024, ["Crime", "Documentary"]),
        Movie("Particle Fever", 2013, ["Documentary"])
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    movies = make_movies()
    price_codes = [NEW_RELEASE, REGULAR, CHILDREN, NEW_RELEASE, REGULAR]
    days = 1
    for i in range(len(movies)):
        customer.add_rental(Rental(movies[i], days, price_codes[i]))
        days = (days + 2) % 5 + 1
    print(customer.statement())
