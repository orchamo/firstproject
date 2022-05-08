from flask import request
from importlib_metadata import metadata
from matplotlib.style import available
from sqlalchemy import Column, Integer, String, create_engine,Table,MetaData,ForeignKey
import books
import costumers
# Database Constant Variable
SQLITE = 'sqlite'

# Table Constant Variable
LOANS = 'loans'


class Loans:
    DB_ENGINE = {
        SQLITE: 'sqlite:///loans'
    }

    db_engine = None

    def __init__(self,bookId='', costumerId='',loanDate='',returnDate=''):
        engine_url = self.DB_ENGINE[SQLITE]

        self.db_engine = create_engine(engine_url)

        print(self.db_engine)


    def create_db_table(self):
        metadata = MetaData()
        books = Table(LOANS, metadata,
                        Column('id', Integer, primary_key = True),
                        Column('bookId', String(50), index = True , nullable = False),
                        Column('costumerId', String(50) , nullable = False),
                        Column('loanDate', Integer() , nullable = False),
                        Column('returnDate', Integer() , nullable = False)

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

    def loan(self, bookId, costumerId, loanDate, returnDate ):
        # query = f"SELECT {books.BOOKS[id], costumers.COSTUMERS[id]} FROM {books.BOOKS}, {costumers.COSTUMERS} WHERE {books.BOOKS[availability]} = 'Yes' "
        query = f"INSERT INTO {LOANS}(bookId, costumerId, loanDate, returnDate) VALUES ('{bookId}','{costumerId}',{loanDate},{returnDate})"
        self.execute_query(query)

    def returnBook(self, name):
            query = f"DELETE FROM {LOANS} WHERE name = '{name}'"
            self.execute_query(query)
    
    def print_all_data(self, table = LOANS):
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
        return res