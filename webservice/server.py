from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token
from models import Usuari
from werkzeug.security import check_password_hash

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    contrasenya = data.get("contrasenya")
    usuari = Usuari.query.filter_by(email=email).first()
    if not usuari or not check_password_hash(usuari.contrasenya, contrasenya):
        return jsonify({"error": "Credencials incorrectes"}), 401
    token = create_access_token(identity=usuari.id)
    return jsonify({"token": token})
if __name__ == '__main__':
    app.run(debug=True)