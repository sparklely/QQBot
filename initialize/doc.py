import os
from initialize.config import config

def Check_file_integrity():
    file_list=[]#检查文件列表
    for file_ckeck in file_list:
        #检查文件是否存在
        if not os.path.isfile(file_ckeck):
            #初始化
            with open("./data/"+file_ckeck,"w") as open_doc:
                if config['doc']['mode']=='json':
                    open_doc.write("\x7b\x7d")#转义 \x7b->{ \x7d->}
                elif config['doc']['mode']=='yaml':
                    open_doc.write("data:")
                open_doc.close()