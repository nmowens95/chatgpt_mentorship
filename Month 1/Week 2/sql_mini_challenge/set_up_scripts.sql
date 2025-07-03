-- Using PostgreSQL

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount NUMERIC(10, 2)
);

CREATE TABLE order_items (
    item_id INT PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    product_id VARCHAR,
    unit_price NUMERIC(10, 2),
    quantity INT
);

CREATE TABLE products (
    product_id VARCHAR PRIMARY KEY,
    product_name VARCHAR,
    category VARCHAR
);

INSERT INTO orders (order_id, customer_id, order_date, total_amount) VALUES
(1, 101, '2024-05-01', 200.00),
(2, 102, '2024-05-03', 150.00),
(3, 101, '2024-05-05', 300.00),
(4, 103, '2024-05-06', 450.00),
(5, 104, '2024-05-08', 100.00);


INSERT INTO products (product_id, product_name, category) VALUES
('A1', 'Wireless Mouse', 'Electronics'),
('B2', 'USB-C Cable', 'Electronics'),
('C3', 'Notebook', 'Stationery'),
('D4', 'Desk Lamp', 'Furniture'),
('E5', 'Water Bottle', 'Accessories');


INSERT INTO order_items (item_id, order_id, product_id, unit_price, quantity) VALUES
(1, 1, 'A1', 25.00, 2),
(2, 1, 'B2', 10.00, 3),
(3, 2, 'C3', 15.00, 4),
(4, 3, 'A1', 25.00, 2),
(5, 3, 'D4', 50.00, 3),
(6, 4, 'E5', 20.00, 5),
(7, 5, 'B2', 10.00, 2);