from flask import Flask, request, jsonify
import mysql.connector
from werkzeug.security import check_password_hash
from DAOUsuari import DAOUsuari
from DAOPelicula import DAOPelicula

app = Flask(__name__)

# Endpoints
@app.route('/login', methods=['POST'])
def login():  # Endpoint per validar l'usuari.
    data = request.get_json()
    identifier = data.get('email')  # email
    password = data.get('password')
    dao_user = DAOUsuari()
    user = dao_user.validate_user(identifier, password)
    if user:
        return jsonify({
            "id": user['id'],
            "nom": user['nom'],
            "email": user['email'],
            "rol": user['rol'],
            "msg": "Usuari validat correctament",
            "coderesponse": "1"
        }), 200
    else:
        return jsonify({
            "coderesponse": "0",
            "msg": "Credencials incorrectes"
        }), 400

@app.route('/pelicules', methods=['GET'])
def llistar_pelicules():  # Endpoint per llistar totes les pel·lícules.
    dao_pelicula = DAOPelicula()
    movies = dao_pelicula.get_all_movies()
    return jsonify(movies), 200


if __name__ == '__main__':
    app.run(debug=True)