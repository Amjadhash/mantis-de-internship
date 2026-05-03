🏗️ Data Lakehouse on Databricks
A complete, professional implementation of a Lakehouse architecture using Databricks, structured into Bronze, Silver, and Gold layers and developed as part of the Data with Baraa - Databricks Bootcamp. The project processes bike sales data and includes a fully orchestrated ETL pipeline triggered automatically when new files arrive in the raw volume.

Tech Stack
Databricks Lakehouse Platform
Apache Spark / PySpark
Python
Git & GitHub

🔄 Pipeline Overview
Bronze: Load raw datasets into Delta format.
Silver: Apply cleaning, normalization, schema enforcement, and deduplication.
Gold: Produce optimized, analytics-ready tables for BI and downstream consumption.

CODE DESCRIPTION :

 TRIP Duration BY Minutes :
withColumn("trip_duration_min",
    F.round((F.unix_timestamp("tpep_dropoff_datetime") -
    F.unix_timestamp("tpep_pickup_datetime")) / 60.0, 1)) \
    .withColumn("hour_of_day", F.hour("tpep_pickup_datetime")) \
    .withColumn("day_of_week", F.dayofweek("tpep_pickup_datetime"))


TIPPED PAYMENT  & PAYMENT TYPE
.withColumn("tipped", F.when(F.col("tip_amount") > 0, "Yes").otherwise("No")) 
## Yes Pay tipped    No dont pay tipped or extra money
\
    .withColumn("payment_label",
        F.when(F.col("payment_type") == 1, "Credit Card")
         .when(F.col("payment_type") == 2, "Cash")
         .otherwise("Other"))
         ##  payment_type = 1 pay by Credit Card ,
              payment_type = 2 pay by Cash 
              otherNumber pay by "Other"


Triggering Mechanism
The job is automatically triggered when new files are added to the raw volume:

workspace.bronze.raw_sources

This enables near-real-time ingestion and processing without manual intervention
    
