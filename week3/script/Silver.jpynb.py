from pyspark.sql import functions as F

# Load and clean the data
df_raw = spark.read.csv("/Volumes/workspace/default/nycdata/nyc_taxi.csv", header=True, inferSchema=True)

df_clean = df_raw.filter(
    (F.col("trip_distance") > 0) &
    (F.col("fare_amount") > 0) &
    (F.col("passenger_count") > 0) &
    (F.col("passenger_count") <= 6) &
    (F.col("tpep_dropoff_datetime") > F.col("tpep_pickup_datetime"))
)

df = df_clean \
    .withColumn("tpep_pickup_datetime", F.to_timestamp("tpep_pickup_datetime", "M/d/yyyy H:mm")) \
    .withColumn("tpep_dropoff_datetime", F.to_timestamp("tpep_dropoff_datetime", "M/d/yyyy H:mm"))

# Apply transformations
df = df \
    .withColumn("trip_duration_min",
        F.round((F.unix_timestamp("tpep_dropoff_datetime") -
                 F.unix_timestamp("tpep_pickup_datetime")) / 60.0, 1)) \
    .withColumn("hour_of_day", F.hour("tpep_pickup_datetime")) \
    .withColumn("day_of_week", F.dayofweek("tpep_pickup_datetime")) \
    .withColumn("time_of_day",
        F.when(F.col("hour_of_day").between(6,9),   "AM Rush")
         .when(F.col("hour_of_day").between(10,15), "Midday")
         .when(F.col("hour_of_day").between(16,20), "PM Rush")
         .when(F.col("hour_of_day").between(21,23), "Evening")
         .otherwise("Late Night")) \
    .withColumn("tipped", F.when(F.col("tip_amount") > 0, "Yes").otherwise("No")) \
    .withColumn("payment_label",
        F.when(F.col("payment_type") == 1, "Credit Card")
         .when(F.col("payment_type") == 2, "Cash")
         .otherwise("Other"))

print("Done! Preview:")
display(df.select("trip_duration_min","hour_of_day","time_of_day","tipped","payment_label").limit(5))

result = df.groupBy("hour_of_day", "time_of_day") \
    .agg(
        F.count("*").alias("trips"),
        F.round(F.avg("fare_amount"), 2).alias("avg_fare"),
        F.round(F.avg("tip_amount"), 2).alias("avg_tip"),
        F.round(F.avg("trip_duration_min"), 1).alias("avg_duration_min")
    ) \
    .orderBy("hour_of_day")

display(result)

result2 = df.groupBy("payment_label", "tipped") \
    .agg(
        F.count("*").alias("trips"),
        F.round(F.avg("tip_amount"), 2).alias("avg_tip"),
        F.round(F.avg("total_amount"), 2).alias("avg_total")
    ).orderBy("payment_label", "tipped")

display(result2)