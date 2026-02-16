
CREATE TABLE products_OLTP (
    product_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    product_name VARCHAR(255) NOT NULL,
    description TEXT,
    base_price DECIMAL(12, 2) NOT NULL,
    stock_quantity INT DEFAULT 0
);

SELECT  p.Produc_tName, SUM(f.Total_sales_Amount) AS Revenue
FROM FactSales f
JOIN Dim_Product p ON f.Product_Key = p.Product_Key
GROUP BY p.Product_Name
ORDER BY Revenue DESC
limit 5;
























 


