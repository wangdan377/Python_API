import os
import yaml
import getpathinfo
class ReadYaml():
    def __init__(self,filename):
        path = getpathinfo.get_path()#获取本地路径
        self.filepath = os.path.join(path,'configs/test')+"/"+filename#拼接定位到data文件夹
        # self.filepath = os.path.join(path, 'configs/pre') + "/" + filename  # 拼接定位到data文件夹
    def get_yaml_data(self):
        with open(self.filepath, "r", encoding="utf-8")as f:
            # 调用load方法加载文件流
            return yaml.load(f)

if __name__ == '__main__':
    data = ReadYaml("regiter_one.yml").get_yaml_data()
    print(data)


