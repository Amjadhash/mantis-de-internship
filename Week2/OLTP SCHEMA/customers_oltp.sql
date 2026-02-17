CREATE TABLE customers_OLTP (
    customer_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    gender VARCHAR(20)
   
);






 


