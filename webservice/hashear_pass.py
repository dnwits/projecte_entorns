import mysql.connector
from hash import hash_text
from server_config import DB_CONFIG

connection = mysql.connector.connect(**DB_CONFIG)
cursor = connection.cursor()

# Actualitzar totes les contrasenyes a hash
cursor.execute("SELECT id, contrasenya FROM Usuari")
users = cursor.fetchall()

for user in users:
    user_id, plain_password = user
    hashed_password = hash_text(plain_password)
    cursor.execute("UPDATE Usuari SET contrasenya = %s WHERE id = %s", (hashed_password, user_id))

connection.commit()
cursor.close()
connection.close()
print("Contrasenyes actualitzades a hash.")