# Walmart Sales ETL Pipeline

A simple ETL process for handling Walmart store weekly sales data.

The program performs the following tasks:
- Reading the CSV file
- Cleaning the data (removing duplicates, handling missing values)
- Rounding the fuel price to two decimal places
- Saving the result to a new CSV file

## Requirements

- Python 3.9 or higher
- Required libraries (see `requirements.txt`)

## How to Run
1. Prepare the files
  - Make sure you have pipeline.py, config.json, and requirements.txt in your project folder
  - Place the input file demo5.csv inside data/raw/

2. Install dependencies
  - pip install -r requirements.txt

3. Run the ETL pipeline

4. Expected output
  - Processed file: data/processed/demo5_clean.csv (you can change the path in config.json)
  - Log file: logs/pipeline.log