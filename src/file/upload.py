from network import get
from initialize.config import group
from initialize.config import address


# 上传文件到群
# path:String <文件的本地目录> name:String <储存名称> folder:String <文件父目录>
def group_file(path, name, folder):
    get.get_text(address + "/upload_group_file?group_id=" + str(
        group) + "&&file=" + path + "&&name=" + name + "&&folder=" + folder)

