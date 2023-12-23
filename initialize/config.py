import yaml

# 读取go-cqhttp的配置文件
with open('../config.yml', 'r') as stream:
    go_config = yaml.safe_load(stream)
address = go_config['servers'][0]['http']['address']  # 监听地址

# 读取配置文件
with open('config.yml', 'r') as stream:
    config = yaml.safe_load(stream)
group = config['group']  # 群号

print("监听地址: "+address)
print("群号: "+ str(group))