-- Script to list all genres not linked to the show Dexter in the database hbtn_0d_tvshows.

SELECT name
FROM tv_genres
WHERE name NOT IN (
    SELECT tv_genres.name
    FROM tv_genres
    JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;
