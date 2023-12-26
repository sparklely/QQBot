import threading
from database import mysql_db
from data import GlobalVariable

if __name__ == "__main__":
    # 初始化mysql
    # 获取mysql参数
    mysql = mysql_db.MySQL()
    # 创建异步线程用于重新连接mysql
    reconnection_thread = threading.Thread(target=GlobalVariable.mysql.reconnect)
    reconnection_thread.start()

