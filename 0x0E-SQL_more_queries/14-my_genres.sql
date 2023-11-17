-- SQL.
SELECT tv_shows.title AS 'name'
FROM tv_shows 
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
AND tv_show_genres.genre_id = 5
ORDER BY tv_shows.title;
