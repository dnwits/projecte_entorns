-- Inserts para Usuari
INSERT INTO Usuari (nom, email, contrasenya, rol) VALUES
('Anna Pérez', 'anna@example.com', '1234', 'usuari'),
('Valery Escobar', 'valery@example.com', '1234', 'usuari'),
('Admin Root', 'admin@example.com', '1234', 'admin');

-- Inserts para Pelicula
INSERT INTO Pelicula (titol, duracio, descripcio) VALUES
('Matrix', 136, 'Un hacker descobreix la veritat sobre la seva realitat.'),
('Avatar', 162, 'Una aventura èpica al planeta Pandora.'),
('El Señor de los Anillos', 178, 'Un viatge per destruir un anell poderós.');

-- Inserts para Sessio
INSERT INTO Sessio (id_pelicula, data_hora, sala) VALUES
(1, '2025-05-01 18:00:00', 'Sala 1'),
(1, '2025-05-02 20:30:00', 'Sala 2'),
(2, '2025-05-01 17:00:00', 'Sala 3'),
(3, '2025-05-03 19:00:00', 'Sala 1');

-- Inserts para Entrada
INSERT INTO Entrada (id_usuari, id_sessio, seient, preu) VALUES
(1, 1, 'A1', 8.50),
(1, 3, 'B3', 9.00),
(2, 2, 'C5', 8.50),
(3, 4, 'D2', 9.50);
