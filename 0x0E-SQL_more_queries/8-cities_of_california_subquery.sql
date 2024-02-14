-- Script to list all cities of California in the database hbtn_0d_usa.

-- Use the database hbtn_0d_usa.
USE hbtn_0d_usa;

-- Select cities of California using subquery to get state_id.
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
