import logging
import sys
import os
from datetime import datetime
from pyspark.logger import PySparkLogger

# Setup log file path for data cleaning
log_dir = "/Workspace/Users/amjad2.hash@gmail.com/logs"
os.makedirs(log_dir, exist_ok=True)
log_file = f"{log_dir}/data_cleaning_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Create file-based logger
cleaning_logger = logging.getLogger("data_cleaning_logger")
cleaning_logger.setLevel(logging.INFO)

# Remove existing handlers
for h in cleaning_logger.handlers[:]:
    cleaning_logger.removeHandler(h)

# File handler
file_handler = logging.FileHandler(log_file)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
cleaning_logger.addHandler(file_handler)

# Console handler
stream_handler = logging.StreamHandler(sys.stdout)
console_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
stream_handler.setFormatter(console_formatter)
cleaning_logger.addHandler(stream_handler)

cleaning_logger.info("="*80)
cleaning_logger.info("DATA CLEANING PIPELINE STARTED")
cleaning_logger.info(f"Log file: {log_file}")
cleaning_logger.info("="*80)

# Initialize PySparkLogger for structured logging
pyspark_logger = PySparkLogger.getLogger()
pyspark_logger.info("event", user="amjad", action="data_cleaning_started")

# Read table
table_name = "workspace.bronze.taxi_trips_clean"
cleaning_logger.info(f"Reading table: {table_name}")
df_raw = spark.table(table_name)
raw_count = df_raw.count()
cleaning_logger.info(f"Raw data loaded: {raw_count:,} rows")

# Log sample raw data
cleaning_logger.info("Sample raw data (first 3 rows):")
for idx, row in enumerate(df_raw.limit(3).collect(), 1):
    cleaning_logger.info(f"  Row {idx}: {row.asDict()}")

# Data cleaning: Remove nulls
cleaning_logger.info("Step 1: Removing null values...")
df_clean = df_raw.dropna()
after_dropna = df_clean.count()
rows_removed = raw_count - after_dropna
cleaning_logger.info(f"  Nulls removed: {rows_removed:,} rows ({(rows_removed/raw_count*100):.2f}%)")
cleaning_logger.info(f"  Remaining: {after_dropna:,} rows")

# Data cleaning: Remove duplicates
cleaning_logger.info("Step 2: Removing duplicate rows...")
df_clean = df_clean.dropDuplicates()
after_dedup = df_clean.count()
dupes_removed = after_dropna - after_dedup
cleaning_logger.info(f"  Duplicates removed: {dupes_removed:,} rows ({(dupes_removed/after_dropna*100):.2f}%)")
cleaning_logger.info(f"  Remaining: {after_dedup:,} rows")

# Data cleaning: Filter trip_distance > 0
cleaning_logger.info("Step 3: Filtering trip_distance > 0...")
df_clean = df_clean.filter(df_clean.trip_distance > 0)
after_trip = df_clean.count()
trip_removed = after_dedup - after_trip
cleaning_logger.info(f"  Invalid trip_distance removed: {trip_removed:,} rows")
cleaning_logger.info(f"  Remaining: {after_trip:,} rows")

# Data cleaning: Filter fare_amount > 0
cleaning_logger.info("Step 4: Filtering fare_amount > 0...")
df_clean = df_clean.filter(df_clean.fare_amount > 0)
after_fare = df_clean.count()
fare_removed = after_trip - after_fare
cleaning_logger.info(f"  Invalid fare_amount removed: {fare_removed:,} rows")
cleaning_logger.info(f"  Remaining: {after_fare:,} rows")

# Data cleaning: Filter passenger_count > 0
cleaning_logger.info("Step 5: Filtering passenger_count > 0...")
df_clean = df_clean.filter(df_clean.passenger_count > 0)
final_count = df_clean.count()
passenger_removed = after_fare - final_count
cleaning_logger.info(f"  Invalid passenger_count removed: {passenger_removed:,} rows")
cleaning_logger.info(f"  Remaining: {final_count:,} rows")

# Log cleaned data summary
total_removed = raw_count - final_count
cleaning_logger.info("="*80)
cleaning_logger.info("DATA CLEANING SUMMARY")
cleaning_logger.info(f"  Initial rows: {raw_count:,}")
cleaning_logger.info(f"  Final rows: {final_count:,}")
cleaning_logger.info(f"  Total removed: {total_removed:,} rows ({(total_removed/raw_count*100):.2f}%)")
cleaning_logger.info(f"  Data quality: {(final_count/raw_count*100):.2f}% retained")
cleaning_logger.info("="*80)

# Log sample cleaned data
cleaning_logger.info("Sample cleaned data (first 5 rows):")
for idx, row in enumerate(df_clean.limit(5).collect(), 1):
    cleaning_logger.info(f"  Row {idx}: VendorID={row['VendorID']}, trip_distance={row['trip_distance']}, fare_amount={row['fare_amount']}, passenger_count={row['passenger_count']}")

# Select final columns
df_final = df_clean.select("VendorID", "trip_distance", "fare_amount", "passenger_count")
cleaning_logger.info(f"Final DataFrame created with {len(df_final.columns)} columns: {', '.join(df_final.columns)}")

# Log statistics for final dataset
cleaning_logger.info("Final dataset statistics:")
stats = df_final.describe().collect()
for stat_row in stats:
    cleaning_logger.info(f"  {stat_row.asDict()}")

pyspark_logger.info("event", user="amjad", action="data_cleaning_completed", final_rows=final_count)

cleaning_logger.info("="*80)
cleaning_logger.info("DATA CLEANING PIPELINE COMPLETED")
cleaning_logger.info(f"Log file saved to: {log_file}")
cleaning_logger.info("="*80)

print(f"\n✓ Data cleaning completed! Check log file at: {log_file}")