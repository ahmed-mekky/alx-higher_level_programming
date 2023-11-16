-- SQL.
SELECT cities.id, cities.name, state.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
