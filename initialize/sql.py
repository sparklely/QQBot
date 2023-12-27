from initialize.config import config
from database import sqlite_db
import os


# 是否使用数据库存储
if config['datastorage']['mode'] == "SQL":
    # 获取sqlite路径
    path = config['SQL']['sqlite']['path']
    if not os.path.exists(path):
        # 文件不存在，创建文件
        with open(path, "w"):
            pass
        print("成功創建sqlite")
    # 连接sqlite
    GlobalVariable.sql.sqlite = sqlite_db.SQLite(path)
