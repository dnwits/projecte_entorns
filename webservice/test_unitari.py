import unittest
from server import app

class TestEndpoints(unittest.TestCase):

    def setUp(self):
        # Configurar el client de proves de Flask
        self.app = app.test_client()
        self.app.testing = True
        self.token = None  # Variable per emmagatzemar el token JWT

    def test_login_correcte(self):
        # Substitueix per un usuari REAL que tinguis a la base de dades
        dades = {
            "email": "valery@example.com",
            "password": "abcd1234"  # contrasenya tal com guardada (sense hash) abcd1234
        }
        resposta = self.app.post('/login', json=dades)
        self.assertEqual(resposta.status_code, 200)
        resposta_json = resposta.get_json()
        self.assertEqual(resposta_json['coderesponse'], "1")
        self.assertIn('email', resposta_json)
        self.token = resposta_json.get("token")  # Guardar el token JWT

    def test_login_incorrecte(self):
        dades = {
            "email": "noexisteix@example.com",
            "password": "passwordincorrecta"
        }
        resposta = self.app.post('/login', json=dades)
        self.assertEqual(resposta.status_code, 400)
        resposta_json = resposta.get_json()
        self.assertEqual(resposta_json['coderesponse'], "0")

    def test_llistar_pelicules(self):
        # Primer, fer login per obtenir el token
        self.test_login_correcte()

        # Incloure el token al header
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        resposta = self.app.get('/pelicules', headers=headers)
        self.assertEqual(resposta.status_code, 200)
        pelicules = resposta.get_json()
        self.assertIsInstance(pelicules, list)

        if len(pelicules) > 0:
            self.assertIn('titol', pelicules[0])
            self.assertIn('duracio', pelicules[0])

if __name__ == '__main__':
    unittest.main()
