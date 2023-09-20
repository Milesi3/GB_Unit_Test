import pytest
from unittest.mock import Mock
from book_repository import BookService

@pytest.fixture
def book_repository_mock():
    return Mock()

def test_get_book_title(book_repository_mock):
    # Arrange
    book_id = 1
    expected_title = "Sample Book Title"
    book_repository_mock.get_book.return_value = {'title': expected_title}
    book_service = BookService(book_repository_mock)

    actual_title = book_service.get_book_title(book_id)

    assert actual_title == expected_title
    book_repository_mock.get_book.assert_called_once_with(book_id)


if __name__ == '__main__':
    pytest.main()