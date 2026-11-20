-- Creates the table force_name where name can not be null.
-- Creates the table without failing if it already exists.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
