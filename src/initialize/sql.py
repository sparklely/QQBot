from initialize.config import config
from initialize import g_vars
from database import sqlite_db
import os


# 获取sqlite路径
path = config['SQL']['sqlite']['path']
if not os.path.exists(path):
    # 文件不存在，创建文件
    with open(path, "w"):
        pass
    print("成功創建sqlite")
    # 连接sqlite
g_vars.sql.sqlite = sqlite_db.SQLite(path)
