from lib import DataReader
from pyspark.sql.functions import *
from pyspark.sql import *
def filter_order_status(df,status):
    return df.filter(col('order_status')==status)

def order_status_sales(df,column):
    return df.groupBy(column).agg(sum('total_price').alias('total_sales'))

def join_df(df1,df2,key):
    return df1.join(df2,key)

def filter_count_customers(df1,count1):
    count_df=df1.groupBy('customer_id').agg(count(col('order_id')).alias('count_no')).filter(col('count_no')>count1)
    return count_df

def avg_order_price(df1):
    return df1.groupBy('city').agg(avg('total_price').alias('average_total_price'))

def top_expensive_per_department(df1,column):
    window_size=Window.partitionBy(column).orderBy(col('Total_price').desc())
    top_df=df1.withColumn('rank',dense_rank().over(window_size))
    return top_df.filter('rank=1')