-- Script to list all genres not linked to the show Dexter in the database hbtn_0d_tvshows.

-- Use the database hbtn_0d_tvshows.
USE hbtn_0d_tvshows;

-- Select genres linked to Dexter.
SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter';

-- Select all genres excluding those linked to Dexter.
SELECT name
FROM tv_genres
WHERE name NOT IN (
    SELECT tv_genres.name
    FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;
