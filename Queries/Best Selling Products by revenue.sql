--Top 5 Best-Selling Products by Revenue
SELECT  p.Product_Name, SUM(f.Total_sales_Amount) AS Revenue
FROM Fact_Sales f
JOIN Dim_Product p ON f.Product_Key = p.Product_Key
GROUP BY p.Product_Name
ORDER BY Revenue DESC
limit 5;
