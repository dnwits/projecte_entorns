# Descripció del projecte
El projecte consisteix en una aplicació que permet als usuaris consultar, reservar i gestionar entrades de cinema. El sistema permet visualitzar la cartellera, seleccionar pel·lícules, escollir seients i fer reserves. El frontend es desenvoluparà per consola.

## Requeriments Tècnics

## 1. Backend (Servidor i Gestió de Dades)

El backend serà el cor del sistema, encarregat de gestionar dades, usuaris i la lògica del sistema.

### a. Requisits del servidor

- **Allotjament:** Entorn local (localhost)
- **Base de dades:** MySQL (phpMyAdmin)
- **Sistema operatiu del servidor:** Windows/Linux (entorn local)
- **APIs i serveis web:** RESTFul amb Flask

### b. Llenguatges de programació

- Python

### c. Seguretat

- Autenticació i autorització amb JSON Web Tokens (JWT)
- Protecció de credencials i dades sensibles
- Còpies de seguretat manualment a phpMyAdmin (exportacions periòdiques)

## 2. Frontend

### a. Tipus de Clients

- Consola Python (CLI). Escriptori.
- **Llenguatge de programació:** Python (CLI)
- **Compatibilitat dispositius:** Ordinador (Windows, Linux, Mac)

## 3. Requisits Generals

### a. Gestió d'usuari i autenticació

- **Rols d’usuari:** Admin, Usuari *(ampliable si calgués)*
- **Base de dades:** MySQL (phpMyAdmin)
- **Seguretat:** Autenticació per email i contrasenya, amb gestió de token (JWT)

### b. Emmagatzematge local i sincronització

- **Dades que es guarden en local:** Token JWT, id usuari, email
- **Seguretat:** Connexió local, validació amb token

### c. Gestió d’accessibilitat

- No aplica per aplicació de consola (CLI)

## 4. Requisits d'Infraestructura

- **Xarxa:** Localhost (127.0.0.1)
- **Espai d’emmagatzematge al núvol:** No aplica
- **APIs de tercers:** No es fan servir

## 5. Requisits del Procés de Desenvolupament

- **IDE’s:** Visual Studio Code
- **Extensions VSCode:** Python, Python Snippets
- **Control de Versions:** Git, GitHub
- **Mètode de desenvolupament:** Metodologia àgil (Scrum o Kanban)
- **Proves de qualitat (QA):** Tests unitaris amb unittest


## Model E/R
[Model E/R](diagrames/d_model_entitat_relacio.mermaid)

## BBDD Mysql
[BBDD Mysql](cinema.sql) <br>
[Inserts BBDD](inserts.sql)

## Diagrama d'arquitectura Client / Servidor
[Diagrama d'arquitectura Client / Servidor](diagrames/d_arquitectura_cliente_server.mermaid)

## Descripció dels End-points del WebService
[Descripció dels End-points del WebService](documentacio/end-points_desc.md)

## Diagrama de classes del Backend
[Diagrama de classes del Backend](diagrames/d_classes_backend.mermaid)

## Diagrama de seqüència del Login
[Diagrama de seqüència del Login](diagrames/d_secuencia_login.mermaid)

## Wireframes del Login i les següents pantalles
[Wireframe general del servei](diagrames/d_wireframe_general.mermaid) <br>
[Wireframe Login](diagrames/d_wireframe_login.mermaid) <br>
[Wireframe Pantalla principal](diagrames/d_wireframe_pprincipal.mermaid)

## Desenvolupament d'una part petita de codi
[Servidor](webservice/server.py)
[Client](webservice/clientConsola.py)

## Cas d'ús detallat a escollir
[Cas d'ús de Login](documentacio/cas_dus.md)