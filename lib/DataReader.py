from lib.ConfigReader import get_app_config
from lib.utils import get_spark_session

def getOrderSchema():
    return '''order_id int,customer_id int,product_id int,order_date date,order_status string,quantity int,total_price double
'''
def get_order_df(spark,env):
    conf=get_app_config(env)
    file_path=conf['order.file.path']
    return spark.read.format('csv') \
          .schema(getOrderSchema()) \
          .option('header',True) \
          .load(file_path)

def get_customer_schema():
    return '''customer_id int,customer_name string,email string,city string,state string,signup_date date
'''
def get_customer_df(spark,env):
   conf=get_app_config(env)
   file_path=conf['customer.file.path']
   return spark.read.format('csv') \
         .schema(get_customer_schema()) \
          .option('header',True) \
         .load(file_path)

def get_product_schema():
    return '''product_id int,product_name string,category string,price double
'''
def get_product_df(spark,env):
    conf=get_app_config(env)
    file_path=conf['product.file.path']
    return spark.read.format('csv') \
         .schema(get_product_schema()) \
          .option('header',True) \
         .load(file_path)