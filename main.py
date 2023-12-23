import yaml


print("喵~QQBot开始启动")

# 读取go-cqhttp的配置文件
with open('../config.yml', 'r') as stream:
    config = yaml.safe_load(stream)
address = config['servers'][0]['http']['address']  # 读取监听地址
