-- Creates the table id_not_null where id has the default value 1.
-- Creates the table without failing if it already exists.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
