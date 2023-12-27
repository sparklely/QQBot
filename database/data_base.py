from initialize import vars
from initialize.config import config

u_m = vars.sql.use_mysql
my = vars.sql.mysql
lite = vars.sql.sqlite


# 保存數據到數據庫
# table_name 表名, column_name 列名, data 值
def save_data(table_name, column_name, data):
    if u_m:
        my.save_data(table_name, column_name, data)
    else:
        lite.save_data(table_name, column_name, data)


# 检查数据库的某个列中是否有某个值
def check_value_exists
