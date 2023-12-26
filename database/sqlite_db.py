import sqlite3


class SQLite:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)
        print('Connected to SQLite')

    def execute_query(self, query, params=None):
        with self.connection.cursor() as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            result = cursor.fetchall()
            return result

    def save_data(self, table_name, column_name, data):
        if not self.is_table_exists(table_name):
            self.create_table(table_name)
        self.add_column(table_name, column_name)

        query = f"INSERT INTO {table_name} ({column_name}) VALUES (?)"
        self.execute_query(query, (data,))

    # 其他方法...

    def is_table_exists(self, table_name):
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
        result = self.execute_query(query)
        return len(result) > 0

    def create_table(self, table_name):
        query = f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT)"
        self.execute_query(query)

    def is_column_exists(self, table_name, column_name):
        query = f"PRAGMA table_info('{table_name}')"
        result = self.execute_query(query)
        return any(column_name in r for r in result)

    def add_column(self, table_name, column_name):
        if self.is_column_exists(table_name, column_name):
            return

        query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} TEXT"
        self.execute_query(query)
