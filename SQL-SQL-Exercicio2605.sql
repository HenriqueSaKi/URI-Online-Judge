-- URI Online Judge - Exercise 2605 (SQL)

-- Manipulling 3 data bases into one with useful information.
SELECT products.name, providers.name FROM products, providers WHERE products.id_providers = providers.id AND products.id_categories = 6;
