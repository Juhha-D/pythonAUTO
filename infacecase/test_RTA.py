# import pytest
import requests
import json
import re

#这个是腾讯平台的回归case
from common.request_util import RequestUtil
from common.yaml_util import read_yaml

#这个请求的imei信息如下：
#"{\"78899\":{\"rate\":8.0,\"pkg\":\"78899\"}}"
class TestRta():

    def test_qqrta(self):

        url = "http://rta-api-sit.ing.mob.com/api/rtaTest"
        data = {
                "device": {
                    "imei_md5sum": "fffe4a290c9e208b2f08006dd850548f",
                    "os": 2
                },
                "id": "1",
                "exps": {
                    "exp_id": "206520"
                }
        }

        res = RequestUtil().send_request(method="post", url=url, json=data)
        a2 = str(res.text)
        ret = re.sub(r"(.+?):(\s*)(.+)", r"'\1':'\3',", a2)
        print(a2)
        print('{'+ret+'}')
        # print(type(res))
        # print(res.status_code)
        # print(res.text)
