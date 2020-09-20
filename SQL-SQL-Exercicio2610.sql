-- URI Online Judge - Exercise 2610 (SQL)

-- Show the average price from 'products' table
SELECT ROUND(AVG(p.price),2) FROM products AS p;
