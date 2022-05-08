from flask import request
from importlib_metadata import metadata
from sqlalchemy import Column, Integer, String, create_engine,Table,MetaData,ForeignKey

# Database Constant Variable
SQLITE = 'sqlite'

# Table Constant Variable
BOOKS = 'books'


class BooksDatabase:
    DB_ENGINE = {
        SQLITE: 'sqlite:///books'
    }

    db_engine = None


    def __init__(self,name='', author='', year='',book_type=''):
        engine_url = self.DB_ENGINE[SQLITE]

        self.db_engine = create_engine(engine_url)

        print(self.db_engine)


    def create_db_table(self):
        metadata = MetaData()
        books = Table(BOOKS, metadata,
                        Column('id', Integer, primary_key = True),
                        Column('name', String(50), index = True , nullable = False),
                        Column('author', String(50) , nullable = False),
                        Column('year', Integer() , nullable = False),
                        Column('book_type', Integer(), nullable = False),
                        Column('availability', String(50))

                        )
        try:
            metadata.create_all(self.db_engine)
            print("Table created")
        except Exception as e:
            print("error occured while table creation")
            print(e)

    def execute_query(self, query=''):
        if query == '' : return

        print (query)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    def addBook(self, name, author, year,book_type):
        query = f"INSERT INTO {BOOKS}(name, author,year,book_type, availability) VALUES ('{name}','{author}',{year},{book_type},'available')"
        self.execute_query(query)
  

    def removeBook(self, name):
            query = f"DELETE FROM {BOOKS} WHERE name = '{name}'"
            self.execute_query(query)
    
    def print_all_data(self, table = BOOKS):
        query = f"SELECT * FROM '{table}';"
        print(query)
        res = []
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    res.append( row)
                result.close()
        # print("\n")
        return res

    def findBookStatus(self, name):
            query = f"SELECT availability FROM {BOOKS} WHERE name = '{name}'"
            print(query)
            res = []
            with self.db_engine.connect() as connection:
                try:
                    result = connection.execute(query)
                except Exception as e:
                    print(e)
                else:
                    for row in result:
                        res.append( row)
                    result.close()
            ress = res[0]
            ress = str(ress).strip('(').strip(')').strip(',')
            print (ress)
            return ress

    def updateBookStatus(self, name ,availability):
        query = f"UPDATE {BOOKS} SET availability = {availability} WHERE name = {name}"
        self.execute_query(query)