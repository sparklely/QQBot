import yaml

# 读取go-cqhttp的配置文件
with open('../config.yml', 'r', encoding='utf-8', errors='ignore') as stream:
    go_config = yaml.safe_load(stream)
address = "http://" + go_config['servers'][0]['http']['address']  # 监听地址
address = address.replace("0.0.0.0", "127.0.0.1")  # 把0.0.0.0替换成127.0.0.1
# 读取配置文件
with open('config.yml', 'r', encoding='utf-8', errors='ignore') as stream:
    config = yaml.safe_load(stream)
group = config['group']  # 群号
ai_chat_enable = bool(config['ai']['chat']['enable'])  # 是否启用了AI聊天
ai_img_enable = bool(config['ai']['img']['enable'])  # 是否启用了AI画图
command_prefix = config['command']['prefix']  # 命令前缀
yiyan_enable = config['yiyan']['enable']  # 是否启用一言
if yiyan_enable:
    yiyan_api = config['yiyan']['api']  # 一言API
random_agc_enable = bool(config['acg']['random-img']['enable'])  # 是否启用随机二次元
if random_agc_enable:
    random_agc_api = config['acg']['random-img']['api']
    random_agc_max = int(config['acg']['random-img']['max'])
    random_agc_min = int(config['acg']['random-img']['min'])
