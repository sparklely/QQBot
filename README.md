# QQBot
使用 python 制作的基于go-cqhttp的QQ群机器人
# 使用方法
## 安装
切换至你的go-cqhttp所在目录，你应该会看到如下文件/目录：
```text
config.yml  device.json  LICENSE           cqLogs
download    logs         README.md
data        go-cqhttp    password.encrypt  session.token
```
然后打开终端/PowerShell,执行以下命令:
```bash
git clone https://github.com/ONFNTH/QQBot.git
cd QQBot
```
注意: 请确保你已经安装了git
安装工作到此完成
## 启动
直接运行`start.sh`/`start.bat`即可启动（请确保go-cqhttp已经启动）
## 配置
#### 配置go-cqhttp
找到`config.yml`，编辑以下配置(只列出了必要的)：
```yaml
account: # 账号相关
  uin: 你的QQ号 # QQ账号
  password: '' # 密码为空时使用扫码登录
  encrypt: false  # 是否开启密码加密
  status: 0      # 在线状态 请参考 https://docs.go-cqhttp.org/guide/config.html#在线状态
  relogin: # 重连设置
    delay: 3   # 首次重连延迟, 单位秒
    interval: 3   # 重连间隔
    max-times: 0  # 最大重连次数, 0为无限制
servers:
  - http: # HTTP 通信设置
      address: 0.0.0.0:8000 # HTTP监听地址
      version: 11     # OneBot协议版本, 支持 11/12
      timeout: 5      # 反向 HTTP 超时时间, 单位秒，<5 时将被忽略
      long-polling:   # 长轮询拓展
        enabled: false       # 是否开启
        max-queue-size: 2000 # 消息队列大小，0 表示不限制队列大小，谨慎使用
      middlewares:
        <<: *default # 引用默认中间件
      post:           # 反向HTTP POST地址列表
      - url: 'http://127.0.0.1:8001/'                # 地址
        secret: ''             # 密钥
        max-retries: 1         # 最大重试，0 时禁用
        retries-interval: 1500 # 重试时间，单位毫秒，0 时立即
```
如果不编辑这些配置，那么将无法正常启动
#### 配置文件
在`QQBot`目录的`config.yml`是该程序的配置文件，你无需编辑太多
```yaml
# 群号
group: 你的群号
command:
  # 命令前缀
  prefix: "#"
ai:
  img:
    # 是否启用AI画图
    enable: True
    # AI画图API %prompt%为提示词
    api: "https://image.ai.crystalneko.online?text=%prompt%"
  chat:
    # 是否启用AI聊天
    enable: True
    # AI聊天API %prompt%为提示词 %text%为输入文本
    api: "http://chat.ai.crystalneko.online/?p=%prompt%&&t=%text%"
    prompt: "你是一个可爱的猫娘"
yiyan:
  # 是否启用一言
  enable: True
  # 一言API
  api: "https://api.cenguigui.cn/api/yiyan/"
SQL:
  sqlite:
    # sqlite路径
    path: "../bot.db"
doc:
  # 选择文件格式 json/yaml
  mode: json
  # 数据存储位置
  path: "../bot-data/"
  
```