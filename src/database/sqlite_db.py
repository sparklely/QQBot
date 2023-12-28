import sqlite3


class SQLite:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)
        print('Connected to SQLite')

    def execute_query(self, query, params=None):
        """
        执行SQL查询，并返回结果集

        Args:
            query (str): SQL查询语句
            params (tuple, optional): 查询参数. Defaults to None.

        Returns:
            list: 查询结果集
        """
        with self.connection.cursor() as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            result = cursor.fetchall()
            return result

    def save_data(self, table_name, column_name, data):
        """
        将数据保存到数据库表中

        Args:
            table_name (str): 表名
            column_name (str): 列名
            data (str): 要保存的数据
        """
        if not self.is_table_exists(table_name):
            self.create_table(table_name)
        self.add_column(table_name, column_name)

        query = "INSERT INTO {} ({}) VALUES (?)".format(table_name, column_name)
        self.execute_query(query, (data,))

    def check_value_exists(self, table_name, column_name, value):
        """
        检查数据库表的某个列中是否存在某个值

        Args:
            table_name (str): 表名
            column_name (str): 列名
            value (str): 要检查的值

        Returns:
            bool: 值是否存在
        """
        query = "SELECT COUNT(*) FROM {} WHERE {} = ?".format(table_name, column_name)
        result = self.execute_query(query, (value,))
        count = result[0][0]
        return count > 0

    def save_data_where(self, table_name, column_name, where_name, where_value, column_value):
        """
        根据条件将数据保存到数据库表中

        Args:
            table_name (str): 表名
            column_name (str): 要更改的列
            where_name (str): 条件列名
            where_value (str): 条件值
            column_value (str): 更改后的值
        """
        if not self.is_table_exists(table_name):
            self.create_table(table_name)

        query = "UPDATE {} SET {} = ? WHERE {} = ?".format(table_name, column_name, where_name)
        self.execute_query(query, (column_value, where_value))

    def get_column_value(self, table_name, column_name, where_name, where_value):
        """
        获取数据库表中某个特定条件的值

        Args:
            table_name (str): 表名
            column_name (str): 列名
            where_name (str): 条件列名
            where_value (str): 条件值

        Returns:
            str: 查询结果
        """
        query = "SELECT {} FROM {} WHERE {}=?".format(column_name, table_name, where_name)
        result = self.execute_query(query, (where_value,))
        if result:
            return result[0][0]
        return None

    def read_all_values_in_a_column(self, table_name, column_name):
        """
        读取数据库表某个列的所有值

        Args:
            table_name (str): 表名
            column_name (str): 列名

        Returns:
            list: 查询结果的数组
        """
        query = "SELECT {} FROM {}".format(column_name, table_name)
        result = self.execute_query(query)
        values = [row[0] for row in result]
        return values

    def delete_line(self, table_name, where_column, where_value):
        """
        删除数据库表中某一行的数据

        Args:
            table_name (str): 表名
            where_column (str): 条件所在列
            where_value (str): 条件值

        Returns:
            bool: 是否成功删除
        """
        query = "DELETE FROM {} WHERE {} = ?".format(table_name, where_column)
        self.execute_query(query, (where_value,))
        return True

    def is_table_exists(self, table_name):
        """
        检查表是否存在

        Args:
            table_name (str): 表名

        Returns:
            bool: 表是否存在
        """
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"
        result = self.execute_query(query, (table_name,))
        return len(result) > 0

    def create_table(self, table_name):
        """
        创建表

        Args:
            table_name (str): 表名
        """
        query = "CREATE TABLE {} (id INTEGER PRIMARY KEY AUTOINCREMENT)".format(table_name)
        self.execute_query(query)

    def is_column_exists(self, table_name, column_name):
        """
        检查列是否存在

        Args:
            table_name (str): 表名
            column_name (str): 列名

        Returns:
            bool: 列是否存在
        """
        query = "PRAGMA table_info({})".format(table_name)
        result = self.execute_query(query)
        for column in result:
            if column[1] == column_name:
                return True
        return False

    def add_column(self, table_name, column_name):
        """
        添加列

        Args:
            table_name (str): 表
            column_name (str): 列名
        """
        if self.is_column_exists(table_name, column_name):
            return

        query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} TEXT"
        self.execute_query(query)
