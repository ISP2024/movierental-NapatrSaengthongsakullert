import unittest
from movie import Movie
from pricing import price_code_for_movie, NEW_RELEASE, REGULAR, CHILDREN


class TestPriceCodeForMovie(unittest.TestCase):
    def test_new_release(self):
        movie = Movie("NewFilm", 2024, ["Drama"])
        self.assertEqual(price_code_for_movie(movie), NEW_RELEASE)

    def test_children_movie(self):
        movie = Movie("ChildrenFilm", 2015, ["Children"])
        self.assertEqual(price_code_for_movie(movie), CHILDREN)

    def test_regular_movie(self):
        movie = Movie("RegularFilm", 2010, ["Drama", "Action"])
        self.assertEqual(price_code_for_movie(movie), REGULAR)


if __name__ == "__main__":
    unittest.main()
