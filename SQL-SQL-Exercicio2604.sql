-- URI Online Judge - Exercise 2604 (SQL)

-- Print on screen some table, that present all ID and it's name, from products wich price is under 10 or over 100.
SELECT id, name FROM products WHERE price < 10 OR price > 100; 
