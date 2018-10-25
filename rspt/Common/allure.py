# @Time    : 2018/10/15  10:14
# @Author  : MissA
# @File    : Allure.py


import pytest
import allure

class Allure:
    #封装Allure，方便调用

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