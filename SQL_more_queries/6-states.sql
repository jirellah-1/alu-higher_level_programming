-- Creates the database hbtn_0d_usa and the table states in it.
-- Creates the database without failing if it already exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Creates the table states without failing if it already exists.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
