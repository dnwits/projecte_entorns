import mysql.connector

class DAOUser:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="cinema"
        )
        self.cursor = self.connection.cursor(dictionary=True)
    # Usuari (nom, email, contrasenya, rol)
    def validate_user(self, identifier, password):
        query = """
            SELECT * FROM User
            WHERE (nom = %s OR email = %s) AND password = %s
        """
        self.cursor.execute(query, (identifier, identifier, password))
        user = self.cursor.fetchone()
        return user

    def close_connection(self):
        self.cursor.close()
        self.connection.close()