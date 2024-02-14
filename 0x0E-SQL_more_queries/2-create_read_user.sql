-- Script to create the database hbtn_0d_2 and the user' user_0d_2'.

-- Create database hbtn_0d_2 if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user user_0d_2 if it doesn't exist and set password.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to user_0d_2 in database hbtn_0d_2.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
