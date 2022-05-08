from flask import request, flash
from importlib_metadata import metadata
from sqlalchemy import Column, Integer, String, create_engine,Table,MetaData,ForeignKey

# Database Constant Variable
SQLITE = 'sqlite'

# Table Constant Variable
COSTUMERS = 'costumers'


class Costumers:
    DB_ENGINE = {
        SQLITE: 'sqlite:///costumers'
    }

    db_engine = None

    def __init__(self,name='', city='',age=''):
        engine_url = self.DB_ENGINE[SQLITE]

        self.db_engine = create_engine(engine_url)

        print(self.db_engine)


    def create_db_table(self):
        metadata = MetaData()
        books = Table(COSTUMERS, metadata,
                        Column('id', Integer, primary_key = True),
                        Column('name', String(50), index = True , nullable = False),
                        Column('city', String(50) , nullable = False),
                        Column('age', Integer() , nullable = False),

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

    def addCostumer(self, name, city, age ):
       
        query = f"INSERT INTO {COSTUMERS}(name,city,age) VALUES ('{name}','{city}',{age})"
        self.execute_query(query)
        

    def removeCostumer(self, name):
            query = f"DELETE FROM {COSTUMERS} WHERE name = '{name}'"
            self.execute_query(query)
    
    def findCostumer(self, name):
            query = f"SELECT * FROM {COSTUMERS} WHERE name = '{name}'"
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
                        # print(row) # print(row[0], row[1], row[2])
                    result.close()
            # print("\n")
            return res 


    def print_all_data(self, table = COSTUMERS):
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