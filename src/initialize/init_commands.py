from API import command
from command import acg
from command import ai
from command import yiyan
from initialize import config


def start():
    if config.random_agc_enable:
        command.reg('二次元', acg.acg_class, 'user')
        command.reg_help('二次元', '获取随机二次元', 'user')

    if config.ai_chat_enable or config.ai_img_enable:
        command.reg('ai', ai.ai_class, 'user')
    if config.ai_chat_enable:
        command.reg_help('ai chat <文本>', 'AI聊天', 'user')
    if config.ai_img_enable:
        command.reg_help('ai img <文本>', 'AI画图', 'user')

    if config.yiyan_enable:
        command.reg('一言', yiyan.yy_class, 'user')
        command.reg_help('一言', '获取一言', 'user')

