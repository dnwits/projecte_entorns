# Endpoints del WebService

## Autenticació
### POST /login → Permet a un usuari iniciar sessió al sistema
- Request Body:
    ```
    {
    "email": "usuari@example.com",
    "password": "contrasenya123"
    }
    ```
- Resposta Exitosa (200 OK):
    ```
    {
    "token": "eyJhbGci...",
    "usuari": {
        "id": 123,
        "nom": "Nom Usuari",
        "email": "usuari@example.com",
        "rol": "usuari"
        }
    }
    ```
- Errors:
    - 401 Unauthorized: Credencials incorrectes
    - 400 Bad Request: Dades faltants o mal formatejades

### POST /register → Registra un nou usuari al sistema
- Request Body:
    ```
    {
    "nom": "Nom Usuari",
    "email": "nou@example.com",
    "contrasenya": "password123"
    }
    ```
- Resposta Exitosa (201 Created):
    ```
    {
    "id": 124,
    "nom": "Nom Usuari",
    "email": "nou@example.com",
    "rol": "usuari"
    }
    ```
- Errors:
    - 400 Bad Request: Dades faltants o email ja registrat
    - 422 Unprocessable Entity: Contrasenya no compleix requisits

## Catàleg
### GET /pelicules → Retorna el llistat de pel·lícules disponibles
- Resposta Exitosa (200 OK):
    ```
    [
        {
        "id": 1,
        "titol": "Avatar",
        "duracio": 162
        }
    ]
    ```

### GET /sessions/:id → Retorna les sessions disponibles per una pel·lícula específica
- Paràmetres URL: id: ID de la pel·lícula.
- Resposta Exitosa (200 OK):
    ```
    [
        {
        "id": 15,
        "data": "2023-05-20",
        "hora": "18:30",
        "sala": 3
        },
        {
        "id": 16,
        "data": "2023-05-20",
        "hora": "22:15",
        "sala": 3
        }
    ]
    ```
- Errors:
    - 404 Not Found: Pel·lícula no trobada

## Gestió d'Entrades
### POST /entrades/reservar → Realitza una reserva d'entrades.
- Headers:Authorization: Bearer <token>
- Request Body:
    ```
    {
    "id_sessio": 1,
    "seient": "A1",
    "preu": 8.50
    }
    ```
- Resposta Exitosa (201 Created):
    ```
    {
    "id": 456,
    "id_usuari": 1,
    "id_sessio": 15,
    "seient": "A1",
    "preu": 8.50
    }
    ```
- Errors:
    - 400 Bad Request: Dades incorrectes
    - 409 Conflict: No hi ha prou places disponibles
    
### GET /entrades/historial:id_usuari → Retorna l'historial de reserves de l'usuari.
- Resposta Exitosa (200 OK):
    ```
    {
    "id": 456,
    "pelicula": "Interstellar",
    "sessio": "2023-05-20T18:30:00",
    "sala": "Sala 3",
    "seient": "A12",
    "preu": 9.50
    }
    ```
