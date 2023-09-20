from abc import ABC, abstractmethod

class BookRepository(ABC):
    @abstractmethod
    def get_book(self, book_id):
        pass

# book_service.py

class BookService:
    def __init__(self, repository):
        self.repository = repository

    def get_book_title(self, book_id):
        book = self.repository.get_book(book_id)
        return book['title']