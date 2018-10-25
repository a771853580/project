from Base.PublicBase import MyBaseTest
from Confing import Config
import json


class AccountApi(MyBaseTest):

    def test_0001_get_jsession1(self):
        """
        测试用例:测试登陆
        """
        data = {
            'username': 'admin',
            'password': '12345'
        }
        res = self.re_model.post(self.url, data)


    def test_0001_get_jsession(self):
        """
        测试用例：获取jesssion
        """
        data={'username':self.username,'password':self.userpw}
        res_login=self.re_model.post(self.rs_login_url,data=data)
        self.assertStatusOk(res_login)



    def test_0002_get_token(self):
        """
        获取token
        :return:
        """
        config = Config()
        data={'username':'admin',
            'password':'12345',
            'client_id':'cxh',
            'grant_type':'password',
            'client_secret':'password'}
        header={
            'Accept':'application/json,text/plain,*/*',
            'Accept-Encoding':'gzip,deflate,br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive',
            'Content-Length':'86',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host': 'ssotest.chexinhui.com',
            'Origin': 'https://dshitest.chexinhui.com',
            'Referer': 'https://dshitest.chexinhui.com/cxh/dist/',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
        }
        try:
            res=self.re_model.post(self.rs_oauth,data=data,headers=header)
            config.set_item('token','token',json.loads(res.text)['access_token'])
            print(json.loads(res.text)['access_token'])
            return json.loads(res.text)['access_token']
        except Exception as e:
            print('连接失败，检查服务器：%s'%e)


    def test_0003_user(self):
        """
        :return:
        """
        config= Config()
        header={
            'Authorization':'bearer%s' % config.get_kv('token','token')
        }
        self.test_0001_get_jsession()
        url='https://apitest.chexinhui.com/hiserver/rest/org/user'
        res=self.re_model.get(url,headers=header)
        self.assertEqual('超级管理员', json.loads(res.text)['user']['userFullName'], '服务器通讯不正常，请修复')
        print(json.loads(res.text)['user']['userFullName'])

