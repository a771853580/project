
# @Time    : 2018/10/1510:46
# @Author  : MissA
# @File    : Config.py

import os.path
from configparser import ConfigParser

class Config:
    # titles:
    TITLE_DEBUG = "private_debug"
    TITLE_RELEASE = "online_release"
    TITLE_EMAIL = "mail"
    TITLE_DATA = 'create_bd'

    # values:
    # [debug\release]
    VALUE_TESTER = "tester"
    VALUE_ENVIRONMENT = "environment"
    VALUE_VERSION_CODE = "versionCode"
    VALUE_HOST = "host"
    VALUE_LOGIN_HOST = "loginHost"
    VALUE_LOGIN_INFO = "loginInfo"
    VALUE_TOkEN = "token"

    #data
    VALUE_time= 'create_time' #创建时间
    VALUE_InsuranceComName= 'insurancecomname'
    VALUE_insuredPerson = 'insuredperson'#被保险人
    VALUE_policyNo = 'policyno'#保单号
    VALUE_reportNo = 'reportno'#事故号
    VALUE_reporttime = 'reporttime'#报案时间
    VALUE_reporttid = 'reportid'#
    VALUE_injureCaseId = 'reportid'#人伤ID

    VALUE_accidentNature = 'accidentnature' #事故类型:01-当方事故
    VALUE_injuredType = 'injuredType'#伤者类型:#010 -第三着车辆损失
    VALUE_licensePlate= 'licensePlate'#车号码
    VALUE_diagnoseType= 'diagnoseType'#人伤类型：0-一般损伤，1，残疾
    VALUE_treatType= 'treatType'#诊疗类型：0
    VALUE_accidentDutyType= 'accidentDutyType'#事故责任：0
    VALUE_injuredCertificateNum='injuredCertificateNum'#身份证号码
    VALUE_injuredName ='injuredName'#人伤姓名
    VALUE_injuredCertificateType ='injuredCertificateType'#证件类型
    VALUE_injuredPhone ='injuredPhone'#联系号码
    VALUE_livingStatus ='livingStatus'#生存状态1、2，默认1
    # VALUE_injuredBirthday='injuredBirthday'#伤者出身日期
    # VALUE_injuredAge='injuredAge'#伤者年龄
    VALUE_injuredSex='injuredSex'#伤者性别

    VALUE_detailAddress='detailAddress'#常住地址

    VALUE_compensateBasis='compensateBasis'#赔偿依据
    VALUE_compensateYear='compensateYear'#赔偿年度
    VALUE_industry='industry'#赔偿年度

    VALUE_trackRecord = 'trackRecord'#案件处理信息















    # path address
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        #初始化ConfigParser、初始加载配置文件
        self.config = ConfigParser()
        self.logfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.config.read(self.logfile, encoding='utf-8')

        self.tester_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
        self.environment_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_ENVIRONMENT)
        self.versionCode_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_VERSION_CODE)
        self.host_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_HOST)
        self.loginHost_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_HOST)
        self.loginInfo_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_INFO)
        self.token_debug= self.get_conf(Config.TITLE_DEBUG,Config.VALUE_TOkEN)

        self.tester_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_TESTER)
        self.environment_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_ENVIRONMENT)
        self.versionCode_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_VERSION_CODE)
        self.host_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_HOST)
        self.loginHost_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_LOGIN_HOST)
        self.loginInfo_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_LOGIN_INFO)

        #test data
        self.insuranceComName=self.get_conf(Config.TITLE_DATA,Config.VALUE_InsuranceComName)
        self.insuredPerson=self.get_conf(Config.TITLE_DATA,Config.VALUE_insuredPerson)
        self.policyNo=self.get_conf(Config.TITLE_DATA,Config.VALUE_policyNo)
        self.reportNo=self.get_conf(Config.TITLE_DATA,Config.VALUE_reportNo)
        self.accidentNature=self.get_conf(Config.TITLE_DATA,Config.VALUE_accidentNature)
        self.injuredType=self.get_conf(Config.TITLE_DATA,Config.VALUE_injuredType)
        self.licensePlate=self.get_conf(Config.TITLE_DATA,Config.VALUE_licensePlate)
        self.treatType=self.get_conf(Config.TITLE_DATA,Config.VALUE_treatType)
        self.diagnoseType=self.get_conf(Config.TITLE_DATA,Config.VALUE_diagnoseType)
        self.accidentDutyType=self.get_conf(Config.TITLE_DATA,Config.VALUE_accidentDutyType)






    def delete_item(self, section, key):
        """
        删除节点和Key
        :param section:
        :param key:
        :return:
        """
        self.config.remove_option(section, key)

    def add_section(self, section):
        """
        添加节点名称
        :param section:
        :return:
        """
        self.config.add_section(section)

    def set_item(self, section, key, value):
        """
        添加节点、key、vaule
        :param section:
        :param key:
        :param value:
        :return:
        """
        self.config.set(section, key, value)
        with open(self.logfile, "w") as f:
            return self.config.write(f)

        # self.cfg_load()
        # self.config.set(section, key, value)
        # self.save()

    def cfg_load(self):
        '''
        加载配置文件
        :return:
        '''
        self.config.read(self.logfile)

    def get_conf(self,section,key):
        """
        读取key，vlues
        :return:
        """
        # self.cfg_load()
        return self.config.get(section,key)

    def save(self):
        """
        保存
        :return:
        """
        fp = open(self.logfile,'w')
        self.config.write(fp)
        fp.close()
        return fp

