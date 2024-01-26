#!/bin/bash

path="src/main.py"

PYTHON_CMD=$(which python || which python3 || which py)
PIP_CMD=$(which pip || which pip3)
# 检查是否找到可执行的 Python 命令
if [ -z "$PIP_CMD" ]; then
    echo "未找到可执行的 pip 命令,是否使用apt进行安装 y/n"
    read input
    if [ -n "$input" ] && [ "$input" = "y" ]; then
	sudo apt install python3-pip
    fi
fi
if [ -z "$PYTHON_CMD" ]; then
    echo "未找到可执行的 Python 命令"
    read -rp "按下 Enter 退出..."
    exit 1
fi

# 检查并安装 pymysql 库
if ! $PYTHON_CMD -c "import pymysql" &>/dev/null; then
    echo "未找到 pymysql，开始安装..."
    ${PIP_CMD} install pymysql || { echo "安装 pymysql 失败";  }
fi


# 运行启动命令
$PYTHON_CMD ${path}

