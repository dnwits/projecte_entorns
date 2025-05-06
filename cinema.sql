-- Crear les taules
CREATE TABLE Usuari (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  contrasenya VARCHAR(255),
  rol ENUM('usuari','admin')
);

CREATE TABLE Pelicula (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titol VARCHAR(255),
  duracio INT,
  descripcio TEXT
);

CREATE TABLE Sessio (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_pelicula INT,
  data_hora DATETIME,
  sala VARCHAR(50),
  FOREIGN KEY (id_pelicula) REFERENCES Pelicula(id)
);

CREATE TABLE Entrada (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_usuari INT,
  id_sessio INT,
  seient VARCHAR(10),
  preu DECIMAL(5,2),
  FOREIGN KEY (id_usuari) REFERENCES Usuari(id),
  FOREIGN KEY (id_sessio) REFERENCES Sessio(id)
);
