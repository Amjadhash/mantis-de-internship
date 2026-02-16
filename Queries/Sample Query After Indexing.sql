--Indexing and Query Performance
CREATE  INDEX IX_Orders_order_date

ON Orders_oltp (order_date) INCLUDE (order_status, total_amount, customer_id);

CREATE  INDEX IX_Orders_customer_id 
ON Orders_oltp (customer_id) INCLUDE (order_date, order_status, total_amount);

select c.full_name,count(o.order_id ) as orders,sum(o.total_amount )as total_spent
from customers_oltp c
join orders_oltp  o on c.customer_id=o.customer_id
group by c.full_name
order by total_spent desc;






















 


