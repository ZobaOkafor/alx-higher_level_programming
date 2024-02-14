-- Script to list all genres in hbtn_0d_tvshows_rate by their rating.

SELECT tv_genres.title, SUM(tv_show_ratings.rate) rating
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_genres.title
ORDER BY rating DESC;
