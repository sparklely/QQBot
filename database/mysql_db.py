from initialize.config import config
import pymysql
from time import sleep


class MySQL:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=config['mysql']['host'],
                port=config['mysql']['port'],
                database=config['mysql']['database'],
                user=config['mysql']['username'],
                password=config['mysql']['password'],
                charset=config['mysql']['char']
            )
            print('Connected to MySQL')
        except pymysql.Error as e:
            print('Failed to connect to MySQL:', str(e))
            sleep(5)
            self.connect()

    def reconnect(self):
        while True:
            try:
                self.connect()
                sleep(3600)  # 暂停1小时
            except pymysql.Error as e:
                print('Unable to connect to MySQL:', str(e))
                sleep(5)

    def save_data(self, table_name, column_name, data):
        if not self.is_table_exists(table_name):
            self.create_table(table_name)
        self.add_column(table_name, column_name)

        query = f"INSERT INTO {table_name} ({column_name}) VALUES (%s)"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (data,))
            self.connection.commit()

    def check_value_exists(self, table_name, column_name, value):
        query = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (value,))
            count = cursor.fetchone()[0]
            return count > 0

    def save_data_where(self, table_name, column_name, where_name, where_value, column_value):
        if not self.is_table_exists(table_name):
            self.create_table(table_name)

        query = f"UPDATE {table_name} SET {column_name} = %s WHERE {where_name} = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (column_value, where_value))
            self.connection.commit()

    def get_column_value(self, table_name, column_name, where_name, where_value):
        query = f"SELECT {column_name} FROM {table_name} WHERE {where_name} = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (where_value,))
            result = cursor.fetchone()
            if result:
                return result[0]

    def read_all_value_in_a_column(self, table_name, column_name):
        query = f"SELECT {column_name} FROM {table_name}"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            return [result[0] for result in results]

    def delete_line(self, table_name, where_column, where_value):
        query = f"DELETE FROM {table_name} WHERE {where_column} = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (where_value,))
            self.connection.commit()

    def is_table_exists(self, table_name):
        with self.connection.cursor() as cursor:
            cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            result = cursor.fetchone()
            return result is not None

    def create_table(self, table_name):
        query = f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY)"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()

    def is_column_exists(self, table_name, column_name):
        with self.connection.cursor() as cursor:
            cursor.execute(f"SHOW COLUMNS FROM {table_name} LIKE '{column_name}'")
            result = cursor.fetchone()
            return result is not None

    def add_column(self, table_name, column_name):
        if self.is_column_exists(table_name, column_name):
            return

        query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} TEXT"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()

