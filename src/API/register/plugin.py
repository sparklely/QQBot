from abc import ABC, abstractmethod


class plug(ABC):
    # 必须
    name = "plugin_name"
    version = "1.0.0"

    # 可选
    authors = [None]
    repository = None

    @abstractmethod
    def on_enable(self):
        """
        插件在启动时执行的函数
        """
        pass

