from lib.book_store import BookStore
class BookStoreRepository():

    # Selecting all records
    # No arguments
    def __init__(self,connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = BookStore(row["id"], row["title"], row["author_name"])
            books.append(item)
        return books

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(self, id):
        rows = self._connection.execute('SELECT * from books WHERE id =%s', [id])
        row = rows[0]
        return BookStore(row["id"], row["title"], row["author_name"])

    def create(self, book):
        self._connection.execute('INSERT INTO books (title, author_name) VALUES (%s, %s)', [
                                 book.title, book.author_name])
        return None


    def update_title(self, bookid,bookupdated):
        self._connection.execute(
            'UPDATE books SET title = %s WHERE id=%s', [bookupdated, bookid])
        return None

    def delete(self, id):
        self._connection.execute(
            'DELETE FROM books WHERE id = %s', [id])
        return None 