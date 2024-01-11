import yaml

# 读取配置文件
with open('../config.yml', 'r', encoding='utf-8', errors='ignore') as stream:
    go_config = yaml.safe_load(stream)
with open('config.yml', 'r', encoding='utf-8', errors='ignore') as stream:
    config = yaml.safe_load(stream)

# ---------------------------------------------------------go-cqhttp----------------------------------------------

address = "http://" + go_config['servers'][0]['http']['address']  # 监听地址
address = address.replace("0.0.0.0", "127.0.0.1")  # 把0.0.0.0替换成127.0.0.1

# ---------------------------------------------------------配置------------------------------------------------------

group = config['group']  # 群号

# -----------------------------------------------------------AI---------------------------------------------------

ai_chat_enable = bool(config['ai']['chat']['enable'])  # 是否启用了AI聊天
if ai_chat_enable:
    ai_chat_api = config["ai"]["chat"]["api"]
    ai_chat_prompt = config["ai"]["chat"]["prompt"]
ai_img_enable = bool(config['ai']['img']['enable'])  # 是否启用了AI画图
if ai_img_enable:
    ai_img_api = config["ai"]["img"]["api"]

# -----------------------------------------------------------命令------------------------------------------------
command_prefix = config['command']['prefix']  # 命令前缀
command_async = bool(config['command']['async'])  # 是否启用异步任务

# ----------------------------------------------------一言--------------------------------------------------------
yiyan_enable = config['yiyan']['enable']  # 是否启用一言
if yiyan_enable:
    yiyan_api = config['yiyan']['api']  # 一言API

# ---------------------------------------------------随机二次元-------------------------------------------------------
random_agc_enable = bool(config['acg']['random-img']['enable'])  # 是否启用随机二次元
if random_agc_enable:
    random_agc_api = config['acg']['random-img']['api']
    random_agc_max = int(config['acg']['random-img']['max'])
    random_agc_min = int(config['acg']['random-img']['min'])
    random_agc_cache = bool(config['acg']['random-img']['cache'])

# --------------------------------------------------日志----------------------------------------------------
log_info = bool(config['log']['info'])
log_warning = bool(config['log']['warning'])
log_error = bool(config['log']['error'])
log_debug = bool(config['log']['debug'])
