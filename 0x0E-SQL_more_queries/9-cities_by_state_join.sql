-- Script to list all cities with their respective states in the database hbtn_0d_usa.

-- Use the database hbtn_0d_usa.
USE hbtn_0d_usa;

-- Select cities and their respective states.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
