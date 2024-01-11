#!/bin/bash

path="src/main.py"
# 尝试执行 py 命令
if hash py 2>/dev/null; then
    py ${path}
# 如果不存在 py 命令，尝试执行 python 命令
elif hash python 2>/dev/null; then
    python ${path}
# 如果不存在 python 命令，尝试执行 python3 命令
elif hash python3 2>/dev/null; then
    python3 ${path}
# 如果都不存在，输出提示信息并退出脚本
else
    echo "找不到 Python 解释器"
    exit 1
fi

