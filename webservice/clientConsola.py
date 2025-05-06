import requests

BASE_URL = "http://127.0.0.1:5000"  # URL del servidor Flask

def login():

    #Funció per provar l'endpoint de login.
    email = input("Introdueix el teu email: ")
    password = input("Introdueix la teva contrasenya: ")

    data = {
        "email": email,
        "password": password
    }

    response = requests.post(f"{BASE_URL}/login", json=data)
    if response.status_code == 200:
        print("Login correcte!")
        print("Resposta del servidor:", response.json())
    else:
        print("Error en el login.")
        print("Resposta del servidor:", response.json())

def llistar_pelicules():
    #Funció per provar l'endpoint de llistar pel·lícules.

    response = requests.get(f"{BASE_URL}/pelicules")
    if response.status_code == 200:
        print("Llistat de pel·lícules:")
        for pelicula in response.json():
            print(f"- {pelicula['titol']} (Duració: {pelicula['duracio']} minuts)")
    else:
        print("Error en obtenir les pel·lícules.")
        print("Resposta del servidor:", response.json())

def main():
    #Menú principal per provar els endpoints.

    while True:
        print("\n--- Client per provar els endpoints ---")
        print("1. Login")
        print("2. Llistar pel·lícules")
        print("3. Sortir")
        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            login()
        elif opcio == "2":
            llistar_pelicules()
        elif opcio == "3":
            print("Sortint del client...")
            break
        else:
            print("Opció no vàlida. Torna-ho a intentar.")

if __name__ == "__main__":
    main()