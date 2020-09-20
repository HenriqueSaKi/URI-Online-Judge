-- URI Online Judge - Exercise 2609 (SQL)

SELECT c.name, SUM(p.amount) FROM categories c INNER JOIN products p ON c.id = p.id_categories;
