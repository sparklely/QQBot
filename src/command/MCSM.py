from initialize.config import config
from message import send
from file import doc, log
from network import post, get, put

import yaml
import time


class MCSM:
    def __init__(self):
        self.qq = ""
        self.headers = {'X-Requested-With': "XMLHttpRequest", 'Content-Type': "application/json; charset=UTF-8"}

    # 注册
    def reg(self, msg_data):
        self.qq = msg_data["sender"]["user_id"]
        data = {
            "username": msg_data["sender"]["user_id"],
            "password": str(msg_data["sender"]["user_id"]) + "@Ab123456",
            "permission": "1"
        }
        try:
            re=post.json_headers(config["MCSM"]["url"]+"/api/auth?apikey="+config["MCSM"]["apikey"],self.headers,data)
            if re.json()['data']==True:
                send.group_msg(f"[CQ:at,qq={self.qq}]注册成功\n-------------------------------------\n默认密码:{self.qq}Ab123456\n请及时进入面板更改密码\n若忘记密码请让管理员帮忙重置",False)
                return True
            elif re.json()['data']=='用户名已经被占用':
                send.group_msg(f"[CQ:at,qq={self.qq}]禁止重复注册",False)
                return False
            else:
                print(re.json())
                send.group_msg(f"[CQ:at,qq={self.qq}]未知错误,请联系管理员查看后台报错",False)
                return False
        except Exception as e:
            log.error("无法请求MCSM注册api:" + str(e), True)
            send.group_msg(f"[CQ:at,qq={self.qq}]无法请求到api", False)
    # 创建实例
    def CI(self):
        MCSM_port = doc.yaml_read("./res/MCSM/port.yaml")
        port = str(MCSM_port['port'])
        ticks = time.time()
        # instance数据处理
        data = doc.json_read("./res/MCSM/init_instance.json")
        data['nickname'] = config["MCSM"]["AAI"]["name"] + ":" + port
        data['createDatetime'] = ticks
        data['lastDatetime'] = ticks
        data_docker_ports = []
        for port_type in config["MCSM"]["AAI"]["port"]["type"]:
            data_docker_ports.append(f"{port}:{port}/{port_type}")
        data['docker']['ports']=data_docker_ports
        data['startCommand']=config["MCSM"]["AAI"]["startCommand"]
        data['stopCommand']=config["MCSM"]["AAI"]["stopCommand"]
        data['type']=config["MCSM"]["AAI"]["type"]
        data['endTime']=config["MCSM"]["AAI"]["endTime"]
        data['docker']['image']=config["MCSM"]["AAI"]["docker"]["image"]
        data['docker']['memory']=config["MCSM"]["AAI"]["docker"]["memory"]
        data['docker']['cpusetCpus']=config["MCSM"]["AAI"]["docker"]["cpusetCpus"]
        return post.json_headers(config["MCSM"]["url"]+"/api/instance?apikey="+config["MCSM"]["apikey"]+"&daemonId="+config["MCSM"]["AAI"]["remote_uuid"],self.headers,data).json()
    # 自动分配实例
    def AAI(self, CIData):
        # 查询用户uuid
        uuid=get.get_json(config["MCSM"]["url"]+"/api/auth/search?apikey="+config["MCSM"]["apikey"]+"&userName="+str(self.qq)+"&role=&page=1&page_size=10000")[0]['data']['data'][0]['uuid']
        # 分配实例数据处理
        data = {
            "uuid": uuid,
            "apikey": config["MCSM"]["apikey"],
            "config": {
                "permission": 1,
                "instances": [
                    {
                        "instanceUuid":CIData["data"]["instanceUuid"],
                        "daemonId":config["MCSM"]["AAI"]["remote_uuid"]
                    }
                ]
            }
        }
        put.headers_json(config["MCSM"]["url"]+"/api/auth/?apikey="+config["MCSM"]["apikey"],self.headers,data).json()
        MCSM_port=doc.yaml_read("./res/MCSM/port.yaml")
        port=str(MCSM_port['port'])
        open_doc=open("./res/MCSM/port.yaml","w")
        open_doc.write(yaml.dump({"port":int(port)+1}))
        open_doc.close()

class MCSM_run:
    plugin = 'bot'
    permission = "command.MCSM"

    @staticmethod
    def user_execute(a,msg_data):
        pMCSM=MCSM()
        if pMCSM.reg(msg_data) and config["MCSM"]["AAI"]["enable"]:
            Q=pMCSM.CI()
            pMCSM.AAI(Q)