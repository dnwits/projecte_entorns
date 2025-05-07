import mysql.connector
from server_config import DB_CONFIG
from hash import hash_text

class DAOUsuari:
    def __init__(self):
        self.connection = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.connection.cursor(dictionary=True)

    def validate_user(self, email, password):  # Valida un usuari pel seu email i contrasenya.
        try:
            query = "SELECT * FROM Usuari WHERE email = %s"
            self.cursor.execute(query, (email,))
            user = self.cursor.fetchone()
            # Comparar la contrasenya hashada
            if user and user['contrasenya'] == hash_text(password):
                return user
            return None
        finally:
            self.close_connection()

    def register_user(self, nom, email, password, rol):  # Registra un nou usuari.
        try:
            hashed_password = hash_text(password)
            query = "INSERT INTO Usuari (nom, email, contrasenya, rol) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (nom, email, hashed_password, rol))
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            self.close_connection()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()