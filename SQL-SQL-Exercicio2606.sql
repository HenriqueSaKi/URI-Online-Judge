-- URI Online Judge - Exercise 2606 (SQL)

SELECT products.id, products.name FROM products INNER JOIN categories ON categories.id = products.id_categories AND categories.name LIKE 'super%';
