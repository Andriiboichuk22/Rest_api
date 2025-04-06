from dataclasses import dataclass


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    genre: str = ""
    pages: int = 0

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "pages": self.pages,
            "year": self.year,
        }


all_books = [
     Book(id=1, title="Пісок часу", author="Максим Ковальчук", genre="Фентезі", pages=320, year=2015),
     Book(id=2, title="Сліди на воді", author="Олександра Вербицька", genre="Детектив", pages=280, year=2020),
     Book(id=3, title="Місячна дорога", author="Антон Савенко", genre="Пригоди", pages=410, year=2018),
     Book(id=4, title="Тінь вітру", author="Наталія Романенко", genre="Психологічний роман", pages=365, year=2017),
     Book(id=5, title="Край світу", author="Ігор Лисенко", genre="Фантастика", pages=450, year=2019),
     Book(id=6, title="Шепіт лісу", author="Дарина Коваленко", genre="Містика", pages=390, year=2021)
]