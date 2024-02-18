from waiting.initialize.config import config
from waiting.initialize import g_vars
from waiting.storage.database import sqlite_db
import os
from file import log


def start():
    # 获取sqlite路径
    path = config['SQL']['sqlite']['path']
    if not os.path.exists(path):
        # 文件不存在，创建文件
        with open(path, "w"):
            pass
        log.info("成功創建sqlite文件", True)
        # 连接sqlite
    g_vars.sql.sqlite = sqlite_db.SQLite(path)
