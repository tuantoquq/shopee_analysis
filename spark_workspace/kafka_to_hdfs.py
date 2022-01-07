from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from functools import reduce
from pyspark.sql import DataFrame
from pyspark.sql.functions import *
from pyspark.sql.types import *

#config kafka server and topic
KAFKA_BROKER = "kafka-container:9092"
KAFKA_TOPIC = "item-shopee"

#Create spark job
spark = SparkSession.builder.appName('shopee-streaming-data').getOrCreate()

#create stream kafka message
kafkaMessage = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BROKER) \
    .option("subscribe",KAFKA_TOPIC) \
    .option("startingOffsets","earliest") \
    .load()

#read stream kafka message
messages = kafkaMessage.selectExpr("CAST(value AS STRING)")
# write to hdfs
fileStream = messages.writeStream \
    .trigger(processingTime='60 seconds')\
    .queryName("Persist the processed data") \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "hdfs://namenode:9000/user/tuannha/data/") \
    .option("checkpointLocation", "hdfs://namenode:9000/user/tuannha/checkpoints") \
    .start() \
    .awaitTermination()