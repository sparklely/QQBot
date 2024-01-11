import pkgutil
from file import log
from initialize.g_vars import plugs


def start():
    # 遍历 plugins 包下的所有模块
    for module_info in pkgutil.walk_packages(['plugins']):
        # 导入模块
        module = module_info.module_finder.find_module(module_info.name).load_module()
        # 调用 on_enable 函数
        if hasattr(module, 'on_enable'):
            # 获取插件名称
            plugin_name = module.plugin_name
            plugin_version = module.plugin_version
            plugin_authors = module.plugin_authors
            log.info(f'正在加载插件{plugin_name} V {plugin_version} by {plugin_authors}', True)
            # 写入全局变量
            plugs.plugs.update({plugin_name: module})
            # 启动插件
            module.on_enable()
