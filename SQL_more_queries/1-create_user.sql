-- Creates the MySQL server user user_0d_1 with all privileges on the server.
-- Creates the user with its password, without failing if it already exists.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Gives all privileges on the whole server to the user.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
