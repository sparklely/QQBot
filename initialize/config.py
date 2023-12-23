import yaml

# 读取go-cqhttp的配置文件
with open('../config.yml', 'r') as stream:
    go_config = yaml.safe_load(stream)
address = "http://" + go_config['servers'][0]['http']['address']  # 监听地址
address = address.replace("0.0.0.0", "127.0.0.1")  # 把0.0.0.0替换成127.0.0.1
# 读取配置文件
with open('config.yml', 'r') as stream:
    config = yaml.safe_load(stream)
group = config['group']  # 群号
