-- Creates the table unique_id where id has the default value 1 and is unique.
-- Creates the table without failing if it already exists.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
