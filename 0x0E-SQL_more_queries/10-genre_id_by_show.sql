-- Script to list all shows with at least one linked genre in the database hbtn_0d_tvshows.

-- Use the database hbtn_0d_tvshows.
USE hbtn_0d_tvshows;

-- Select shows and their linked genres.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
