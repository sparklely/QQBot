from pathlib import Path
from file.YamlConfiguration import YamlConfiguration


print("喵~QQBot开始启动")

# 读取go-cqhttp的配置文件
config_path = Path("../config.yml")
config = YamlConfiguration(config_path)
address = config.get("servers.0.http.address")  # 读取监听地址
print(address)