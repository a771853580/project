"""
创建案件单子
https://dshitest.chexinhui.com/cxh/dist/#/
"""

from Base.config_Base import Config
from Base.PublicBase import MyBaseTest
from Case.test_Account import AccountApi
from Params.params import Basic
import json
class FirstTracking(MyBaseTest):

    def setUp(self):
        self.url='https://apitest.chexinhui.com'

    def test_0001_add(self):
        """创建新单"""
        config=Config()
        data=Basic()
        urls=data.url
        parms=data.data
        headers=data.header
        json_data={'Authorization': 'bearer%s' % config.get_kv('token', 'token')}
        header_new=dict(headers[0],**json_data)


        config.set_item('infromation', 'reportNo', self.create_time() + '-' + self.create_unix())#保单号
        config.set_item('infromation', 'policyNo', self.create_time() + '-' + self.create_unix())#报案号

        insuredPerson=config.get_kv('infromation','insuredPerson')
        policyNo=config.get_kv('infromation','policyNo')
        InjureId=config.get_kv('infromation', 'del_id')

        reportNo=config.get_kv('infromation','reportNo')
        config.set_item('infromation','reportDate',self.create_now_time())
        config.set_item('infromation', 'Date', self.create_time())
        reportDate=self.create_now_time()

        null = ''
        data=json.dumps({"reportId":null,"insuranceComId":null,"insuranceComName":null,"insuredPerson":insuredPerson,"policyNo":policyNo,"reportNo":reportNo,"insClassCode":null,"riskCode":null,"riskName":null,"injuredType":null,"diagnoseType":null,"treatType":null,"insComCode":null,"markName":null,"contactPhone":null,"accidentDate":null,"reportDate":reportDate,"dealPerson":null,"dealPersonComId":null,"dealPersonComName":null,"sysBelongOrgCode":null,"accidentDutyType":null,"accidentDutyPercent":null,"injuredLibraryId":null,"injuredName":null,"injuredSex":null,"injuredPhone":null,"injuredCertificateType":null,"injuredCertificateNum":null,"injuredBirthday":null,"injuredAge":null,"injuredCompany":null,"injuredContacts":null,"livingStatus":null,"householdNature":null,"industry":null,"occupationType":null,"habitualResidenceId":null,"habitualResidence":null,"domicilePlaceId":null,"domicilePlace":null,"detailAddress":null,"appellateCourtAddressId":null,"appellateCourtAddr":null,"accidentSiteId":null,"accidentSite":null,"accidentNature":null,"compensateBasis":null,"compensateYear":null,"incomeStandard":null,"standardSiteId":null,"standardSite":null,"urbanDisposableIncome":null,"ruralNetIncome":null,"urbanConsumptionOutlay":null,"ruralConsumptionOutlay":null,"denizenDisposableIncome":null,"denizenConsumptionOutlay":null,"licensePlate":null,"thisCarDamageAmount":null,"otherCarDamageAmount":null,"resolveStatus":null,"resolveDate":null,"resolveAmount":null,"auditCompleteStatus":null,"auditCompleteDate":null,"insureBeginDate":null,"insureEndDate":null,"biPolicyNo":null,"biInsComCode":null,"biInsComName":null,"biStartDate":null,"biEndDate":null,"ciPolicyNo":null,"ciInsComCode":null,"ciInsComName":null,"ciStartDate":null,"ciEndDate":null,"policyType":null,"isMobileSurveyFlag":null,"delFlag":null,"createPerson":null,"createDate":null,"modifyPerson":null,"modifyDate":null,"id":null})
        # header={
        #     'Connection':'keep - alive',
        #     'Content-Type':'application/json;charset=UTF-8',
        #     'Authorization': 'bearer%s' % config.get_kv('token', 'token')
        # }
        # print('备注类型%s'%type(data))
        # print('备注类型%s'%type(header))
        url=self.url+urls[0]
        res=self.re_model.post(url,data,headers=header_new)
        print(res.text)
        #
        # header = {
        #     'Authorization': 'bearer%s' % config.get_kv('token', 'token')
        # }
        # url_find = self.url + '/hiserver/rest/dsinjureds/HidInjureCaseService/findFirstInjureCase?page=1&rows=10&insuredPerson=&policyNo=' + policyNo + '&reportDate='
        # res = self.re_model.get(url_find,headers=header)
        # config.set_item('infromation','del_id',json.loads(res.text)['rows'][0]['id'])
        # print('创建案件id为：%s'% json.loads(res.text)['rows'][0]['id'])
        #
        # InjureId = config.get_kv('infromation', 'del_id')
        # url_get_id=self.url+'/hiserver/rest/dsinjureds/HidInjureCaseService/findTackPojo?InjureId='+InjureId
        # res=self.re_model.get(url_get_id,headers=header)
        # config.set_item('infromation', 'task_id',json.loads(res.text)['hidTrackTask']['id'])
        # print('任务ID为：%s'%json.loads(res.text)['hidTrackTask']['id'])
        # print('保单号为：%s'%config.get_kv('infromation','policyno'))

    def test_0002_find(self):
        """
        查单单子数量和id
        :return:
        """
        config=Config()
        url=self.url+'/hiserver/rest/dsinjureds/HidInjureCaseService/findFirstInjureCase?page=1&rows=100'
        headers={
            'Authorization': 'bearer%s' % config.get_kv('token', 'token')
        }
        res=self.re_model.get(url,headers=headers)
        # print(json.loads(res.text)['rows'])
        for res_r in json.loads(res.text)['rows']:
            print((res_r)['id']+'--'+(res_r)['insuredPerson'])
            if config.get_kv('infromation','insuredperson')==(res_r)['insuredPerson']:
                config.set_item('infromation', 'del_id', (res_r)['id'])
                print( (res_r)['id'])

    def test_0002_del(self):
        """
        测试用例：模拟删除保单
        :return:
        """
        pass
        # config=Config()
        # url=self.url+'/hiserver/rest/dsinjureds/HidInjureCaseService/deleteHidInjureCase'
        # print(config.get_kv('infromation','del_id'))
        # data=json.dumps({'0':'d7943147186642c59420ea611db05bb1'})
        # headers={
        #     'Content-Type':'application/json;charset=UTF-8',
        #     'Authorization': 'bearer%s' % config.get_kv('token','token')
        # }
        # res=self.re_model.post(url,data=data,headers=headers)
        # print(res.text)

    def test_0002_a_findFirstInjureCase(self):
        """
        用例：按照被保险人查询保单信息
        :return:
        """
        config=Config()
        insuredPerson=config.get_kv('infromation','insuredperson')

        header={
            'Authorization': 'bearer%s' % config.get_kv('token', 'token')
        }
        self.allure_step('步骤1','使用被保险人查询',insuredPerson)
        url=self.url+'/hiserver/rest/dsinjureds/HidInjureCaseService/findFirstInjureCase?page=1&rows=10&insuredPerson='+insuredPerson+'&policyNo=&reportDate='
        res=self.re_model.get(url,headers=header)
        self.allure_step('步骤2','查询结果', '查询数量为：%s'%json.loads(res.text)['total'])
        print('查询数量为：%s' % json.loads(res.text)['total'])
        print(res.text)

    def test_0002_a1_findFirstInjureCase(self):
        """
        用例：按照被保险人模糊查询保单信息
        :return:
        """
        config=Config()
        insuredPerson=config.get_kv('infromation','insuredperson_name')

        header={
            'Authorization': 'bearer%s' % config.get_kv('token', 'token')
        }
        self.allure_step('步骤1','使用被保险人查询',insuredPerson)
        url=self.url+'/hiserver/rest/dsinjureds/HidInjureCaseService/findFirstInjureCase?page=1&rows=10&insuredPerson='+insuredPerson+'&policyNo=&reportDate='
        res=self.re_model.get(url,headers=header)
        self.allure_step('步骤2','查询结果', '查询数量为：%s'%json.loads(res.text)['total'])
        self.assertEqual(True,json.loads(res.text)['total']>=1,'查询失败，请检查是否有案件')
        print('查询数量为：%s' % json.loads(res.text)['total'])
        print(res.text)

    def test_0002_b_findFirstInjureCase(self):
        """
        用例：按照保单号查询保单信息
        :return:
        """
        config=Config()
        policyNo=config.get_kv('infromation','policyNo')

        header={
            'Authorization': 'bearer%s' % config.get_kv('token', 'token')
        }
        self.allure_step('步骤1','使用保单号查询',policyNo)
        url=self.url+'/hiserver/rest/dsinjureds/HidInjureCaseService/findFirstInjureCase?page=1&rows=10&insuredPerson=&policyNo='+policyNo+'&reportDate='
        res=self.re_model.get(url,headers=header)
        self.allure_step('步骤2','查询结果', '查询数量为：%s'%json.loads(res.text)['total'])
        print(res.text)

    def test_0002_b1_findFirstInjureCase(self):
        """
        用例：按照保单号模糊查询保单信息
        :return:
        """
        config = Config()
        policyNo = config.get_kv('infromation', 'policyNo_mh')

        header = {
            'Authorization': 'bearer%s' % config.get_kv('token', 'token')
        }
        self.allure_step('步骤1', '使用保单号查询', policyNo)
        url = self.url + '/hiserver/rest/dsinjureds/HidInjureCaseService/findFirstInjureCase?page=1&rows=10&insuredPerson=&policyNo=' + policyNo + '&reportDate='
        res = self.re_model.get(url, headers=header)
        self.allure_step('步骤2', '查询结果', '查询数量为：%s' % json.loads(res.text)['total'])
        self.assertEqual(True,json.loads(res.text)['total']>=1,'查询失败，请检查案件信息')
        print('查询数量为：%s' % json.loads(res.text)['total'])
        print(res.text)

    def test_0002_c_findFirstInjureCase(self):
        """
        用例：按照报案日期查询保单信息
        :return:
        """
        config=Config()
        reportDate=config.get_kv('infromation','reportDate')

        header={
            'Authorization': 'bearer%s' % config.get_kv('token', 'token')
        }
        self.allure_step('步骤1','报案日期查询',reportDate)
        url=self.url+'/hiserver/rest/dsinjureds/HidInjureCaseService/findFirstInjureCase?page=1&rows=10&reportDate='+reportDate

        res=self.re_model.get(url,headers=header)
        self.allure_step('步骤2','查询结果', '查询数量为：%s'%json.loads(res.text)['total'])
        self.assertEqual(json.loads(res.text)['total'],1,'查询案件数量错误，请检查')
        print('查询数量为：%s' % json.loads(res.text)['total'])
        print(res.text)

    def test_0002_d_findFirstInjureCase(self):
        """
        用例：按照报案日期模糊查询保单信息
        :return:
        """
        config=Config()
        reportDate=config.get_kv('infromation','Date')
        header={
            'Authorization': 'bearer%s' % config.get_kv('token', 'token')
        }
        self.allure_step('步骤1','报案日期查询',reportDate)
        url=self.url+'/hiserver/rest/dsinjureds/HidInjureCaseService/findFirstInjureCase?page=1&rows=10&reportDate='+reportDate
        res=self.re_model.get(url,headers=header)
        self.allure_step('步骤2','查询结果', '查询数量为：%s'%json.loads(res.text)['total'])
        self.assertEqual(True,json.loads(res.text)['total'] >= 1,'查询案件数量错误，请检查')
        print('查询数量为：%s' % json.loads(res.text)['total'])
        print(res.text)

    def test_0003_a_saveFirstTrackPojo(self):
        """
        诊疗类型：无治疗--暂存
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
        treatType=config.get_kv('details','treatType')#诊疗类型
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

        taskType='01'#01-首次跟踪,02-后续跟踪,03-跟踪审核
        taskState='1'#0-未开始,1-处理中,2-已完成


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
                    "taskType": taskType,
                    "times": "",
                    "taskState": taskState,
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
        url =self.url+'/hiserver/rest/dsinjureds/HidInjureCaseService/saveFirstTrackPojo'
        res=self.re_model.post(url,data=data,headers=header)
        print(res.text)
        # self.assertEqual(True,json.loads(res.text)['success'],'检查post数据或者服务器是否正常')

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
