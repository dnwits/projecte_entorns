# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager, create_access_token
# from werkzeug.security import check_password_hash

# app = Flask(__name__)

# # Configuració de la base de dades
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/cinema'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['JWT_SECRET_KEY'] = 'secret-key'  # Canvia-ho per una clau segura
# db = SQLAlchemy(app)
# jwt = JWTManager(app)

# # Models
# class Usuari(db.Model):
#     __tablename__ = 'usuaris'
#     id = db.Column(db.Integer, primary_key=True)
#     nom = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     contrasenya = db.Column(db.String(200), nullable=False)
#     rol = db.Column(db.String(50), nullable=False)

# class Pelicula(db.Model):
#     __tablename__ = 'pelicules'
#     id = db.Column(db.Integer, primary_key=True)
#     titol = db.Column(db.String(100), nullable=False)
#     duracio = db.Column(db.Integer, nullable=False)
#     descripcio = db.Column(db.Text, nullable=False)

# class Sessio(db.Model):
#     __tablename__ = 'sessions'
#     id = db.Column(db.Integer, primary_key=True)
#     id_pelicula = db.Column(db.Integer, db.ForeignKey('pelicules.id'), nullable=False)
#     data_hora = db.Column(db.String(100), nullable=False)
#     sala = db.Column(db.String(50), nullable=False)

# class Entrada(db.Model):
#     __tablename__ = 'entrades'
#     id = db.Column(db.Integer, primary_key=True)
#     id_usuari = db.Column(db.Integer, db.ForeignKey('usuaris.id'), nullable=False)
#     id_sessio = db.Column(db.Integer, db.ForeignKey('sessions.id'), nullable=False)
#     seient = db.Column(db.String(10), nullable=False)
#     preu = db.Column(db.Float, nullable=False)

# # DAO
# class UsuariDAO:
#     @staticmethod
#     def obtenir_usuari_per_email(email):
#         return Usuari.query.filter_by(email=email).first()

# class PeliculaDAO:
#     @staticmethod
#     def obtenir_totes_les_pelicules():
#         return Pelicula.query.all()

# class SessioDAO:
#     @staticmethod
#     def obtenir_sessions_per_pelicula(id_pelicula):
#         return Sessio.query.filter_by(id_pelicula=id_pelicula).all()

# class EntradaDAO:
#     @staticmethod
#     def obtenir_entrades_per_usuari(id_usuari):
#         return Entrada.query.filter_by(id_usuari=id_usuari).all()

# # Endpoints
# @app.route("/login", methods=["POST"])
# def login():
#     data = request.get_json()
#     email = data.get("email")
#     contrasenya = data.get("contrasenya")

#     # Obtenir usuari des de la base de dades
#     usuari = UsuariDAO.obtenir_usuari_per_email(email)
#     if not usuari or not check_password_hash(usuari.contrasenya, contrasenya):
#         return jsonify({"error": "Credencials incorrectes"}), 401

#     # Crear token JWT
#     token = create_access_token(identity=usuari.id)
#     return jsonify({"token": token, "rol": usuari.rol})

# @app.route("/pelicules", methods=["GET"])
# def llistar_pelicules():
#     pelicules = PeliculaDAO.obtenir_totes_les_pelicules()
#     resultat = [
#         {"id": pelicula.id, "titol": pelicula.titol, "duracio": pelicula.duracio, "descripcio": pelicula.descripcio}
#         for pelicula in pelicules
#     ]
#     return jsonify(resultat)

# if __name__ == '__main__':
#     app.run(debug=True)