-- My first table
-- Write a SQL script that creates a table users following these requirements:
CREATE TABLE if not exists users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);
