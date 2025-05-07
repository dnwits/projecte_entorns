import mysql.connector
from server_config import DB_CONFIG

class DAOUsuari:
    def __init__(self):
        self.connection = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.connection.cursor(dictionary=True)

    def validate_user(self, email, password):  # Valida un usuari pel seu email i contrasenya.
        try:
            query = "SELECT * FROM Usuari WHERE email = %s"
            self.cursor.execute(query, (email,))
            user = self.cursor.fetchone()
            # Comparar directament la contrasenya en text pla
            if user and user['contrasenya'] == password:
                return user
            return None
        finally:
            self.close_connection()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
