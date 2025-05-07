# Descripció del projecte
El projecte consisteix en una aplicació que permet als usuaris consultar, reservar i gestionar entrades de cinema. El sistema permet visualitzar la cartellera, seleccionar pel·lícules, escollir seients i fer reserves. El frontend es desenvoluparà per consola.

## Requeriments Tècnics
- Interfície: Aplicació per consola (CLI)
- Backend: Python amb Flask (WebService REST)
- Base de Dades: MySQL (phpMyAdmin)
- Autenticació: JSON Web Tokens (JWT)
- Control de versions: Git + GitHub
- Testing: unittest

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