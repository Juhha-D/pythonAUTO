import json

import requests

class RequestUtil:

    sess = requests.session()
    def send_request(self,method,url,datas=None,**kwargs):
        method = str(method).lower()
        res = None
        if method == "get":
            res = RequestUtil.sess.request(method=method,url=url,params=datas,**kwargs)
        elif method =="post":
            if datas:
                datas = json.dumps(datas)
            res = RequestUtil.sess.request(method=method,url=url,data=datas,**kwargs)
        else:
            pass
        return res