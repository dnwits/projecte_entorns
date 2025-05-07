import mysql.connector
from server_config import DB_CONFIG

class DAOPelicula:
    def __init__(self):
        self.connection = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.connection.cursor(dictionary=True)

    def get_all_movies(self):  # Retorna totes les pel·lícules de la base de dades.
        try:
            query = "SELECT * FROM Pelicula"
            self.cursor.execute(query)
            movies = self.cursor.fetchall()
            return movies
        finally:
            self.close_connection()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
