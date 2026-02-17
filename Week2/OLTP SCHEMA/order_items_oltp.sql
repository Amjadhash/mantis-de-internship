
CREATE TABLE order_items_OLTP (
    order_item_id INT PRIMARY KEY ,
    order_id INT REFERENCES orders_OLTP(order_id) ON DELETE CASCADE,
    product_id INT REFERENCES products_OLTP(product_id),
    quantity INT NOT NULL,
    unit_price DECIMAL(12, 2) NOT NULL  
);

























 


