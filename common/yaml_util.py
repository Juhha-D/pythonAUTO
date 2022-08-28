
import os
import yaml

#这个文件是为了将一些参数用这个方法来传
#读取
def read_yaml(key):
    with open(os.getcwd()+'/extract.yaml',encoding='utf-8') as f:
        value=yaml.load(stream=f,Loader=yaml.FullLoader)
        return value[key]
#写入

def write_yaml(data):
    with open(os.getcwd()+'/extract.yaml',mode='a',encoding='utf-8') as f:
        yaml.dump(data,stream=f,allow_unicode=True)
#清空
def clear_yaml():
    with open(os.getcwd()+'/extract.yaml',mode='w',encoding='utf-8') as f:
        f.truncate()