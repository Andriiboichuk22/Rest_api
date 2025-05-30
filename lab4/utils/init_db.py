import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from books.models import db, Book


def seed_books():
    if db.session.query(Book).count() == 0:
        books = [
            Book(title="Shadows of the Forgotten", author="F. Scott Fitzgerald", genre="Fiction", pages=218, year=1925),
            Book(title="Echoes of Tomorrow", author="George Orwell", genre="Dystopian", pages=328, year=1949),
            Book(title="Whispers in the Garden", author="Harper Lee", genre="Fiction", pages=281, year=1960),
            Book(title="Beneath the Crimson Sky", author="J.D. Salinger", genre="Fiction", pages=277, year=1951),
            Book(title="Hearts Entwined", author="Jane Austen", genre="Romance", pages=279, year=1813)
        ]

        db.session.add_all(books)
        db.session.commit()
        print("Database seeded with books.")
    else:
        print("Books already exist in the database.")


if __name__ == '__main__':
    from app import app

    with app.app_context():
        seed_books()