from datetime import datetime
import os


# 用于获取时间的函数
def time():
    # 获取当前时间
    now = datetime.now()
    # 格式化为 "小时:分钟:秒" 字符串
    time_str = now.strftime("%H:%M:%S")
    return time_str


# 获取log文件的名称（当天的时间）
def file_name():
    # 获取当前时间
    now = datetime.now()
    # 格式化为 "月_日" 字符串
    date_str = "logs/" + now.strftime("%m_%d") + ".log"
    return date_str


# 最基础的输出函数，用于输出log信息
def log(text, isprint):
    _file = file_name()
    if isprint:
        print(text)
    # 创建log目录(如果不存在)
    os.makedirs("logs", exist_ok=True)
    # 如果日志文件不存在，则创建日志
    if not os.path.exists(_file):
        with open(_file, "wb") as file:
            file.write(f'file: {_file}'.encode('utf-8'))

    # 打开文件并将光标定位到文件末尾
    with open(_file, 'a') as f:
        # 写入日志信息
        f.write(text + '\n')


# 用于输出info的函数
def info(text, isprint):
    # 添加[info 时间]前缀
    text = f'[info {time()}]' + text
    log(text, isprint)


# 用于输出warning的函数
def warning(text, isprint):
    # 添加[info 时间]前缀,并将字体设置为黄色
    text = f'\033[33m[warning {time()}]' + text + "\033[0m"
    log(text, isprint)


# 用于输出error的函数
def error(text, isprint):
    # 添加[info 时间]前缀,并将字体设置为黄色
    text = f'\033[31m[error {time()}]' + text + "\033[0m"
    log(text, isprint)
