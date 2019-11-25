import psycopg2
from psycopg2 import pool


class ConnectionPool():
    def __int__(self):
        self.connection_pool = pool.SimpleConnectionPool(1, 1, database="learning", user="postgres", password="1033",
                                                         host="localhost")

    def __enter__(self):
        return self.connection_pool.getconn()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
