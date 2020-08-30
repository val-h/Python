import sqlite3
from sqlite3.dbapi2 import Cursor

def intro():
    # Coonect to a database
    connection = sqlite3.connect('mydata.db')
    cursor = connection.cursor()

    # Create a table in the database
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS persons (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    )
    """)

    cursor.execute("""
    INSERT INTO persons VALUES
    (1, 'Paul', 'Smith', 24),
    (2, 'Mark', 'Johnson', 42),
    (3, 'Anna', 'Smith', 34)
    """)

    cursor.execute("""
    SELECT * FROM persons
    WHERE last_name = 'Smith'
    """)

    rows = cursor.fetchall()
    print(rows)

    connection.commit()
    connection.close()

def oop_database():

    class Person:
        def __init__(self, id_num=-1, first='', last='', age=-1):
            self.id_num = id_num
            self.first = first
            self.last = last
            self.age = age
            self.connection = sqlite3.connect('mydata.db')
            self.cursor = self.connection.cursor()

        def load_person(self, id_num):
            self.cursor.execute(f"""
            SELECT * FROM persons
            WHERE id = {id_num}
            """)

            results = self.cursor.fetchone()

            self.id_num = id_num
            self.first = results[1]
            self.last = results[2]
            self.age = results[3]

        def insert_person(self):
            self.cursor.execute(f"""
            INSERT INTO persons VALUES
            ({self.id_num}, '{self.first}', '{self.last}', {self.age})
            """)
            # quotes are used in the arguments since python passes the value
            # as a string but with the plain format of a string >> Joe, and
            # sql looks for a column with the name Joe...

            self.connection.commit()

        def __str__(self):
            return f'{self.first} {self.last}, {self.age}y-old with id:{self.id_num}'

    p1 = Person(7, 'Joe', 'Torn', 67)
    p1.insert_person()
    print(p1)

# Load some data
#intro()

oop_database()
