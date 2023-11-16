-- SQL.
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
WHERE month = 7 OR month = 8
LIMIT 3;
