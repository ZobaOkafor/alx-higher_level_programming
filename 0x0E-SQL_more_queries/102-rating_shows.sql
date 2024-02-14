-- Script to list all shows from hbtn_0d_tvshows_rate by their rating.

SELECT tv_shows.title, SUM(tv_show_ratings.rate) rating_sum
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
