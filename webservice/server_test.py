from flask import Flask, request, jsonify
from DAOUsuari import DAOUsuari

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    identifier = data.get('email')  # username or email
    password = data.get('password')
    dao_user = DAOUsuari()
    user = dao_user.validate_user(identifier, password)
    if user:
        return jsonify({
            "id": user['id'],
            "nom": user['nom'],
            "email": user['email'],
            "token": user['token'],
            "rol": user['rol'],  # Example role ID
            "msg": "Usuari Ok",
            "coderesponse": "1"
        }), 200
    else:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

if __name__ == '__main__':
    app.run(debug=True)