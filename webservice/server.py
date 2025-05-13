from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from DAOUsuari import DAOUsuari
from DAOPelicula import DAOPelicula

app = Flask(__name__)

# Configuració del secret per JWT
app.config['JWT_SECRET_KEY'] = 'secret-key'  # Canvia-ho per una clau segura
jwt = JWTManager(app)

# Endpoints
@app.route('/login', methods=['POST'])
def login():  # Endpoint per validar l'usuari.
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    dao_user = DAOUsuari()
    user = dao_user.validate_user(email, password)
    if user:
        # Generar token JWT
        token = create_access_token(identity=user['id'])
        return jsonify({
            "id": user['id'],
            "nom": user['nom'],
            "email": user['email'],
            "rol": user['rol'],
            "token": token,
            "msg": "Usuari validat correctament",
            "coderesponse": "1"
        }), 200
    else:
        return jsonify({
            "coderesponse": "0",
            "msg": "Credencials incorrectes"
        }), 400

@app.route('/register', methods=['POST'])
def register():  # Endpoint per registrar un nou usuari.
    data = request.get_json()
    nom = data.get('nom')
    email = data.get('email')
    password = data.get('password')
    rol = data.get('rol', 'usuari')  # Per defecte, el rol és "usuari"
    dao_user = DAOUsuari()
    success = dao_user.register_user(nom, email, password, rol)
    if success:
        return jsonify({"msg": "Usuari registrat correctament"}), 201
    else:
        return jsonify({"msg": "Error en registrar l'usuari"}), 400

@app.route('/pelicules', methods=['GET'])
@jwt_required()  # Requereix autenticació
def llistar_pelicules():  # Endpoint per llistar totes les pel·lícules.
    dao_pelicula = DAOPelicula()
    movies = dao_pelicula.get_all_movies()
    return jsonify(movies), 200

@app.route('/perfil', methods=['GET'])
@jwt_required()  # Requereix autenticació
def perfil():  # Endpoint per obtenir el perfil de l'usuari autenticat.
    user_id = get_jwt_identity()
    dao_user = DAOUsuari()
    user = dao_user.get_user_by_id(user_id)
    if user:
        return jsonify({
            "id": user['id'],
            "nom": user['nom'],
            "email": user['email'],
            "rol": user['rol']
        }), 200
    else:
        return jsonify({"msg": "Usuari no trobat"}), 404

if __name__ == '__main__':
    app.run(debug=True)