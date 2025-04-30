-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-04-2025 a las 13:17:56
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cinema`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `entrada`
--

CREATE TABLE `entrada` (
  `id` int(11) NOT NULL,
  `id_usuari` int(11) DEFAULT NULL,
  `id_sessio` int(11) DEFAULT NULL,
  `seient` varchar(10) DEFAULT NULL,
  `preu` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `entrada`
--

INSERT INTO `entrada` (`id`, `id_usuari`, `id_sessio`, `seient`, `preu`) VALUES
(1, 1, 1, 'A1', 8.50),
(2, 1, 3, 'B3', 9.00),
(3, 2, 2, 'C5', 8.50),
(4, 3, 4, 'D2', 9.50);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pelicula`
--

CREATE TABLE `pelicula` (
  `id` int(11) NOT NULL,
  `titol` varchar(255) DEFAULT NULL,
  `duracio` int(11) DEFAULT NULL,
  `descripcio` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pelicula`
--

INSERT INTO `pelicula` (`id`, `titol`, `duracio`, `descripcio`) VALUES
(1, 'Matrix', 136, 'Un hacker descobreix la veritat sobre la seva realitat.'),
(2, 'Avatar', 162, 'Una aventura èpica al planeta Pandora.'),
(3, 'El Señor de los Anillos', 178, 'Un viatge per destruir un anell poderós.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sessio`
--

CREATE TABLE `sessio` (
  `id` int(11) NOT NULL,
  `id_pelicula` int(11) DEFAULT NULL,
  `data_hora` datetime DEFAULT NULL,
  `sala` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `sessio`
--

INSERT INTO `sessio` (`id`, `id_pelicula`, `data_hora`, `sala`) VALUES
(1, 1, '2025-05-01 18:00:00', 'Sala 1'),
(2, 1, '2025-05-02 20:30:00', 'Sala 2'),
(3, 2, '2025-05-01 17:00:00', 'Sala 3'),
(4, 3, '2025-05-03 19:00:00', 'Sala 1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuari`
--

CREATE TABLE `usuari` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `contrasenya` varchar(255) DEFAULT NULL,
  `rol` enum('usuari','admin') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `usuari`
--

INSERT INTO `usuari` (`id`, `nom`, `email`, `contrasenya`, `rol`) VALUES
(1, 'Anna Pérez', 'anna@example.com', '1234abcd', 'usuari'),
(2, 'Valery Escobar', 'valery@example.com', 'abcd1234', 'usuari'),
(3, 'Admin Root', 'admin@example.com', 'adminpass', 'admin');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `entrada`
--
ALTER TABLE `entrada`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuari` (`id_usuari`),
  ADD KEY `id_sessio` (`id_sessio`);

--
-- Indices de la tabla `pelicula`
--
ALTER TABLE `pelicula`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `sessio`
--
ALTER TABLE `sessio`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_pelicula` (`id_pelicula`);

--
-- Indices de la tabla `usuari`
--
ALTER TABLE `usuari`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `entrada`
--
ALTER TABLE `entrada`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `pelicula`
--
ALTER TABLE `pelicula`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `sessio`
--
ALTER TABLE `sessio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuari`
--
ALTER TABLE `usuari`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `entrada`
--
ALTER TABLE `entrada`
  ADD CONSTRAINT `entrada_ibfk_1` FOREIGN KEY (`id_usuari`) REFERENCES `usuari` (`id`),
  ADD CONSTRAINT `entrada_ibfk_2` FOREIGN KEY (`id_sessio`) REFERENCES `sessio` (`id`);

--
-- Filtros para la tabla `sessio`
--
ALTER TABLE `sessio`
  ADD CONSTRAINT `sessio_ibfk_1` FOREIGN KEY (`id_pelicula`) REFERENCES `pelicula` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
