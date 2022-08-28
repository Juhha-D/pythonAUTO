# import pytest
import requests

#这块主要是策略相关的case
from common.request_util import RequestUtil
from common.yaml_util import read_yaml

#创建策略
class TestStrategy():

    def test_CreateStrategy(self):

        url = "http://rta-manage-sit.ing.mob.com/advLister/create"
        data = {
            "userId": read_yaml("uerid"),
            "outerTargetId": "20220828",
            "listerName": "快手自动化测试",
            "plat": 2,
            "cooperationMode": 1
        }
        headers={
            "token": read_yaml("token")
        }

        res = RequestUtil().send_request(method="post", url=url, json=data,headers=headers)
        print(res.json())

#创建规则集，不太需要每次创建
    # def test_ruleCollection(self):
    #     url = "http://rta-manage-sit.ing.mob.com/ruleCollection/save"
    #     data = {
    #         "name": "自动化测试",
    #         "remark": "自动化测试"
    #     }
    #     headers = {
    #         "token": read_yaml("token")
    #     }
    #     res = RequestUtil().send_request(method="post", url=url, json=data,headers=headers)
    #     print(res.json())


