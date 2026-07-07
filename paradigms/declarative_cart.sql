IF NOT EXIST CREATE TABLE order_items(
    id INTEGER AUTOINCREMENT PRIMARY KEY,
    product_name VARCHAR NOT NULL,
    unit_price FLOAT NOT NULL,
    quantity INTEGER NOT NULL
);
INSERT INTO order_items(product_name, unit_price, quantity)
    VALUES ('Banana', 100, 10),
            ('Apple', 200, 5),
            ('Milk', 1500,50);

SELECT SUM(unit_price*quantity) AS total_price
FROM order_items;