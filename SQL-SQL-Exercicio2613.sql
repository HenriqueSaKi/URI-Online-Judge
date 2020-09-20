-- URI Online Judge - Exercise 2613 (SQL)

-- Select all movies that the price was smaller than 2.00
SELECT m.id, m.name FROM movies m JOIN prices p ON m.id_prices = p.id AND p.value < 2.00;
