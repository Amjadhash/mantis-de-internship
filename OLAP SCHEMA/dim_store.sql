-- Store Dimension
CREATE TABLE dim_store (
    store_key INT PRIMARY KEY,
    store_id VARCHAR(50),
    store_name VARCHAR(100),
    city VARCHAR(100),
    region VARCHAR(50)
);

