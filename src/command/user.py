from command import help, yiyan, ai, acg, MCSM
from initialize import config
from initialize.config import command_async
from initialize.g_vars import commands as cmd
import asyncio
import threading


def execute(c_type, msg_data):
    if command_async:
        thread = threading.Thread(target=start_async, args=(c_type, msg_data))
        thread.start()

    else:
        _execute(c_type, msg_data)


def start_async(c_type, msg_data):
    # 在新线程中创建事件循环并运行异步任务
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(async_execute(c_type, msg_data))
    loop.close()


async def async_execute(c_type, msg_data):
    # 通过异步线程执行
    _execute(c_type, msg_data)


def _execute(c_type, msg_data):
    # 转换为数组
    if c_type == "":
        return
    arr_type = c_type.split()
    if arr_type[0] == "help":
        help.user_execute(arr_type)
    if arr_type[0] == "ai":
        if len(arr_type) >= 3:
            if arr_type[1] == "img" and config.ai_img_enable:
                ai.ai_img(arr_type[2])
            if arr_type[1] == "chat" and config.ai_chat_enable:
                ai.ai_chat(arr_type[2])
    if arr_type[0] == "一言" and config.yiyan_enable:
        yiyan.yy()
    if arr_type[0] == "注册":
        MCSM.run(msg_data)
    # 如果输入的命令存在于字典中且cate为user
    if arr_type[0] in cmd.commands and cmd.commands[arr_type[0]]['cate'] == 'user':
        # 获取命令的类
        cmd_class = cmd.commands[arr_type[0]]['class']()
        # 执行命令
        cmd_class.user_execute(arr_type)
