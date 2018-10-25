import requests
import json
from Common_DS.Session import Session
from Confing_DS.Config import Config
from Common_DS import Request
import pytest

class add():
    def __init__(self):
        self.evn = 'debug'




    # def login(self):
    #     header={
    #         "Content-Type":"application/x-www-form-urlencoded",
    #         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    #     }
    #     data={
    #         'username':'htadmin',
    #         'password':'ht123456'
    #     }
    #     url="https://ssotest.chexinhui.com/uaa/login"
    #     res =self.dsgj.post(url,data=data,headers=header)
    #
    #     # header = {
    #     #     'Connection': 'keep-alive',
    #     #     'Cookie': self.login(),
    #     #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    #     #
    #     # url1 = 'https://dsgjtest.chexinhui.com/dsgj/rest/vin/VinModelService/findModelList?vin=LE4GG3EBXFL362070'
    #     # res1 = self.dsgj.get(url1)
    #     # print(res1.text)

    def test_get_vin_info(self):
        Con = Config()
        request=Request.Request(self.evn)

        token =Con.get_conf(Con.TITLE_DEBUG,Con.VALUE_TOkEN)
        print(token)
        json_header = {'Authorization': 'bearer %s' % token}
        # print('读取%s：'%token)
        # # header_new = dict(headers[0], **json_header)
        url ='https://apiresttest.chexinhui.com/rest/vin/VinModelService/findModelList?vin=LE4GG3EBXFL362070'

        # res=self.dsgj.get(url,headers=header)
        reponse=request.get_request(url,json_header)
        print(reponse['text'])


    def add_part(self):
        Con = Config()
        request = Request.Request(self.evn)
        json_header = {
            'Authorization': 'bearer %s' % request.get_session,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
            }

        data={
            "evalPartAmount":"1",
            "partName":"车门1(前左)",
            "partId":"A20472053001",
            "partJyNo":"02c593092cc2fd1c8f925541cbc95fb1",
            "factPartCode":"A20472053001",
            "singlequantity":"1",
            "evalState":"A",
            "checkWaiting":"0",
            "handAddpartFlag":"1",
            "delFlag":"0",
            "fitBackFlag":"1",
            "partstandardname":"车门1(前左)",
            "standardgroupcode":"a49e457e41ba930f0bb2f41aad852645",
            "standardgroupname":"前车门",
            "standardpgroupcode":"7b60a39fc2a49bbac1b3426abb5ada4b",
            "standardpgroupname":"前车门",
            "figureCode":"61W72015",
            "figurePartSequence":"10",
            "updatedDate":"2018-10-24 09:41:09",
            "partGroupCode":"82d140a9ccfda05912c3ac9726b6b09b",
            "stdPartId":"2e0fac27292a2f3f70d692e34410fda",
        }
        url="https://apiresttest.chexinhui.com/rest/distribute/ShopCarService/addPart?processstatus=null&evalId=187782&stdPartId=2e0fac27292a2f3f70d692e34410fda0&modelId=2663545f549959e123ca1b872164d7c7"
        #url="https://dsgjtest.chexinhui.com/dsgj/rest/distribute/ShopCarService/addPart?processstatus=null&evalId=187782&stdPartId=2e0fac27292a2f3f70d692e34410fda0&modelId=2663545f549959e123ca1b872164d7c7"
        res=request.post_request(url,data,json_header)
        print(res['text'])

if __name__ == "__main__":
    test=add()
    # test.login()
    # test.test_get_vin_info()
    test.add_part()
    # test.SetUP()
    # test.add_part()