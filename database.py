import psycopg2
from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1, 1, database="learning", user="postgres", password="1033",
                                            host="localhost")

"""getting one connection from connection pool and keep track of connection that it represents"""


class ConnectionFromPool():
    def __int__(self):
        self.connection = None


"""at the enter of with statement enter is called and at the return exit is called"""


def __enter__(self):
    self.connection = connection_pool.getconn()
    return self.connection


def __exit__(self, exc_type, exc_val, exc_tb):
    self.connection.commit()
    connection_pool.putconn(self.connection)
