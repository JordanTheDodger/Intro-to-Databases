from database import ConnectionFromPool
import psycopg2


class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self) -> str:
        return "User {}>".format(self.email)

    def save_to_db(self):
        """ using "with" with psycopg2.connection string it will automatically commit and close """
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s )',
                               (self.email, self.first_name, self.last_name))

        # """' you need to do .commit() and .close() '"""
        # connection = psycopg2.connect(user='postgres', password='1033', database='learning', host='localhost')
        # with connection.cursor() as cursor:
        #     cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s )',
        #                   (self.email, self.first_name, self.last_name))
        # connection.commit()
        # connection.close()

    @classmethod
    def load_from_db_by_email(cls, email):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
                usr_data = cursor.fetchone()
                return cls(id=usr_data[0], email=usr_data[1], first_name=usr_data[2], last_name=usr_data[3])
