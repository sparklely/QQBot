from initialize import vars

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
# tableName 表名, columnName 列名, value 要检查的值
def check_value_exists(table_name, column_name, value):
    if u_m:
        my.check_value_exists(table_name, column_name, value)
    else:
        lite.check_value_exists(table_name, column_name, value)


# 在tableName表中，需要更改columnName,当满足whereName = data时，则执行update
# tableName 表名, columnName 要更改的列(如: balance), whereName 要更改的条件列 (如：username), whereValue 要更改的条件值 (如：CrystalNeko)
# columnValue 更改后的值(如：123)
def save_data_where(table_name, column_name, where_name, where_value, column_value):
    if u_m:
        my.save_data_where(table_name, column_name, where_name, where_value, column_value)
    else:
        lite.save_data_where(table_name, column_name, where_name, where_value, column_value)
