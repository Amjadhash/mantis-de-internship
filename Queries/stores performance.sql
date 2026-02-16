--comparing a specific store's performance against the company average
WITH StoreSales AS (
    SELECT store_id, SUM(total_amount) AS store_total
    FROM Orders_oltp
    GROUP BY store_id
),
CompanyAverage AS (
    SELECT AVG(store_total) AS avg_revenue
    FROM StoreSales
)
SELECT 
    s.store_id, 
    s.store_total, 
    a.avg_revenue,
    (s.store_total - a.avg_revenue) AS performance_gap
FROM StoreSales s, CompanyAverage a;























 


