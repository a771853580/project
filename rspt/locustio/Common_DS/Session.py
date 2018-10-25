# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 13:33
# @Author  : MissA
# @File    : Session.py

"""
封装获取token、session方法
"""

import requests
import json
from Confing_DS import Config
from Params_DS.params import Basic


class Session:
    def __init__(self):
        self.config = Config.Config()

    def get_session(self, env):

        """
        获取session
        :param env: 环境变量
        :return:
        """
        Con =Config.Config()
        data = Basic()
        urls=data.url

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        if env == "debug":
            login_url = 'http://' + self.config.loginHost_debug
            parm = eval(self.config.loginInfo_debug)
            session_debug = requests.session()
            res = session_debug.post(login_url, parm, headers=headers)
            Con.set_item(Con.TITLE_DEBUG,Con.VALUE_TOkEN, json.loads(res.text)['access_token'])
            # self.config.set_item(self.config.TITLE_DEBUG, 'test2', json.loads(res.text)['access_token'])
            return  json.loads(res.text)['access_token']

        elif env == "release":
            login_url = 'http://' + self.config.loginHost_release
            parm = self.config.loginInfo_release

            session_release = requests.session()
            response = session_release.post(login_url, parm, headers=headers)
            self.config.set_item(self.config.TITLE_DEBUG, self.config.VALUE_TOkEN,json.loads(response.text)['access_token'])
            # self.log.debug('cookies: %s' % response.cookies.get_dict())
            return json.loads(response.text)['access_token']

        else:
            print("get cookies error")
            # self.log.error('get cookies error, please checkout!!!')


if __name__ == '__main__':
    ss = Session()
    ss.get_session('debug')