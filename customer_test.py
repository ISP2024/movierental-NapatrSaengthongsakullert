import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie, NEW_RELEASE, REGULAR, CHILDREN


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:
    	c = a customer
    	movies = list of some movies
    	"""
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", NEW_RELEASE)
        self.regular_movie = Movie("CitizenFour", REGULAR)
        self.childrens_movie = Movie("Frozen", CHILDREN)

    @unittest.skip("No convenient way to test")
    def test_billing():
        # no convenient way to test billing since its buried in the statement() method.
        pass

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

    def test_total_charge(self):
        self.c.add_rental(Rental(self.new_movie, 4))
        self.c.add_rental(Rental(self.regular_movie, 3))
        self.c.add_rental(Rental(self.childrens_movie, 5))
        self.assertEqual(self.c.get_total_charge(), 20.0)

    def test_total_rental_point(self):
        self.c.add_rental(Rental(self.new_movie, 4))
        self.c.add_rental(Rental(self.regular_movie, 3))
        self.c.add_rental(Rental(self.childrens_movie, 5))
        self.assertEqual(self.c.get_total_rental_points(self.c.rentals), 6)