-- URI Online Judge - Exercise 2617 (SQL)

-- Select all products name which were provided for 'Ajax SA' 
SELECT prod.name, prov.name FROM products prod JOIN providers prov ON prod.id_providers = prov.id AND prov.name = 'Ajax SA';
