import sqlite3

def create_connection(db_file):
    """Oppretter en ny connection til databasen"""

    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection


class Database:

    def __init__(self, db_file):
        self.connection = create_connection(db_file)
        self.cursor = self.connection.cursor()

    def run_script(self, sql_file):
        """Utfører et sql-script"""
        with open("kaffeDB.sql", encoding="utf-8") as file:
            script = file.read()
            self.cursor.executescript(script)
            self.commit()

    def close(self):
        """Lukker databasen"""
        self.connection.close()

    def execute(self, query, args=None):
        """Brukes til å utføre SQL-spørringer"""

        if not args:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, args)

    def fetchone(self):
        """Henter siste resultat fra en spørring"""
        return self.cursor.fetchone()

    def fetchmany(self, count):
        """Henter et bestemt antaøø resultat fra en spørring"""
        return self.cursor.fetchmany(count)

    def fetchall(self):
        """Henter alle resultat fra en spørring"""
        return self.cursor.fetchall()

    def commit(self):
        """Committer til databasen"""
        self.connection.commit()

