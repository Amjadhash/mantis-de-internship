from pyspark.sql import SparkSession
df_raw = spark.read.csv("/Volumes/workspace/default/nycdata/nyc_taxi.csv", header=True, inferSchema=True)
spark.sql("CREATE SCHEMA IF NOT EXISTS workspace.Bronze")
spark.sql("USE workspace.Bronze")
#df=spark.sql("select * from samples.nyctaxi.trips")
#df_raw = spark.read.csv("/Volumes/workspace/default/nycdata/nyc_taxi.csv")
df_clean=df_raw.write.mode("overwrite").format("delta").saveAsTable("taxi_trips_clean")


print(f"Rows: {df_raw.count():,}")
print(f"Columns: {len(df_raw.columns)}")

%sql
use catalog `workspace`; select * from `gold`.`taxi_trips_clean` limit 100;