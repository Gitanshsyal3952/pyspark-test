from pyspark.sql import SparkSession
from lib.ConfigReader import get_pyspark_config
def get_spark_session(env):
   if env == "LOCAL":
    return SparkSession.builder \
        .master("local[2]") \
        .config(conf=get_pyspark_config(env)) \
    .getOrCreate()
   else:
    return SparkSession.builder \
   .config(conf=get_pyspark_config(env)) \
   .enableHiveSupport() \
   .getOrCreate()
