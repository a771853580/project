"""
方便扩展设置
"""

import  time
import json,os
import  unittest
import requests
import allure,pytest
import configparser

class MyBaseTest(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        super(MyBaseTest, self).__init__(*args, **kwargs)

    def assertStatusOk(self,res):
        """
        先保证服务器借口可用的最基本检测
        :return:
        """
        status_code =res.status_code
        self.assertEqual(status_code,200,msg='检查服务器通讯是否正常')

    def create_unix(self):
        return (str(round(time.time()*1000))).strip()

    def allure_step(self,step,step_name,step_remark,):
        """
        allure 步骤说明
        :param step:
        :param step_name:
        :param step_remark:
        :return:
        """
        with  pytest.allure.step(step):
            allure.attach(step_name,str(step_remark))

    def allure_step_remark(self,step_name,step_remark):
        """
        allure备注说明
        :param step_name:
        :param step_remark:
        :return:
        """
        allure.attach(step_name, step_remark)

    def allure_create_pic(self,pic_url):
        """
        获取当前文件夹目录上一级并将图片写入本地
        :param pic_url:
        :return:
        """
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\data'
        response = self.rs_model.get(pic_url, stream=True)
        # 这里打开一个空的png文件，相当于创建一个空的txt文件,wb表示写文件
        with open(path+'\\'+self.create_time()+'.png', 'wb') as file:
            # 每128个流遍历一次
            for data in response.iter_content(128):
                # 把流写入到文件，这个文件最后写入完成就是，selenium.png
                file.write(data)  # data相当于一块一块数据写入到我们的图片文件中

    def create_now_time(self):
        """
        创建生成本地时间
        :return:
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def create_time(self):
        """
        创建日期
        :return:
        """
        return time.strftime("%Y-%m-%d", time.localtime())

    def get_data_yera(self):
        return time.strftime("%Y", time.localtime())

    def get_data_month(self):
        return time.strftime("%m", time.localtime())

    def get_data_data(self):
        return time.strftime("%d", time.localtime())

    def request_get_url(self,url,header):
        """
        请求完整的url
        :param url:
        :param header:
        :return:
        """
        return self.re_model.get(url,headers=header)


    def request_post_gj(self,url,data,headers):
        """
        Post定损工具url
        :param url:
        :param data:
        :param headers:
        :return:
        """
        return self.re_model.post(self.rs_dsgj_url+url,data,headers=headers)





