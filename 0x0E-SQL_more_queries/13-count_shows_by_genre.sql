-- Script to list all genres and the number of shows linked to each in the database hbtn_0d_tvshows.

SELECT tv_show_genres.genre AS genre, COUNT(*) AS number_of_shows
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_show_genres.genre
HAVING COUNT(*) > 0
ORDER BY number_of_shows DESC;
