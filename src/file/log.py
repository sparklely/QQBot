from datetime import datetime
import os
from initialize.config import log_info
from initialize.config import log_warning
from initialize.config import log_error
from initialize.config import log_debug


# 用于获取时间的函数
def _time():
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
    # 打开文件并将光标定位到文件末尾
    with open(_file, 'a') as f:
        # 写入日志信息
        f.write(str(text) + '\n')


# 用于输出info的函数
def info(text, isprint):
    if log_info:
        # 添加[info 时间]前缀
        text = f'[info {_time()}]' + str(text)
        log(text, isprint)


# 用于输出warning的函数
def warning(text, isprint):
    if log_warning:
        # 添加[warning 时间]前缀,并将字体设置为黄色
        text = f'\033[33m[warning {_time()}]' + str(text) + "\033[0m"
        log(text, isprint)


# 用于输出error的函数
def error(text, isprint):
    if log_error:
        # 添加[error 时间]前缀,并将字体设置为黄色
        text = f'\033[31m[error {_time()}]' + str(text) + "\033[0m"
        log(text, isprint)


# 用于输出debug信息的函数
def debug(text, isprint):
    if log_debug:
        # 添加[debug 时间]前缀,并将字体设置为绿色
        text = f'\033[92m[debug {_time()}]' + str(text) + "\033[0m"
        log(text, isprint)
