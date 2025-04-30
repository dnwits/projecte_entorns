# Cas d’ús detallat: Login d’usuari

| **Nom del cas d’ús** | Login d’usuari |
|----------------------|----------------|
| **Actors principals** | Usuari |
| **Actors secundaris** | Sistema (Webservice Flask + BBDD MySQL) |
| **Objectiu** | Permetre a l’usuari accedir al sistema introduint les seves credencials |
| **Pre-condicions** | L’usuari ha d’estar registrat a la base de dades amb email i contrasenya |
| **Post-condicions** | L’usuari accedeix al sistema si les credencials són correctes |

## Descripció
Aquest cas d’ús permet a un usuari autenticar-se al sistema introduint el seu email i contrasenya des de l’aplicació per consola. Si les credencials són vàlides, el sistema li permet accedir a les funcionalitats disponibles segons el seu rol.

## Flux principal (escenari correcte)

1. L’usuari obre l’aplicació per consola.
2. El sistema demana **email** i **contrasenya**.
3. L’usuari introdueix les seves credencials.
4. L’aplicació envia una **petició HTTP POST** al Webservice Flask amb les credencials.
5. El Webservice consulta la base de dades per verificar l’usuari i la contrasenya.
6. Si les credencials són vàlides:
   - El sistema retorna una **resposta JSON amb èxit**.
   - L’aplicació consola mostra un missatge de "Login correcte" i accés al sistema.

## Flux alternatiu (error de credencials)

- Si les credencials no són vàlides:
   - El sistema retorna una **resposta JSON d’error**.
   - L’aplicació consola mostra un missatge "Email o contrasenya incorrectes".
   - L’usuari pot intentar-ho de nou o sortir.

## Flux alternatiu (usuari no registrat)

- Si l’email no existeix a la base de dades:
   - El sistema retorna una **resposta JSON indicant que l’usuari no existeix**.
   - L’aplicació consola mostra un missatge "Usuari no registrat".
   - L’usuari pot optar per registrar-se.

## Requisits funcionals relacionats

- **RF01**: Validació d’usuari i contrasenya.
- **RF02**: Gestió d’errors de login.


