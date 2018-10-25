# @Time    : 2018/10/15  10:14
# @Author  : MissA
# @File    : Request.py


import requests
from Common_DS import Session


class Request:

    def __init__(self,env):
        """
        :param env:
        """
        self.session = Session.Session()
        self.get_session = self.session.get_session(env)


    def get_request(self,url,header):
        """
        get 请求
        :param url:
        :param header:
        :return:
        """
        response = requests.get(url = url,headers = header)
        response_dicts = dict()
        response_dicts['code'] = response.status_code
        response_dicts['stats'] = response.json()
        response_dicts['jsons'] = response.json()
        response_dicts['text'] = response.text
        return response_dicts

    def post_request(self,url,data,header):
        """
        post 请求
        :param url:
        :param header:
        :return:
        """
        response = requests.post(url = url,data=data,headers = header)
        # print(response.text)
        # print(json.loads(response.text)['success'])
        response_dicts = dict()
        response_dicts['code'] = response.status_code
        response_dicts['stats'] = response.json()
        response_dicts['jsons'] = response.json()
        response_dicts['text'] = response.text
        return response_dicts

