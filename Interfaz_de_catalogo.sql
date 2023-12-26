-- Crea la base de datos utilizando UTF-8
CREATE DATABASE IF NOT EXISTS interfaz_de_catalogo CHARACTER SET utf8 COLLATE utf8_general_ci;

-- Selecciona la base de datos recién creada
USE interfaz_de_catalogo;

CREATE TABLE productos (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    modelo VARCHAR(20),
    precio int,
    cantidad int
);

select * from productos;
drop table productos;
