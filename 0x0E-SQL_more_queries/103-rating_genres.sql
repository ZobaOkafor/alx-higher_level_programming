-- Script to list all genres in hbtn_0d_tvshows_rate by their rating

SELECT tv_genres.name, SUM(tv_show_ratings.rate) rating
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
