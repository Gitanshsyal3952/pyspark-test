import sys
from lib import DataReader, utils
from pyspark.sql.functions import *
if __name__ == '__main__':
  if len(sys.argv) < 2:
    print("Please specify the environment")
    sys.exit(-1)
job_run_env = sys.argv[1]
print("Creating Spark Session")
spark = utils.get_spark_session(job_run_env)
print("Created Spark Session")
order_df=DataReader.get_order_df(spark,job_run_env)
customer_df=DataReader.get_customer_df(spark,job_run_env)
product_df=DataReader.get_product_df(spark,job_run_env)
print(order_df.select('order_id','order_date','order_status').show())