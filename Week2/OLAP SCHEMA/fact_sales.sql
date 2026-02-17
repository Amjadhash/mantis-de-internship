-- Sales Fact Table
CREATE TABLE fact_sales (
    sales_key SERIAL PRIMARY KEY,
    date_key INT REFERENCES dim_date(date_key),
    product_key INT REFERENCES dim_product(product_key),
    store_key INT REFERENCES dim_store(store_key),
    customer_key INT REFERENCES dim_customer(customer_key),
    order_id VARCHAR(50), 
    quantity INT,
    unit_price DECIMAL(18, 2),
   total_sales_amount DECIMAL(18, 2)

);



 


