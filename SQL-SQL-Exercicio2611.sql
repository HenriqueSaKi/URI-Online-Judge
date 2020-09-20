-- URI Online Judge - Exercise 2611 (SQL)

-- Select all the movies that the gender is equal to 'Action'
SELECT m.id, m.name FROM movies m JOIN genres g ON m.id_genres = g.id AND description = 'Action';
