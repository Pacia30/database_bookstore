from lib.book_store import BookStore
#1
# construct book
def test_construct_book():
    book = BookStore(1, "Test title", "Test author")
    assert book.id == 1
    assert book.title == "Test title"
    assert book.author_name == "Test author"

#2
#formatted book string
def test_formatted_book():
    book = BookStore(1, "Test title", "Test author")
    assert str(book) == "Book(1, Test title, Test author)"