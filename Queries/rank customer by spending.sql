--rank customer by spending
SELECT 
    customer_id,
    SUM(total_amount) as total_spent,
    DENSE_RANK() OVER (ORDER BY SUM(total_amount) DESC) AS customer_rank
FROM Orders_oltp
GROUP BY customer_id;























 


