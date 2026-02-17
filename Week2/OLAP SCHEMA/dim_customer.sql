-- Customer Dimension
CREATE TABLE dim_customer (
    customer_key INT PRIMARY KEY,
    customer_id VARCHAR(50),
    full_name VARCHAR(255),
    email VARCHAR(255),
    gender VARCHAR(20)
    
);


