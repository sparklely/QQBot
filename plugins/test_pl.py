from API.register.plugin import plug
from file import log


class plug_main(plug):
    name = "plugin_name"
    version = "1.0.0"

    @staticmethod
    def on_enable():
        log.info("成功启动测试插件", True)
