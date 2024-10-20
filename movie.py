from dataclasses import dataclass, field
from typing import Collection


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
