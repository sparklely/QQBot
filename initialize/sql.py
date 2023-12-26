import threading
from database import mysql_db
from database.data_base import sql

if __name__ == "__main__":
    # 初始化mysql
    # 获取mysql参数
    mysql = mysql_db.MySQL()
    # 创建异步线程用于重新连接mysql
    reconnection_thread = threading.Thread(target=sql.mysql.reconnect)
    reconnection_thread.start()

# TODO: 把mysql参数写入全局变量
