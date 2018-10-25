"""
创建案件单子
https://dshitest.chexinhui.com/cxh/dist/#/
"""

from Confing.Config import Config
from Common import Request
from Base.PublicBase import MyBaseTest
from Params.params import Basic
from Common.Assert import Assertions
from Common.Base import check_json_value,count_data
from Common.allure import Allure

import json


class FirstTracking(MyBaseTest):

    def setUp(self):
        self.evn ='debug'


    def test_0001_add(self):
        """创建新单"""
        Con=Config()
        test=Assertions()
        allure=Allure()
        reques= Request.Request(self.evn)

        data=Basic()
        urls=data.url
        parms=data.data
        headers=data.header

        Con.set_item(Con.TITLE_DATA,Con.VALUE_policyNo,self.create_time() + '-' + self.create_unix())
        Con.set_item(Con.TITLE_DATA,Con.VALUE_reportNo,self.create_time() + '-' + self.create_unix())
        Con.set_item(Con.TITLE_DATA,Con.VALUE_reporttime,self.create_time())

        policyNo = Con.get_conf(Con.TITLE_DATA, Config.VALUE_policyNo)
        reportNo = Con.get_conf(Con.TITLE_DATA, Config.VALUE_reportNo)

        json_data ={'reportDate':self.create_now_time(),
                    "insuranceComName": Con.insuranceComName,
                    "insuredPerson": Con.insuredPerson,
                    "policyNo":policyNo,
                    "reportNo":reportNo,
                    }

        data_new =dict(parms[0],**json_data)

        json_header={'Authorization': 'bearer %s' % reques.get_session}
        header_new=dict(headers[0],**json_header)

        host = Con.host_debug
        req_url ='https://'+ host

        api_url = req_url + urls[0]['url_1']
        response = reques.post_request(api_url,json.dumps(data_new), header_new)

        allure.allure_step('第一步', '添加单子',(response['stats']))
        assert test.assert_code(response['code'], 200)
        assert test.assert_text((response['stats'])['success'],True)

        #查询事故号：
        req_url_1 = 'https://' + host
        url_find = req_url_1+ urls[0]['url_2']+'&policyNo='+ policyNo+'&reportDate='

        res = reques.get_request(url_find,json_header)
        Con.set_item(Con.TITLE_DATA, Con.VALUE_reporttid,res['jsons']['rows'][0]['id'])
        allure.allure_step('第二步', '查询单子','事故号id为：%s' %res['jsons']['rows'][0]['id'])
        print('事故号id为：%s' %res['jsons']['rows'][0]['id'])



    def test_0002_a_precisefind(self):
        """
        根据被保险人查询单子
        :return:
        """
        Con = Config()
        test = Assertions()
        allure = Allure()
        reques = Request.Request(self.evn)
        data = Basic()

        urls = data.url
        parms = data.data
        headers = data.header

        json_header = {'Authorization': 'bearer%s' % reques.get_session}

        host = Con.host_debug
        req_url = 'https://' + host

        test_data=Con.get_conf(Con.TITLE_DATA, Config.VALUE_insuredPerson)
        api_url = req_url + urls[0]['url_2']+ test_data
        response = reques.get_request(api_url,json_header)
        allure.allure_step('第一步','查询单子','根据被保险人，精准查询单子数量：%s'%response['jsons']['total'])
        print('根据被保险人，精准查询单子数量：%s'%response['jsons']['total'])
        assert test.assert_text(response['jsons']['total']>1,True)

    def test_0002_b_vaguefind(self):
        """
        根据被保险人模糊查询单子
        :return:
        """
        Con = Config()
        test = Assertions()
        allure = Allure()
        reques = Request.Request(self.evn)
        data = Basic()

        urls = data.url
        parms = data.data
        headers = data.header

        json_header = {'Authorization': 'bearer%s' % reques.get_session}

        host = Con.host_debug
        req_url = 'https://' + host

        test_data=Con.get_conf(Con.TITLE_DATA, Config.VALUE_insuredPerson)
        split_res =test_data.split('-')
        api_url = req_url + urls[0]['url_2']+ split_res[0]
        response = reques.get_request(api_url,json_header)
        allure.allure_step('第一步', '查询单子', '根据被保险人，模糊查询单子数量：%s' % response['jsons']['total'])
        print('根据被保险人，模糊查询单子数量：%s'%response['jsons']['total'])
        assert test.assert_text(response['jsons']['total'] > 1, True)

    def test_0002_c_precisefind(self):
        """
        根据事故号查询单子
        :return:
        """
        Con = Config()
        test = Assertions()
        allure = Allure()
        reques = Request.Request(self.evn)
        data = Basic()

        urls = data.url
        parms = data.data
        headers = data.header

        json_header = {'Authorization': 'bearer%s' % reques.get_session}

        host = Con.host_debug
        req_url = 'https://' + host

        test_data=Con.get_conf(Con.TITLE_DATA, Config.VALUE_reportNo)
        api_url = req_url + urls[0]['url_3']+ test_data
        response = reques.get_request(api_url,json_header)
        allure.allure_step('第一步','查询单子','根据事故号，精准查询单子数量：%s'%response['jsons']['total'])
        print('根据事故号，精准查询单子数量：%s'%response['jsons']['total'])
        assert test.assert_text(response['jsons']['total'] > 1, True)

    def test_0002_d_vaguefind(self):
        """
        根据事故号模糊查询单子
        :return:
        """
        Con = Config()
        test = Assertions()
        allure = Allure()
        reques = Request.Request(self.evn)
        data = Basic()

        urls = data.url
        parms = data.data
        headers = data.header

        json_header = {'Authorization': 'bearer%s' % reques.get_session}

        host = Con.host_debug
        req_url = 'https://' + host

        test_data=Con.get_conf(Con.TITLE_DATA, Config.VALUE_reportNo)
        split_res =test_data.split('-')
        api_url = req_url + urls[0]['url_3']+ split_res[0]
        response = reques.get_request(api_url,json_header)
        allure.allure_step('第一步', '查询单子', '根据事故号，模糊查询单子数量：%s' % response['jsons']['total'])
        print('根据事故号，模糊查询单子数量：%s'%response['jsons']['total'])
        assert test.assert_text(response['jsons']['total'] > 1, True)

    def test_0002_e_precisefind(self):
        """
        根据报案时间查询单子
        :return:
        """
        Con = Config()
        test = Assertions()
        allure = Allure()
        reques = Request.Request(self.evn)
        data = Basic()

        urls = data.url
        parms = data.data
        headers = data.header

        json_header = {'Authorization': 'bearer%s' % Con.token_debug}

        host = Con.host_debug
        req_url = 'https://' + host

        test_data=Con.get_conf(Con.TITLE_DATA, Config.VALUE_reporttime)
        api_url = req_url + urls[0]['url_4']+ test_data
        print(api_url)
        response = reques.get_request(api_url,json_header)
        allure.allure_step('第一步','查询单子','根据报案时间，精准查询单子数量：%s'%response['jsons']['total'])
        print('根据报案时间，精准查询单子数量：%s'%response['jsons']['total'])
        assert test.assert_text(response['jsons']['total'] > 1, True)


    def test_0002_del(self):
        """
        测试用例：模拟删除保单
        :return:
        """
        pass
        # Con = Config()
        # test = Assertions()
        # allure = Allure()
        # reques = Request.Request(self.evn)
        # data = Basic()
        #
        # urls = data.url
        # parms = data.data
        # headers = data.header
        #
        #
        # del_id = Con.get_conf(Con.TITLE_DATA, Config.VALUE_reporttid)
        #
        #
        # json_header = {'Authorization': 'bearer%s' % Con.token_debug}
        # header_new = dict(headers[2], **json_header)
        #
        # host = Con.host_debug
        # req_url = 'https://' + host
        #
        # api_url = req_url + urls[2]
        #
        # # dels_id =[]
        # # dels_id.append(str(del_id))
        # # print(dels_id)
        # dels_id =['f06d750ad6e6472c9257cf74dbfaae07']
        # response = reques.post_request(api_url,dels_id, header_new)
        # print(response['json'])



    def test_0003_a_saveFirstTrackPojo(self):
        """
        诊疗类型：无治疗--暂存
        :return:
        """
        Con = Config()
        test = Assertions()

        allure = Allure()
        reques = Request.Request(self.evn)
        data = Basic()

        urls = data.url
        parms = data.data
        headers = data.header

        #不用初始化
        id = Con.get_conf(Con.TITLE_DATA, Config.VALUE_injureCaseId)  # 获取id
        policyNo = Con.get_conf(Con.TITLE_DATA, Config.VALUE_policyNo)  # 获取保单号
        reportNo = Con.get_conf(Con.TITLE_DATA, Config.VALUE_reportNo)  # 获取事故号

        #初始化
        # diagnoseType=Con.get_conf(Con.TITLE_DATA,Config.VALUE_diagnoseType)#人伤类型
        # licensePlate = Con.get_conf(Con.TITLE_DATA, Config.VALUE_licensePlate)  # 获取车牌
        # accidentdutytype = Con.get_conf(Con.TITLE_DATA, Config.VALUE_accidentDutyType)  # 事故责任类型


        Con.set_item(Con.TITLE_DATA,Config.VALUE_time,self.create_now_time())#获取时间

        createDate =Con.get_conf(Con.TITLE_DATA,Config.VALUE_time)#创建时间

        injuredName =Con.get_conf(Con.TITLE_DATA,Config.VALUE_injuredName)#人伤姓名
        injuredCertificateNum = Con.get_conf(Con.TITLE_DATA, Config.VALUE_injuredCertificateNum)  # 身份证
        injuredCertificateType =Con.get_conf(Con.TITLE_DATA,Config.VALUE_injuredCertificateType)#证件类型
        injuredPhone =Con.get_conf(Con.TITLE_DATA,Config.VALUE_injuredPhone)#联系号码
        livingStatus =Con.get_conf(Con.TITLE_DATA,Config.VALUE_livingStatus)#生存状态
        # injuredBirthday =Con.get_conf(Con.TITLE_DATA,Config.VALUE_injuredBirthday)#伤者出生日期
        # injuredAge =Con.get_conf(Con.TITLE_DATA,Config.VALUE_injuredAge)#伤者年龄

        detailAddress =Con.get_conf(Con.TITLE_DATA,Config.VALUE_detailAddress)#常住地址
        injuredSex =Con.get_conf(Con.TITLE_DATA,Config.VALUE_injuredSex)#常住地址

        #赔偿标准信息
        compensateBasis =Con.get_conf(Con.TITLE_DATA,Config.VALUE_compensateBasis)#赔偿依据
        compensateYear =Con.get_conf(Con.TITLE_DATA,Config.VALUE_compensateYear)#赔偿年度
        industry =Con.get_conf(Con.TITLE_DATA,Config.VALUE_industry)#从事行业

        #案件处理信息
        trackRecord=Con.get_conf(Con.TITLE_DATA,Config.VALUE_trackRecord)#案件处理信息


        taskType = '01'  # 01-首次跟踪,02-后续跟踪,03-跟踪审核
        taskState = '1'  # 0-未开始,1-处理中,2-已完成

        #important info 单号重点
        check_json_value(parms[1], 'id', id)  # id
        check_json_value(parms[1], "policyNo", policyNo)  # 保单号
        check_json_value(parms[1], 'reportNo', reportNo, )  # 事故号
        #base info 基本信息
        check_json_value(parms[1], 'diagnoseType', Con.diagnoseType)#人伤类型0一般损伤，1残疾，2死亡
        check_json_value(parms[1], 'injureCaseId',id)#id
        check_json_value(parms[1], 'reportDate',self.create_now_time())#创建时间
        check_json_value(parms[1], 'createDate',self.create_now_time())#流入时间
        check_json_value(parms[1], "licensePlate","粤A12345")#c车牌号
        check_json_value(parms[1], "accidentDutyType",Con.accidentDutyType)#车牌号

        #user info 用户信息
        check_json_value(parms[1], "injuredName",injuredName)#伤亡人员
        check_json_value(parms[1], "injuredCertificateType",injuredCertificateType)#证件类型
        check_json_value(parms[1], "injuredCertificateNum",injuredCertificateNum)#身份证号码
        check_json_value(parms[1], "injuredPhone",injuredPhone,)#身份证电话
        check_json_value(parms[1], "livingStatus",livingStatus,)#生存状态

        res = count_data(injuredCertificateNum)
        check_json_value(parms[1], "injuredBirthday", res['data'])  # 伤者出生日期
        check_json_value(parms[1], "injuredAge", res['age'])  # 伤者年龄
        check_json_value(parms[1], "injuredSex", injuredSex)  # 伤者性别

        check_json_value(parms[1], "accidentSite","福建省-泉州市")#事故地
        check_json_value(parms[1], "accidentSiteId","350500")#事故地
        check_json_value(parms[1], "domicilePlace","福建省-泉州市")#户籍所在地
        check_json_value(parms[1], "domicilePlaceId","360100")#户籍所在地
        check_json_value(parms[1], "habitualResidence","江西省-南昌市")#经常居住地
        check_json_value(parms[1], "habitualResidenceId","360100")#经常居住地
        check_json_value(parms[1], "detailAddress",detailAddress)#常住地址

        #赔偿标准信息
        check_json_value(parms[1], "compensateBasis", compensateBasis)  # 赔偿标准
        check_json_value(parms[1], "compensateYear", compensateYear)  # 赔偿年度
        check_json_value(parms[1], "industry", industry)  # 赔偿年度
        #案件处理信息

        check_json_value(parms[1], "trackRecord", trackRecord)  # 赔偿年度

        #重点在这
        check_json_value(parms[1]['hidTrackInjureDiagnose'][0], 'injureCaseId', id)
        check_json_value(parms[1]['hidTrackCompensateFee'][0], 'injureCaseId', id)
        check_json_value(parms[1]['hidTrackCompensateFee'][0]['hidTrackCompensateDetail'][0], 'injureCaseId', id)



        json_header = {'Authorization': 'bearer%s' % reques.get_session}
        header_new = dict(headers[1], **json_header)



        # print(parms[1]['hidTrackInjureDiagnose'])
        print(parms[1])



        host = Con.host_debug
        req_url = 'https://' + host
        api_url = req_url + urls[1]

        response = reques.post_request(api_url,json.dumps(parms[1]), header_new)
        print(response['jsons'])
        # assert test.assert_in_text(response['jsons']['success'],True)
        print(parms[1])


    # def test_0003_a_saveFirstTrackPojo(self):
    #     """
    #     诊疗类型：无治疗--暂存
    #     :return:
    #     """
    #     Con = Config()
    #     test = Assertions()
    #
    #     allure = Allure()
    #     reques = Request.Request(self.evn)
    #     data = Basic()
    #
    #     urls = data.url
    #     parms = data.data
    #     headers = data.header
    #
    #     Con.set_item(Con.TITLE_DATA,Config.VALUE_time,self.create_now_time())#获取时间
    #     policyNo = Con.get_conf(Con.TITLE_DATA, Config.VALUE_policyNo)#获取保单号
    #     reportNo = Con.get_conf(Con.TITLE_DATA, Config.VALUE_reportNo)#获取事故号
    #     id=Con.get_conf(Con.TITLE_DATA,Config.VALUE_injureCaseId)#获取id
    #     diagnoseType=Con.get_conf(Con.TITLE_DATA,Config.VALUE_diagnoseType)#人伤类型
    #     licensePlate=Con.get_conf(Con.TITLE_DATA,Config.VALUE_licensePlate)#获取车牌
    #     accidentdutytype=Con.get_conf(Con.TITLE_DATA,Config.VALUE_accidentDutyType)#获取车牌
    #
    #     createDate =Con.get_conf(Con.TITLE_DATA,Config.VALUE_time)#创建时间
    #
    #     injuredName =Con.get_conf(Con.TITLE_DATA,Config.VALUE_injuredName)#人伤姓名
    #     injuredCertificateNum = Con.get_conf(Con.TITLE_DATA, Config.VALUE_injuredCertificateNum)  # 身份证
    #     injuredCertificateType =Con.get_conf(Con.TITLE_DATA,Config.VALUE_injuredCertificateType)#证件类型
    #     injuredPhone =Con.get_conf(Con.TITLE_DATA,Config.VALUE_injuredPhone)#联系号码
    #     livingStatus =Con.get_conf(Con.TITLE_DATA,Config.VALUE_livingStatus)#生存状态
    #     # injuredBirthday =Con.get_conf(Con.TITLE_DATA,Config.VALUE_injuredBirthday)#伤者出生日期
    #     # injuredAge =Con.get_conf(Con.TITLE_DATA,Config.VALUE_injuredAge)#伤者年龄
    #
    #     detailAddress =Con.get_conf(Con.TITLE_DATA,Config.VALUE_detailAddress)#常住地址
    #     injuredSex =Con.get_conf(Con.TITLE_DATA,Config.VALUE_injuredSex)#常住地址
    #
    #     #赔偿标准信息
    #     compensateBasis =Con.get_conf(Con.TITLE_DATA,Config.VALUE_compensateBasis)#赔偿依据
    #     compensateYear =Con.get_conf(Con.TITLE_DATA,Config.VALUE_compensateYear)#赔偿年度
    #     industry =Con.get_conf(Con.TITLE_DATA,Config.VALUE_industry)#从事行业
    #
    #     #案件处理信息
    #     trackRecord=Con.get_conf(Con.TITLE_DATA,Config.VALUE_trackRecord)#案件处理信息
    #
    #
    #     taskType = '01'  # 01-首次跟踪,02-后续跟踪,03-跟踪审核
    #     taskState = '1'  # 0-未开始,1-处理中,2-已完成
    #
    #     #important info 单号重点
    #     check_json_value(parms[1], 'id', id)  # id
    #     check_json_value(parms[1], "policyNo", policyNo)  # 保单号
    #     check_json_value(parms[1], 'reportNo', reportNo, )  # 事故号
    #
    #     #base info 基本信息
    #     check_json_value(parms[1], 'diagnoseType', diagnoseType)#人伤类型0一般损伤，1残疾，2死亡
    #     check_json_value(parms[1], 'injureCaseId',id)#id
    #     check_json_value(parms[1], 'reportDate',self.create_now_time())#创建时间
    #     check_json_value(parms[1], 'createDate',self.create_now_time())#流入时间
    #     check_json_value(parms[1], "licensePlate","粤A12345")#c车牌号
    #     check_json_value(parms[1], "accidentDutyType",accidentdutytype)#车牌号
    #
    #
    #     #user info 用户信息
    #     check_json_value(parms[1], "injuredName",injuredName)#伤亡人员
    #     check_json_value(parms[1], "injuredCertificateType",injuredCertificateType)#证件类型
    #     check_json_value(parms[1], "injuredCertificateNum",injuredCertificateNum)#身份证号码
    #     check_json_value(parms[1], "injuredPhone",injuredPhone,)#身份证电话
    #     check_json_value(parms[1], "livingStatus",livingStatus,)#生存状态
    #
    #     res = count_data(injuredCertificateNum)
    #     check_json_value(parms[1], "injuredBirthday", res['data'])  # 伤者出生日期
    #     check_json_value(parms[1], "injuredAge", res['age'])  # 伤者年龄
    #     check_json_value(parms[1], "injuredSex", injuredSex)  # 伤者性别
    #
    #     check_json_value(parms[1], "accidentSite","福建省-泉州市")#事故地
    #     check_json_value(parms[1], "accidentSiteId","350500")#事故地
    #     check_json_value(parms[1], "domicilePlace","福建省-泉州市")#户籍所在地
    #     check_json_value(parms[1], "domicilePlaceId","360100")#户籍所在地
    #     check_json_value(parms[1], "habitualResidence","江西省-南昌市")#经常居住地
    #     check_json_value(parms[1], "habitualResidenceId","360100")#经常居住地
    #     check_json_value(parms[1], "detailAddress",detailAddress)#常住地址
    #
    #     #赔偿标准信息
    #     check_json_value(parms[1], "compensateBasis", compensateBasis)  # 赔偿标准
    #     check_json_value(parms[1], "compensateYear", compensateYear)  # 赔偿年度
    #     check_json_value(parms[1], "industry", industry)  # 赔偿年度
    #     #案件处理信息
    #
    #     check_json_value(parms[1], "trackRecord", trackRecord)  # 赔偿年度
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #     json_header = {'Authorization': 'bearer%s' % Con.token_debug}
    #     header_new = dict(headers[1], **json_header)
    #
    #
    #     host = Con.host_debug
    #     req_url = 'https://' + host
    #     api_url = req_url + urls[1]
    #
    #     response = reques.post_request(api_url,json.dumps(parms[1]), header_new)
    #     print(response['jsons'])
    #     # assert test.assert_in_text(response['jsons']['success'],True)
    #     print(parms[1])



    def test_0003_b_SureFirstTrackPojo(self):
        """
        诊疗类型：无治疗--确认
        :return:
        """
        config = Config()
        id = config.get_kv('infromation', 'del_id')
        reportNo = config.get_kv('infromation', 'reportNo')
        policyNo = config.get_kv('infromation', 'policyNo')
        insuredPerson = config.get_kv('infromation', 'insuredPerson')
        reportDate = config.get_kv('infromation', 'reportDate')
        injureCaseId = config.get_kv('infromation', 'del_id')
        accidentNature = config.get_kv('details', 'accidentNature')  # 事故性质 01#单方事故，02#双方事故，03#多放，99#其他
        injuredType = config.get_kv('details', 'injuredType')  # 伤着类型
        licensePlate = config.get_kv('details', 'licenseplate')  # 车牌
        diagnoseType = config.get_kv('details', 'diagnoseType')  # 人伤类型
        treatType = config.get_kv('details', 'treatType')  # 诊疗类型
        accidentDutyType = config.get_kv('details', 'accidentDutyType')  # 事故责任类型
        injuredName = config.get_kv('details', 'injuredname')
        injuredCertificateType = config.get_kv('details', 'injuredcertificatetype')
        injuredCertificateNum = config.get_kv('details', 'injuredcertificatenum')
        injuredPhone = config.get_kv('details', 'injuredphone')
        livingStatus = config.get_kv('details', 'livingstatus')
        injuredBirthday = config.get_kv('details', 'injuredBirthday')
        injuredAge = config.get_kv('details', 'injuredage')
        injuredSex = config.get_kv('details', 'injuredsex')
        accidentSiteId = config.get_kv('details', 'accidentsiteid')
        domicilePlace = config.get_kv('details', 'domicileplace')
        habitualResidence = config.get_kv('details', 'habitualresidence')
        detailAddress = config.get_kv('details', 'detailaddress')
        task_id = config.get_kv('infromation', 'task_id')
        # 赔偿标准信息
        compensateBasis = config.get_kv('details', 'compensatebasis')
        compensateYear = config.get_kv('details', 'compensateyear')
        householdNature = config.get_kv('details', 'householdnature')
        industry = config.get_kv('details', 'industry')
        # 案件处理信息
        trackWay = config.get_kv('details', 'trackWay')
        trackRecord = config.get_kv('details', 'trackRecord')

        taskType= '02'#01-首次跟踪,02-后续跟踪,03-跟踪审核
        taskState = '0'#0-未开始,1-处理中,2-已完成

        # hidTrackInjureDiagnose 诊断信息
        # hidTrackCompensateFee  赔偿项目明细
        data = json.dumps({
            "hidInjureCase": {
                "diagnoseType": diagnoseType,
                "riskName": "",
                "accidentDutyPercent": 100,
                "avgYearIncome": "",
                "appellateCourtAddr": "",
                "injuredSex": injuredSex,
                "ruralConsumptionOutlay": "",
                "policyNo": policyNo,
                "urbanDisposableIncome": "",
                "thisCarDamageAmount": "",
                "biEndDate": "",
                "hospFoodSubsidiesStd": "",
                "occupationType": "",
                "licensePlate": licensePlate,
                "accommodationFeeStd": "",
                "reportDate": reportDate,
                "insuredPhone": "",
                "id": id,
                "insureEndDate": "",
                "injuredBirthday": injuredBirthday,
                "injuredType": injuredType,
                "urbanConsumptionOutlay": "",
                "habitualResidenceId": "",
                "accidentSiteId": accidentSiteId,
                "householdNature": householdNature,
                "auditCompleteStatus": "",
                "injuredContactsPhone": "",
                "ciInsComName": "",
                "accidentNature": accidentNature,
                "insuredPerson": insuredPerson,
                "insComCode": "",
                "dealPersonComName": "东升公司",
                "injuredCompany": "",
                "avgMonthIncome": "",
                "nurseFeeStd": "",
                "industry": industry,
                "resolveStatus": "2",
                "delFlag": "",
                "markName": "",
                "dealPersonComId": "10000",
                "biPolicyNo": "",
                "treatType": treatType,
                "denizenConsumptionOutlay": "",
                "createDate": reportDate,
                "accidentDate": "",
                "auditCompleteDate": "",
                "thesePaymentsStd": "",
                "injuredLibraryId": "",
                "denizenDisposableIncome": "",
                "otherCarDamageAmount": "",
                "policyType": "",
                "ciStartDate": "",
                "contactPhone": "",
                "insuranceComName": "",
                "insuranceComId": "",
                "injuredContacts": "",
                "biStartDate": "",
                "habitualResidence": habitualResidence,
                "dealPerson": "超级管理员",
                "sysBelongOrgCode": "10000",
                "transportationFeeStd": "",
                "ciInsComCode": "",
                "biInsComName": "",
                "injuredCertificateType": injuredCertificateType,
                "compensateBasis": compensateBasis,
                "injuredAge": injuredAge,
                "reportNo": reportNo,
                "compensateYear": compensateYear,
                "injuredPhone": injuredPhone,
                "modifyDate": reportDate,
                "standardSite": "",
                "riskCode": "",
                "injuredName": injuredName,
                "accidentSite": "",
                "livingStatus": livingStatus,
                "accidentDutyType": accidentDutyType,
                "lostIncomeStd": "",
                "insClassCode": "",
                "resolveAmount": "",
                "modifyPerson": "10000:admin",
                "caseType": "",
                "domicilePlaceId": "",
                "ciEndDate": "",
                "standardSiteId": "",
                "reportId": "",
                "resolveDate": "",
                "createPerson": "admin",
                "isMobileSurveyFlag": "",
                "appellateCourtAddressId": "",
                "injuredCertificateNum": injuredCertificateNum,
                "ciPolicyNo": "",
                "detailAddress": detailAddress,
                "domicilePlace": domicilePlace,
                "ruralNetIncome": "",
                "incomeStandard": "",
                "insureBeginDate": "",
                "biInsComCode": ""
            },
            "hidTrackHospital": [],
            "hidTrackInjureDiagnose": [{
                "id": "",
                "injureCaseId": "",
                "trackTaskId": "",
                "businessId": "",
                "treatmentHospCode": "",
                "diseaseId": "",
                "diseaseCode": "S27.311",
                "diseaseName": "开放性肺破裂",
                "icd10Code": "",
                "bodyPart": "",
                "warnRules": "",
                "treatmentEstimateFee": "",
                "firstDiagnose": "",
                "leftRight": [],
                "frontBack": [],
                "upDown": [],
                "isOperation": "0",
                "farNear": "近",
                "center": [],
                "delFlag": "",
                "createPerson": "",
                "createDate": "",
                "modifyPerson": "",
                "modifyDate": ""
            }],
            "hidTrackNurse": [],
            "hidTrackDisability": [],
            "hidTrackDeath": "",
            "hidTrackDependent": [],
            "hidTrackCompensateFee":[],
            "hidTrackTask": {
                "trackRecord": trackRecord,
                "resolveAmount": "",
                "dealPersonOrgId": "",
                "inputEndDate": "",
                "auditEndDate": "",
                "dealPerson": "admin",
                "resolveStatus": "2",
                "delFlag": "",
                "inputStartDate": "",
                "modifyPerson": "10000:admin",
                "taskType": taskType,
                "times": "",
                "taskState": "0",
                "id": task_id,
                "trackPerson": "",
                "receivedDate": "",
                "trackWay": trackWay,
                "createDate": reportDate,
                "previousTaskType": "",
                "injureCaseId": injureCaseId,
                "modifyDate": reportDate,
                "resolveDate": "",
                "auditCompleteDate": "",
                "dealPersonOrgName": "",
                "auditCompleteStatus": "",
                "createPerson": "admin",
                "isSplitadjustmentFlag": "",
                "inputPerson": "",
                "trackStartDate": "",
                "auditStartDate": "",
                "flowOrder": "",
                "isSmallCase": "",
                "auditPerson": "",
                "trackEndDate": "",
                "callTime": ""
            },
            "hidTrackRecord": "",
            "hidTrackTreatmentInfo": [],
            "hidHisTrackTask": []

        }
        )
        header = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': 'bearer%s' % config.get_kv('token', 'token')
        }
        url = self.url + '/hiserver/rest/dsinjureds/HidInjureCaseService/SureFirstTrackPojo'
        res = self.re_model.post(url, data=data, headers=header)
        print(res.text)
        # self.assertEqual(True,json.loads(res.text)['success'],'检查post数据或者服务器是否正常')

    def test_0004_a_saveNextTrackPojo(self):
        """
        诊疗类型：门诊治疗--暂存
        :return:
        """
        config=Config()
        id=config.get_kv('infromation','del_id')
        reportNo=config.get_kv('infromation','reportNo')
        policyNo=config.get_kv('infromation','policyNo')
        insuredPerson= config.get_kv('infromation','insuredPerson')
        reportDate = config.get_kv('infromation','reportDate')
        injureCaseId = config.get_kv('infromation','del_id')
        accidentNature=config.get_kv('details','accidentNature')#事故性质 01#单方事故，02#双方事故，03#多放，99#其他
        injuredType=config.get_kv('details','injuredType')#伤着类型
        licensePlate=config.get_kv('details','licenseplate')#车牌
        diagnoseType=config.get_kv('details','diagnoseType')#人伤类型
        treatType=config.get_kv('details','treatType2')#诊疗类型
        accidentDutyType=config.get_kv('details','accidentDutyType')#事故责任类型
        injuredName = config.get_kv('details','injuredname')
        injuredCertificateType = config.get_kv('details','injuredcertificatetype')
        injuredCertificateNum = config.get_kv('details','injuredcertificatenum')
        injuredPhone = config.get_kv('details','injuredphone')
        livingStatus = config.get_kv('details','livingstatus')
        injuredBirthday= config.get_kv('details','injuredBirthday')
        injuredAge = config.get_kv('details','injuredage')
        injuredSex = config.get_kv('details','injuredsex')
        accidentSiteId = config.get_kv('details','accidentsiteid')
        domicilePlace = config.get_kv('details','domicileplace')
        habitualResidence = config.get_kv('details','habitualresidence')
        detailAddress = config.get_kv('details','detailaddress')
        task_id=config.get_kv('infromation','task_id')
        # 赔偿标准信息
        compensateBasis = config.get_kv('details','compensatebasis')
        compensateYear = config.get_kv('details','compensateyear')
        householdNature = config.get_kv('details','householdnature')
        industry = config.get_kv('details','industry')
        # 案件处理信息
        trackWay=config.get_kv('details','trackWay')
        trackRecord=config.get_kv('details','trackRecord')

        #hidTrackInjureDiagnose 诊断信息
        #hidTrackCompensateFee  赔偿项目明细
        data=json.dumps({
                "hidInjureCase": {
                    "diagnoseType":diagnoseType,
                    "riskName": "",
                    "accidentDutyPercent":100,
                    "avgYearIncome": "",
                    "appellateCourtAddr": "",
                    "injuredSex":injuredSex,
                    "ruralConsumptionOutlay": "",
                    "policyNo": policyNo,
                    "urbanDisposableIncome": "",
                    "thisCarDamageAmount": "",
                    "biEndDate": "",
                    "hospFoodSubsidiesStd": "",
                    "occupationType": "",
                    "licensePlate":licensePlate,
                    "accommodationFeeStd": "",
                    "reportDate": reportDate,
                    "insuredPhone": "",
                    "id":id,
                    "insureEndDate": "",
                    "injuredBirthday":injuredBirthday,
                    "injuredType":injuredType,
                    "urbanConsumptionOutlay": "",
                    "habitualResidenceId": "",
                    "accidentSiteId":accidentSiteId,
                    "householdNature":householdNature,
                    "auditCompleteStatus": "",
                    "injuredContactsPhone": "",
                    "ciInsComName": "",
                    "accidentNature": accidentNature,
                    "insuredPerson":insuredPerson,
                    "insComCode": "",
                    "dealPersonComName": "东升公司",
                    "injuredCompany": "",
                    "avgMonthIncome": "",
                    "nurseFeeStd": "",
                    "industry":industry,
                    "resolveStatus": "2",
                    "delFlag": "",
                    "markName": "",
                    "dealPersonComId": "10000",
                    "biPolicyNo": "",
                    "treatType":treatType,
                    "denizenConsumptionOutlay": "",
                    "createDate": reportDate,
                    "accidentDate": "",
                    "auditCompleteDate": "",
                    "thesePaymentsStd": "",
                    "injuredLibraryId": "",
                    "denizenDisposableIncome": "",
                    "otherCarDamageAmount": "",
                    "policyType": "",
                    "ciStartDate": "",
                    "contactPhone": "",
                    "insuranceComName": "",
                    "insuranceComId": "",
                    "injuredContacts": "",
                    "biStartDate": "",
                    "habitualResidence":habitualResidence,
                    "dealPerson": "超级管理员",
                    "sysBelongOrgCode": "10000",
                    "transportationFeeStd": "",
                    "ciInsComCode": "",
                    "biInsComName": "",
                    "injuredCertificateType":injuredCertificateType,
                    "compensateBasis":compensateBasis,
                    "injuredAge":injuredAge,
                    "reportNo":reportNo,
                    "compensateYear":compensateYear,
                    "injuredPhone":injuredPhone,
                    "modifyDate": reportDate,
                    "standardSite": "",
                    "riskCode": "",
                    "injuredName":injuredName,
                    "accidentSite": "",
                    "livingStatus":livingStatus,
                    "accidentDutyType":accidentDutyType,
                    "lostIncomeStd": "",
                    "insClassCode": "",
                    "resolveAmount": "",
                    "modifyPerson": "10000:admin",
                    "caseType": "",
                    "domicilePlaceId": "",
                    "ciEndDate": "",
                    "standardSiteId": "",
                    "reportId": "",
                    "resolveDate": "",
                    "createPerson": "admin",
                    "isMobileSurveyFlag": "",
                    "appellateCourtAddressId": "",
                    "injuredCertificateNum":injuredCertificateNum,
                    "ciPolicyNo": "",
                    "detailAddress":detailAddress,
                    "domicilePlace":domicilePlace,
                    "ruralNetIncome": "",
                    "incomeStandard": "",
                    "insureBeginDate": "",
                    "biInsComCode": ""
                },
                "hidTrackHospital": [],
                "hidTrackInjureDiagnose":[{
                    "id": "",
                    "injureCaseId": "",
                    "trackTaskId": "",
                    "businessId": "",
                    "treatmentHospCode": "",
                    "diseaseId": "",
                    "diseaseCode": "S27.311",
                    "diseaseName": "开放性肺破裂",
                    "icd10Code": "",
                    "bodyPart": "",
                    "warnRules": "",
                    "treatmentEstimateFee": "",
                    "firstDiagnose":'true',
                    "leftRight": [],
                    "frontBack": [],
                    "upDown": [],
                    "isOperation": "0",
                    "farNear": "近",
                    "center": [],
                    "delFlag": "",
                    "createPerson": "",
                    "createDate": "",
                    "modifyPerson": "",
                    "modifyDate": ""
                }],
                "hidTrackNurse": [],
                "hidTrackDisability": [],
                "hidTrackDeath": "",
                "hidTrackDependent": [],
                "hidTrackCompensateFee": [{
                    "id": "",
                    "injureCaseId": "",
                    "trackTaskId": "",
                    "businessId": "",
                    "itemCode": "",
                    "itemName": "医疗门诊费",
                    "itemOrder": "",
                    "quantity": 2,
                    "ratio": 1,
                    "measureUnit": "项",
                    "feeType": "011",
                    "estimateAmount": 0,
                    "selfPayAmount": 0,
                    "reductionAmount": "",
                    "endEstimateAmount": 0,
                    "auditAmount": "",
                    "warnRules": "",
                    "auditRemark": "",
                    "delFlag": "",
                    "createPerson": "",
                    "createDate": "",
                    "modifyPerson": "",
                    "modifyDate": "",
                    "remark": "",
                    "hidTrackCompensateDetail": [{
                            "id": "",
                            "injureCaseId": "193a8404edff4bbbb8291708ba17d5d3",
                            "trackTaskId": "23c5cd0889d54ae8ae7a2674b673d62e",
                            "businessId": "",
                            "compensateFeeId": "",
                            "treatmentHospCode": "",
                            "feeProduceDate": "",
                            "feeType": "011",
                            "feeCategory": "0303",
                            "categoryId": "FA94DAFAA7434AB58ED2386A4DCB45FC",
                            "categoryName": "诊查费",
                            "itemId": "53D835C9496F460A991F4DEA26DDBB9F",
                            "itemName": "附加诊查费",
                            "localItemId": "",
                            "localItemName": "",
                            "measureUnit": "",
                            "useYear": "",
                            "uprice": "",
                            "quantity": "1",
                            "estimateAmount": "",
                            "selfPayRate": "",
                            "selfPayAmount": "",
                            "reductionAmount": "",
                            "reductionReasonCode": "",
                            "reductionReason": "",
                            "unableDeductionAmount": "",
                            "endEstimateAmount": "",
                            "limitFlag": "",
                            "manualInputFlag": "",
                            "delFlag": "",
                            "createPerson": "",
                            "createDate": "",
                            "modifyPerson": "",
                            "modifyDate": ""
                        },{
                            "id": "",
                            "injureCaseId": "193a8404edff4bbbb8291708ba17d5d3",
                            "trackTaskId": "23c5cd0889d54ae8ae7a2674b673d62e",
                            "businessId": "",
                            "compensateFeeId": "",
                            "treatmentHospCode": "",
                            "feeProduceDate": "",
                            "feeType": "011",
                            "feeCategory": "0302",
                            "categoryId": "FEEF1621C3A04192814215C44EE25C4D",
                            "categoryName": "护理费",
                            "itemId": "6F35D759D0AA457F9771162670659AEF",
                            "itemName": "传染病护理加收",
                            "localItemId": "",
                            "localItemName": "",
                            "measureUnit": "",
                            "useYear": "",
                            "uprice": "",
                            "quantity": "1",
                            "estimateAmount": "",
                            "selfPayRate": "",
                            "selfPayAmount": "",
                            "reductionAmount": "",
                            "reductionReasonCode": "",
                            "reductionReason": "",
                            "unableDeductionAmount": "",
                            "endEstimateAmount": "",
                            "limitFlag": "",
                            "manualInputFlag": "",
                            "delFlag": "",
                            "createPerson": "",
                            "createDate": "",
                            "modifyPerson": "",
                            "modifyDate": ""
                        }]
                },{
                    "id": "",
                    "injureCaseId": "",
                    "trackTaskId": "",
                    "businessId": "",
                    "itemCode": "",
                    "itemName": "医疗住院费",
                    "itemOrder": "",
                    "quantity": 0,
                    "ratio": 1,
                    "measureUnit": "项",
                    "feeType": "012",
                    "estimateAmount": 0,
                    "selfPayAmount": 0,
                    "reductionAmount": "",
                    "endEstimateAmount": 0,
                    "auditAmount": "",
                    "warnRules": "",
                    "auditRemark": "",
                    "delFlag": "",
                    "createPerson": "",
                    "createDate": "",
                    "modifyPerson": "",
                    "modifyDate": "",
                    "remark": "",
                    "hidTrackCompensateDetail": []
                }],
                "hidTrackTask": {
                    "trackRecord":trackRecord,
                    "resolveAmount": "",
                    "dealPersonOrgId": "",
                    "inputEndDate": "",
                    "auditEndDate": "",
                    "dealPerson": "admin",
                    "resolveStatus": "2",
                    "delFlag": "",
                    "inputStartDate": "",
                    "modifyPerson": "10000:admin",
                    "taskType": "01",
                    "times": "",
                    "taskState": "1",
                    "id":task_id,
                    "trackPerson": "",
                    "receivedDate": "",
                    "trackWay":trackWay,
                    "createDate":reportDate,
                    "previousTaskType": "",
                    "injureCaseId":injureCaseId,
                    "modifyDate": reportDate,
                    "resolveDate": "",
                    "auditCompleteDate": "",
                    "dealPersonOrgName": "",
                    "auditCompleteStatus": "",
                    "createPerson": "admin",
                    "isSplitadjustmentFlag": "",
                    "inputPerson": "",
                    "trackStartDate": "",
                    "auditStartDate": "",
                    "flowOrder": "",
                    "isSmallCase": "",
                    "auditPerson": "",
                    "trackEndDate": "",
                    "callTime": ""
                },
                "hidTrackRecord": "",
                "hidTrackTreatmentInfo": [],
                "hidHisTrackTask": []

            }
        )
        header = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': 'bearer%s' % config.get_kv('token', 'token')
        }
        url =self.url+'/hiserver/rest/dsinjureds/HidInjureCaseService/saveNextTrackPojo'
        res=self.re_model.post(url,data=data,headers=header)
        print(res.text)
        # self.assertEqual(True,json.loads(res.text)['success'],'检查post数据或者服务器是否正常')
