from lib.book_store_repository import BookStoreRepository
from lib.book_store import BookStore

# 1
# Get all books
def test_list_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookStoreRepository(db_connection)
    books = repo.all()
    assert books == [ BookStore(1,'Nineteen Eighty-Four', 'George Orwell'), BookStore(2,'Mrs Dalloway', 'Virginia Woolf'), BookStore(3,'Emma', 'Jane Austen'), BookStore(4,'Dracula', 'Bram Stoker'), BookStore(5,'The Age of Innocence', 'Edith Wharton')]

# 2
# Get a single book
def test_single_book(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookStoreRepository(db_connection)
    book = repo.find(3)
    assert book == BookStore(3, "Emma", "Jane Austen")
#3
#create record
def test_create_book(db_connection):
    repository = BookStoreRepository(db_connection)
    repository.create(BookStore(None, "Book of Echo", "Ippo"))
    result = repository.all()
    assert result == [BookStore(1,'Nineteen Eighty-Four', 'George Orwell'),BookStore(2,'Mrs Dalloway', 'Virginia Woolf'),BookStore(3,'Emma', 'Jane Austen'),BookStore(4,'Dracula', 'Bram Stoker'),BookStore(5,'The Age of Innocence', 'Edith Wharton'), BookStore(6,'Book of Echo', 'Ippo')]
#4
# delete records
def test_delete_record(db_connection):
    repository = BookStoreRepository(db_connection)
    repository.delete(3) 
    result = repository.all()
    assert result ==[ BookStore(1,'Nineteen Eighty-Four', 'George Orwell'),BookStore(2,'Mrs Dalloway', 'Virginia Woolf'),BookStore(4,'Dracula', 'Bram Stoker'),BookStore(5,'The Age of Innocence', 'Edith Wharton'),BookStore(6,'Book of Echo', 'Ippo')]
#5
#update record
def test_update_record(db_connection):
    repository = BookStoreRepository(db_connection)
    repository.update_title(2, "Book of Echo")
    result = repository.all()
    assert result == [BookStore(1,'Nineteen Eighty-Four', 'George Orwell'),BookStore(4,'Dracula', 'Bram Stoker'),BookStore(5,'The Age of Innocence', 'Edith Wharton'),BookStore(6,'Book of Echo', 'Ippo'), BookStore(2,'Book of Echo', 'Virginia Woolf')]
