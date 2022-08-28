import json
import time
import pytest
import requests


# @pytest.fixture(scope="class",autouse=True)
# def my_fixture():
#     # 定义全局变量
#     # token = ""
#     content = ""
#     # 登陆接口，主要是为了获取token
#     url = "http://api.id.aaa.test.mob.com/login/password/rsa"
#     date = {
#         "account": "V2@163.com",
#         "password": "TGu+8Lm7Futjw6O9pUfNQXbuVZL6bFzqsZNY5FgL6C3WKtXdwjxYQO45Yr5fRP6dubR2DwpI4Crq/RbBmYycTRkS0y5mAu4BykX6Rzrpwxhfm6dW4PPcjj5/+lGkilRTqzAkgdlcA2hepuIuj8lPfJNcGN39bne4PWLokPQg3cXK0On7KeTP/G4/SY1km8qkCiqcE1Auw00tba/0pD0D2q2uChFe0751XjyiZuT6yQXbExW2ze13CcyKmJbvdEZbQ53/WnSlhQUOaHC4oaAy4K5el73T2td2kKXmA2UnKKDGPDAOQZlJskLHEWaUAc4OGS4A49PX1q3U84mIHtwzOw=="
#     }
#     res = requests.post(url, json=date)
#     write_yaml({'token':res.json()['content']['token']})
#     # token = Testuser.token= res.json()['content']['token']
from common.request_util import RequestUtil
from common.yaml_util import write_yaml, read_yaml


class Testuser:

    #定义全局变量,类变量，通过类名调用
    # uerid1 = ""
    # token=""
    # @pytest.mark.smoke
    # sess = requests.session()
    def test_login(self):
        url = "http://api.id.aaa.test.mob.com/login/password/rsa"
        data = {
            "account": "V2@163.com",
            "password": "TGu+8Lm7Futjw6O9pUfNQXbuVZL6bFzqsZNY5FgL6C3WKtXdwjxYQO45Yr5fRP6dubR2DwpI4Crq/RbBmYycTRkS0y5mAu4BykX6Rzrpwxhfm6dW4PPcjj5/+lGkilRTqzAkgdlcA2hepuIuj8lPfJNcGN39bne4PWLokPQg3cXK0On7KeTP/G4/SY1km8qkCiqcE1Auw00tba/0pD0D2q2uChFe0751XjyiZuT6yQXbExW2ze13CcyKmJbvdEZbQ53/WnSlhQUOaHC4oaAy4K5el73T2td2kKXmA2UnKKDGPDAOQZlJskLHEWaUAc4OGS4A49PX1q3U84mIHtwzOw=="
        }
        # res = requests.post(url, json=date)
        res = RequestUtil().send_request(method="post",url=url,json=data)
        # res= Testuser.sess.request(method="post",url=url,json=data)
        # print(res.json())
        write_yaml({"token":res.json()['content']['token']})
        # Testuser.token= res.json()['content']['token']


    #查找前一次自动化创建的用户
    def test_userquery(self):
        #def方法里的变量为局部变量，要是想要其他方法可以用到这个变量，就需要用到global来声明
        global uerid1
        url = "http://rta-manage-sit.ing.mob.com/user/query"
        data = {
            "user3aId": "",
            "username": "",
            "pageNo": 1,
            "pageSize": 10
        }
        headers = {
            "token": read_yaml("token")
        }
        # res = requests.post(url,json=data,headers=headers)
        res = RequestUtil().send_request(method="post", url=url, json=data,headers=headers)
        # print(res.json())
        data1 =Testuser.list1 = res.json().get("data")
        # print(data1)
        for i in data1["list"]:
            username=i['username']
            uerid=i['userId']
            if username== "自动化测试":
                uerid1 = uerid
                # print(uerid1)

        assert res.status_code == 200
        # assert res.json()[]

    #删除自动化创建的用户
    def test_userdelete(self):

        url = "http://rta-manage-sit.ing.mob.com/user/delete"
        data = {
            "userId": uerid1
        }
        headers = {
            "token": read_yaml("token")
        }
        res = requests.delete(url,json=data,headers=headers)
        # print(uerid1)

        assert res.status_code == 200
        # print(res.json())
    #自动化创建用户
    def test_creatUser(self):

        url = "http://rta-manage-sit.ing.mob.com/user/save?"
        data = {
            "user3aId": "555111",
            "username": "自动化测试",
        }
        headers={
            "token" : read_yaml("token")
        }
        # res = requests.post(url,json=data,headers=headers)
        res = RequestUtil().send_request(method="post", url=url, headers=headers,json=data )

        # print(res.json())

        assert res.status_code == 200

# if __name__ == '__main__':
#     Testuser.test_userquery()
#     Testuser.test_userdelete()