-- 2026-02-17 09:09:29
-- File: dim_date.sql

-- This is the dimension table for dates used in
-- the OLAP schema.
-- Create the dim_date table
CREATE TABLE dim_date (
    date_id INT PRIMARY KEY,
    date_value DATE,
    year INT,
    month INT,
    day INT,
    day_of_week INT
);
