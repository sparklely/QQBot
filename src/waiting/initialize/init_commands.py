from API.register import command
from waiting.command import send, ai, yiyan, acg
from waiting.initialize import config


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



    command.reg_help('stop', "关闭程序", 'console')
    command.reg('send', send.send_class, 'console')
    command.reg_help('send msg <消息内容>', '发送消息', 'console')
    command.reg_help('send file <文件路径> <文件名称> <保存目录>', '发送文件', 'console')
