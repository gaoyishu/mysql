import tushare as ts
import pandas as pd
import pymysql
from sqlalchemy import create_engine
#近一年半行情

d = ts.get_k_data('603939')
#导入的是本机的mysql，sangomine是密码，quant是database的名称。
engine = create_engine("mysql+pymysql://root:sangomine@127.0.0.1/quant?charset=utf8")
# 这里一定要写成mysql+pymysql，不要写成mysql+mysqldb

d.to_sql(name='quant', con=engine, if_exists='append', index=False, index_label=False)
