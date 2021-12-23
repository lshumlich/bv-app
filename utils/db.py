
import psycopg2

dbCreds = {
    'host': 'localhost',
    'port': 5433,
    'dbname': 'bowvalley',
    'user': 'postgres',
    'password': 'January01'
}


class DB:
    def __init__(self, dbCreds=dbCreds):
        self.connection = None
        self.connection = psycopg2.connect(
            host=dbCreds['host'],
            port=dbCreds['port'],
            dbname=dbCreds['dbname'],
            user=dbCreds['user'],
            password=dbCreds['password']
        )
        self.debug = False

    def close(self):
        """Close the cursor and the database connection."""
        if (hasattr(self, 'connection')):
            if (hasattr(self, 'cursor')):
                self.cursor.close()
            self.connection.close()

    def select(self, select):
        self.result = None
        try:
            self.cursor = self.connection.cursor()
            # self.query = "SELECT city FROM public.canadacities"
            # self.query = "SELECT * FROM pg_catalog.pg_tables"
            self.cursor.execute(select)
            self.result = [dict((self.cursor.description[i][0], value)
                                for i, value in enumerate(row)) for row in self.cursor.fetchall()]

        finally:
            self.connection.commit()
            if (hasattr(self, 'cursor')):
                self.cursor.close()
