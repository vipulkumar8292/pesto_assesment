from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("AdvertiseX Data Processing") \
    .getOrCreate()

# Read JSON data from Kafka topic
df_ad_impressions = spark \
    .read \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "ad_impressions_topic") \
    .load()

# Example processing - selecting required columns
df_ad_impressions_processed = df_ad_impressions.selectExpr("CAST(value AS STRING)")

# Show processed data
df_ad_impressions_processed.show()
