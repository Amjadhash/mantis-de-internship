--High value customers
SELECT c.full_Name, 
       COUNT(f.Sales_Key) AS Frequency, 
       SUM(f.Total_sales_Amount) AS MonetaryValue
FROM Fact_Sales f
JOIN Dim_Customer c ON f.Customer_Key = c.Customer_Key
GROUP BY c.full_Name
HAVING SUM(f.Total_sales_Amount) > 400
ORDER BY MonetaryValue DESC;