-- Creates the table second_table in the database hbtn_0c_0 and adds multiple rows.
-- Creates the table second_table without failing if it exists.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- Adds the four records of the task to second_table.
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
