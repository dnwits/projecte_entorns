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
# class DAOPelicula:
#     def __init__(self):
#         self.connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="root",
#             database="cinema"
#         )
#         self.cursor = self.connection.cursor(dictionary=True)
#     # def listarPelicula(self, id, titol, ):
#     #     query = """
#     #         SELECT * FROM Pelicula
#     #     """
#     #     self.cursor.execute(query, (self, id, titol))
#     #     pelis = self.cursor.fetchone()
#     #     return pelis
#     def get_all_movies(self): # Retorna totes les pel·lícules de la base de dades.
        
#         query = "SELECT * FROM Pelicula"
#         cursor.execute(query)
#         movies = cursor.fetchall()
#         return movies
        
#         cursor.close()
#         connection.close()
            
#     def close_connection(self):
#         self.cursor.close()
#         self.connection.close()