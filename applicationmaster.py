import sys
from lib import DataReader, utils,DataManipulation
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
filter_df=DataManipulation.filter_order_status(order_df,'DELIVERED')
total_sales_df=DataManipulation.order_status_sales(order_df,'order_status')
join_df=DataManipulation.join_df(order_df,customer_df,'customer_id')
filter_join_df=DataManipulation.filter_count_customers(join_df,1)
avg_total_price_df=DataManipulation.avg_order_price(join_df)
join_df1=DataManipulation.join_df(join_df,product_df,'product_id')
top_products_df=DataManipulation.top_expensive_per_department(join_df1,'category')
print(top_products_df.select('order_id','product_id','category','total_price','rank').show())