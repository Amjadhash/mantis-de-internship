
CREATE TABLE orders_oltp(
    order_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    customer_id INT REFERENCES customers_oltp(customer_id),
    store_id INT REFERENCES stores_OLTP(store_id),
    order_status VARCHAR(20) NOT NULL, -- e.g., 'Pending', 'Shipped', 'Completed'
    total_amount DECIMAL(12, 2) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);






















 


