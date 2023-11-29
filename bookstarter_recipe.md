# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).


Table: books

Columns:
id | title | author_name
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- EXAMPLE
-- (file: spec/seeds_{table_name}.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE students RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO students (name, cohort_name) VALUES ('David', 'April 2022');
INSERT INTO students (name, cohort_name) VALUES ('Anna', 'May 2022');
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/book_stater.py)
class BookStore


# Repository class
# (in lib/book_starter_repository.py)
class BookStoreRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/book_starter.py)

class BookStore:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.author_name = ""


```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# Repository class
# (in lib/student_repository.py)

class BookStoreRepository():

    # Selecting all records
    # No arguments
    def __init__(self,conection)
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = BookStore(row["id"], row["title"], row["author_name"])
            books.append(item)
        Returns an array of Student objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
         rows = self._connection.execute('SELECT * from books WHERE id =%s', [author_name])
         row = rows[0]


    def create(book)
        self._connection.execute('INSERT INTO books (title, author_name) VALUES (%s, %s)', [
                                 book.title, book.author_name])
        return None


    def update_title(book)
        self._connection.execute(
            'UPDATE books SET title = %s WHERE id=%s', [book.title, book.id])
        return None

    def delete(id)
        self._connection.execute(
            'DELETE FROM books WHERE id = %s', [id])
        return None 

class BookStore():
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.authoer_name = author_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

  
    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author_name})"

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# bookstore tests
from lib.book_store import BookStore
#1
# construct book
    book = BookStore(1, "Test title", "Test author")
    assert book.id == 1
    assert book.title == "Test title"
    assert book.author_name == "Test author"
#2
#formatted book string
    book = BookStore(1, "Test title", "Test author")
    assert str(artist) == "Book(1, "Test title", "Test author")"
# repository tests
from lib.book_store_repository import BookStoreRepository
from lib.book_store import BookStore

db_connection.seed("sseeds/book_store.sql")
# 1
# Get all books

repo = BookStoreRepository(db_connection)
books = repo.all()
assert books= [
    BookStore('Nineteen Eighty-Four', 'George Orwell');
    BookStore('Mrs Dalloway', 'Virginia Woolf');
    BookStore('Emma', 'Jane Austen');
    BookStore('Dracula', 'Bram Stoker');
    BookStore('The Age of Innocence', 'Edith Wharton')
]

# 2
# Get a single student
repo = StudentRepository()
book = repo.find(3)
asser book == BookStore(3, "Emma", "Jane Austen")

#3
#create record
repository = BookStoreRepository(db_connection)
    repository.create(Books(None, "Book of Echo", "Ippo"))

    result = repository.all()
    assert result == [
    BookStore(1,'Nineteen Eighty-Four', 'George Orwell');
    BookStore(2,'Mrs Dalloway', 'Virginia Woolf');
    BookStore(3,'Emma', 'Jane Austen');
    BookStore(4,'Dracula', 'Bram Stoker');
    BookStore(5,'The Age of Innocence', 'Edith Wharton')
    BookStore(6,'Book of Echo', 'Ippo')
]

# delete records
repository = BookStoreRepository(db_connection)
    repository.update(book(3)) 

    result = repository.all()
    assert result ==[
    BookStore(1,'Nineteen Eighty-Four', 'George Orwell');
    BookStore(2,'Mrs Dalloway', 'Virginia Woolf');
    BookStore(4,'Dracula', 'Bram Stoker');
    BookStore(5,'The Age of Innocence', 'Edith Wharton')
]
#update record
repository = BookStoreRepository(db_connection)
    repository.create(Books("Book of Echo", 3))
    result = repository.all()
    assert result == [
    BookStore(1,'Nineteen Eighty-Four', 'George Orwell');
    BookStore(2,'Mrs Dalloway', 'Virginia Woolf');
    BookStore(3,'Book of Echo', 'Jane Austen');
    BookStore(4,'Dracula', 'Bram Stoker');
    BookStore(5,'The Age of Innocence', 'Edith Wharton')
]

```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
