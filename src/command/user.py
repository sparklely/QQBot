from command import help, yiyan, ai, acg,MCSM
from initialize import config
from initialize.config import command_async
import asyncio
import threading


def execute(c_type,msg_data):
    if command_async:
        thread = threading.Thread(target=start_async, args=(c_type,msg_data,))
        thread.start()

    else:
        _execute(c_type)


def start_async(c_type,msg_data):
    # 在新线程中创建事件循环并运行异步任务
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(async_execute(c_type,msg_data))
    loop.close()


async def async_execute(c_type,msg_data):
    # 通过异步线程执行
    _execute(c_type,msg_data)


def _execute(c_type,msg_data):
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
    if arr_type[0] == "二次元" and config.random_agc_enable:
        acg.random_img()
    if arr_type[0]=="注册":
        pMCSM=MCSM()
        pMCSM.reg(msg_data)
