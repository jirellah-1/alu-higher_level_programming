-- Creates the database hbtn_0d_2 and the user user_0d_2 that can only read it.
-- Creates the database without failing if it already exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates the user with its password, without failing if it already exists.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Gives only the SELECT privilege on the database hbtn_0d_2 to the user.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
