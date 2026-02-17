select c.full_name,c.email,sum(o.total_amount) as ytd_spent
from customers_oltp c
join orders_oltp  o on c.customer_id=o.customer_id
where EXTRACT(YEAR FROM CAST(o.order_date AS DATE)) = 2025
group by c.customer_id,c.full_name,c.email
order by ytd_spent desc
limit 10;

























 


