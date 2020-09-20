-- URI Online Judge - Exercise 2618 (SQL)

SELECT prod.name, prov.name, c.name 
FROM products prod 
JOIN providers prov ON prod.id_providers = prov.id
JOIN categories c ON prod.id_categories = c.id
AND prov.name = 'Sansul SA'
AND c.name = 'Imported';
