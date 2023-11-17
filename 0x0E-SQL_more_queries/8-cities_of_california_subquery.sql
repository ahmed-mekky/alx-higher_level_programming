-- SQL.
SELECT cities.id, cities.name
WHERE cities.id = (
	SELECT states.id FROM states
	WHERE states.name = 'California'
	LIMIT 1
)
ORDER BY cities.id ASC;
