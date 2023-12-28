from initialize import g_vars

u_m = vars.sql.use_mysql
my = vars.sql.mysql
lite = vars.sql.sqlite


def save_data(table_name, column_name, data):
    """
    将数据保存到指定表格的指定列中。

    Args:
        table_name (str): 表格名称。
        column_name (str): 列名称。
        data: 要保存的数据。
    """
    if u_m:
        my.save_data(table_name, column_name, data)
    else:
        lite.save_data(table_name, column_name, data)


def check_value_exists(table_name, column_name, value):
    """
    检查指定表格的指定列中是否存在特定的值。

    Args:
        table_name (str): 表格名称。
        column_name (str): 列名称。
        value: 要检查的值。

    Returns:
        bool: 如果存在则ReturnsTrue，否则ReturnsFalse。
    """
    if u_m:
        return my.check_value_exists(table_name, column_name, value)
    else:
        return lite.check_value_exists(table_name, column_name, value)


def save_data_where(table_name, column_name, where_name, where_value, column_value):
    """
    根据指定的条件将数据保存到指定表格的指定列中。

    Args:
        table_name (str): 表格名称。
        column_name (str): 列名称。
        where_name (str): 条件列名称。
        where_value: 条件列的值。
        column_value: 要保存的数据。
    """
    if u_m:
        my.save_data_where(table_name, column_name, where_name, where_value, column_value)
    else:
        lite.save_data_where(table_name, column_name, where_name, where_value, column_value)


def get_column_value(table_name, column_name, where_name, where_value):
    """
    获取指定表格中满足特定条件的列的值。

    Args:
        table_name (str): 表格名称。
        column_name (str): 列名称。
        where_name (str): 条件列名称。
        where_value: 条件列的值。

    Returns:
        列的值。
    """
    if u_m:
        return my.get_column_value(table_name, column_name, where_name, where_value)
    else:
        return lite.get_column_value(table_name, column_name, where_name, where_value)


def read_all_values_in_a_column(table_name, column_name):
    """
    读取指定表格中某个列的所有值。

    Args:
        table_name (str): 表格名称。
        column_name (str): 列名称。

    Returns:
        包含所有值的列表。
    """
    if u_m:
        return my.read_all_values_in_a_column(table_name, column_name)
    else:
        return lite.read_all_values_in_a_column(table_name, column_name)


def delete_line(table_name, where_column, where_value):
    """
    删除指定表格中满足特定条件的行数据。

    Args:
        table_name (str): 表格名称。
        where_column (str): 条件列名称。
        where_value: 条件列的值。

    Returns:
        删除的行数。
    """
    if u_m:
        return my.delete_line(table_name, where_column, where_value)
    else:
        return lite.delete_line(table_name, where_column, where_value)
