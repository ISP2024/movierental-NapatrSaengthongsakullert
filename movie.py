from dataclasses import dataclass, field
from typing import Collection, Optional
import csv


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """

    title: str
    year: int
    genre: Collection[str] = field(default_factory=list)

    def is_genre(self, genre_name: str) -> bool:
        for genre in self.genre:
            if genre.lower() == genre_name.lower():
                return True
        return False

    def __str__(self):
        return f"{self.title} ({self.year})"


class MovieCatalog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._movies = {}
            cls._instance._load_movies()
        return cls._instance

    def _load_movies(self):
        """Load movies from the CSV file into memory."""
        with open("movies.csv", mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                if len(row) < 4:
                    continue

                title = row[1].strip()
                year = int(row[2].strip())
                genres = [genre.strip() for genre in row[3].split('|')]

                movie = Movie(title, year, genres)
                self._movies[(title.lower(), year)] = movie

    def get_movie(self, title: str, year: Optional[int] = None) -> Optional[Movie]:
        """Get a movie by title and optional year."""
        key = (title.lower(), year) if year is not None else (title.lower(), None)

        if year is not None:
            return self._movies.get(key)

        for (movie_title, _), movie in self._movies.items():
            if movie_title == title.lower():
                return movie

        return None
