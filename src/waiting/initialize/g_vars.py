# 类变量引用时不会被重置
class sql:
    use_mysql = False
    mysql = None
    sqlite = None


class commands:
    commands = {}
    user_help = ""
    console_help = ""


class plugs:
    plugs = {}
