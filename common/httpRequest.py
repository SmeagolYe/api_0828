import requests
from common.config import *

class HttpRequest:
    def __init__(self):
        self.session = requests.sessions.session()

    def request(self, method, url, data=None, json=None):
        method = method.upper()
        if type(data) == str:
            data = eval(data)

        url = config.get("api", "pre_url") + url

        if method == "GET":
            resp = self.session.request(method=method, url=url, params=data)
        elif method == "POST":
            if data:
                resp = self.session.request(method=method, url=url, data=data)
            else:
                resp = self.session.request(method=method, url=url, json=json)
        else:
            print("请求方法不是get或post")
            resp = None
        return resp

    def close(self):
        self.session.close()