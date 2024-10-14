import unittest
from customer import Customer
from rental import Rental
from movie import Movie, NEW_RELEASE, REGULAR, CHILDREN


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", NEW_RELEASE)
        self.regular_movie = Movie("Air", REGULAR)
        self.childrens_movie = Movie("Frozen", CHILDREN)

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", REGULAR)
        self.assertEqual("Air", m.get_title())
        self.assertEqual(REGULAR, m.get_price_code())

    def test_new_release_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(rental), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(rental), 15.0)

    def test_regular_rental_price(self):
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_price(rental), 2.0)
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_price(rental), 6.5)

    def test_children_rental_price(self):
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_price(rental), 1.5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_price(rental), 4.5)

    def test_new_release_rental_points(self):
        rental = Rental(self.new_movie, 3)
        self.assertEqual(rental.get_rental_points(), 3)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_rental_points(), 5)

    def test_other_rental_points(self):
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_rental_points(), 1)
