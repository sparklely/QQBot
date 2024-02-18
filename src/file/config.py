import yaml

# 读取配置文件
with open('../config.yml', 'r', encoding='utf-8', errors='ignore') as stream:
    go_config = yaml.safe_load(stream)
with open('config.yml', 'r', encoding='utf-8', errors='ignore') as stream:
    config = yaml.safe_load(stream)

# ---------------------------------------------------------go-cqhttp----------------------------------------------
address = "http://" + go_config['servers'][0]['http']['address']  # 监听地址
address = address.replace("0.0.0.0", "127.0.0.1")  # 把0.0.0.0替换成127.0.0.1

# --------------------------------------------------日志----------------------------------------------------
log_info = bool(config['log']['info'])
log_warning = bool(config['log']['warning'])
log_error = bool(config['log']['error'])
log_debug = bool(config['log']['debug'])
