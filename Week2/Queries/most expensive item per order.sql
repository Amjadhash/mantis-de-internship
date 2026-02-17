--the most expensive item per order
WITH RankedItems AS (
    SELECT 
        order_id, 
        product_id, 
        unit_price,
        RANK() OVER (PARTITION BY order_id ORDER BY unit_price DESC) as price_rank
    FROM order_items_oltp 
)
SELECT 
    order_id, 
    product_id, 
    unit_price
FROM RankedItems
WHERE price_rank = 1;
