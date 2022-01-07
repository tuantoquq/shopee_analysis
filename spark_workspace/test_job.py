from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Job Test').getOrCreate()
df = spark.read.parquet('hdfs://namenode:9000/user/tuannha/data/test.parquet')
df.printSchema()
print(df.count())