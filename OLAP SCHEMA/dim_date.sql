-- Date Dimension (Critical for time-series analysis)
CREATE TABLE dim_date (
    date_key INT PRIMARY KEY, -- Format: YYYYMMDD
    full_date DATE,
    calendar_month VARCHAR(15),
    calendar_year INT 
  
);
 


