#coding: utf-8 -*-
import json
import requests




date_json={
    "hidInjureCase": {
        "diagnoseType": "0",
        "riskName": "",
        "accidentDutyPercent": "100",
        "avgYearIncome": "",
        "appellateCourtAddr": "",
        "injuredSex": "2",
        "ruralConsumptionOutlay": "",
        "policyNo": "2018-10-19-1539912343973",
        "urbanDisposableIncome": "",
        "thisCarDamageAmount": "",
        "biEndDate": "",
        "hospFoodSubsidiesStd": "",
        "occupationType": "",
        "licensePlate": "粤A12345",
        "accommodationFeeStd": "",
        "reportDate": "2018-10-19 09:25:54",
        "insuredPhone": "",
        "id": "f3e0eb5307b642c3b86e8415120ba599",
        "insureEndDate": "",
        "injuredBirthday": "1990-02-02",
        "injuredType": "010",
        "urbanConsumptionOutlay": "",
        "habitualResidenceId": "360100",
        "accidentSiteId": "350500",
        "householdNature": "01",
        "auditCompleteStatus": "",
        "injuredContactsPhone": "",
        "accidentAddressl": "",
        "ciInsComName": "",
        "accidentNature": "01",
        "insuredPerson": "Test-person",
        "insComCode": "",
        "dealPersonComName": "东升公司",
        "injuredCompany": "",
        "avgMonthIncome": "",
        "nurseFeeStd": "",
        "industry": "J",
        "resolveStatus": "2",
        "delFlag": "",
        "markName": "",
        "dealPersonComId": "10000",
        "biPolicyNo": "",
        "treatType": "0",
        "denizenConsumptionOutlay": "",
        "createDate": "2018-10-19 09:25:54",
        "accidentDate": "",
        "auditCompleteDate": "",
        "thesePaymentsStd": "",
        "injuredLibraryId": "",
        "denizenDisposableIncome": "",
        "otherCarDamageAmount": "",
        "policyType": "",
        "ciStartDate": "",
        "contactPhone": "",
        "insuranceComName": "Test-comname",
        "insuranceComId": "",
        "injuredContacts": "",
        "biStartDate": "",
        "habitualResidence": "江西省-南昌市",
        "dealPerson": "超级管理员",
        "sysBelongOrgCode": "10000",
        "transportationFeeStd": "",
        "ciInsComCode": "",
        "biInsComName": "",
        "injuredCertificateType": "01",
        "compensateBasis": "03",
        "injuredAge": 28,
        "reportNo": "2018-10-19-1539912343973",
        "compensateYear": "2015",
        "injuredPhone": "15918912345",
        "modifyDate": "",
        "standardSite": "",
        "riskCode": "",
        "reportPerson": "",
        "injuredName": "test-user",
        "accidentSite": "福建省-泉州市",
        "livingStatus": "1",
        "accidentDutyType": "0",
        "lostIncomeStd": "",
        "insClassCode": "",
        "resolveAmount": "",
        "modifyPerson": "10000:admin",
        "caseType": "",
        "domicilePlaceId": "360100",
        "ciEndDate": "",
        "standardSiteId": "",
        "reportId": "",
        "resolveDate": "",
        "createPerson": "admin",
        "isMobileSurveyFlag": "",
        "appellateCourtAddressId": "",
        "injuredCertificateNum": "440505199002022222",
        "ciPolicyNo": "",
        "detailAddress": "test permanent add",
        "domicilePlace": "福建省-泉州市",
        "ruralNetIncome": "",
        "incomeStandard": "",
        "insureBeginDate": "",
        "biInsComCode": "",
        "accidentSiteLink": [
            "福建省",
            "福建省-泉州市"
        ],
        "domicilePlaceLink": [
            "江西省",
            "江西省-南昌市"
        ],
        "habitualResidenceLink": [
            "江西省",
            "江西省-南昌市"
        ]
    },
    "hidTrackHospital": [ ],
    "hidTrackInjureDiagnose": [
        {
            "id": "",
            "injureCaseId": "",
            "trackTaskId": "",
            "businessId": "",
            "treatmentHospCode": "",
            "diseaseId": "",
            "diseaseCode": "T01.301",
            "diseaseName": "下肢皮肤套脱伤",
            "icd10Code": "",
            "bodyPart": "",
            "warnRules": "",
            "treatmentEstimateFee": "",
            "firstDiagnose": "0",
            "leftRight": [ ],
            "frontBack": [ ],
            "upDown": [ ],
            "isOperation": "0",
            "farNear": [ ],
            "center": [ ],
            "delFlag": "",
            "createPerson": "",
            "createDate": "",
            "modifyPerson": "",
            "modifyDate": ""
        }
    ],
    "hidTrackNurse": [ ],
    "hidTrackDisability": [ ],
    "hidTrackDeath": "",
    "hidTrackDependent": [ ],
    "hidTrackCompensateFee": [
        {
            "id": "",
            "injureCaseId": "",
            "trackTaskId": "",
            "businessId": "",
            "itemCode": "",
            "itemName": "残疾辅助器具费",
            "itemOrder": "",
            "quantity": 1,
            "ratio": 1,
            "measureUnit": "项",
            "amount": 0,
            "feeType": "033",
            "estimateAmount": 1500,
            "selfPayAmount": 0,
            "reductionAmount": "",
            "endEstimateAmount": 1500,
            "auditAmount": "",
            "warnRules": "",
            "auditRemark": "",
            "delFlag": "",
            "createPerson": "",
            "createDate": "",
            "modifyPerson": "",
            "modifyDate": "",
            "remark": "",
            "hidTrackCompensateDetail": [
                {
                    "id": "",
                    "injureCaseId": "",
                    "trackTaskId": "f95be334434d4ceca2526627b0593476",
                    "businessId": "",
                    "compensateFeeId": "",
                    "treatmentHospCode": "",
                    "feeProduceDate": "",
                    "feeType": "033",
                    "categoryId": "0603",
                    "categoryName": "脊柱和颅部矫形器",
                    "itemId": "714EC0D099B25EC5E050A8C0230B71A5",
                    "itemName": "胸腰骶矫形器",
                    "localItemId": "",
                    "localItemName": "",
                    "measureUnit": "",
                    "useYear": "",
                    "uprice": "1500",
                    "quantity": "1",
                    "estimateAmount": 1500,
                    "selfPayRate": "",
                    "selfPayAmount": "",
                    "reductionAmount": "",
                    "reductionReasonCode": "",
                    "reductionReason": "",
                    "unableDeductionAmount": "",
                    "endEstimateAmount": 1500,
                    "limitFlag": "",
                    "manualInputFlag": "",
                    "delFlag": "",
                    "createPerson": "",
                    "createDate": "",
                    "modifyPerson": "",
                    "modifyDate": ""
                }
            ]
        }
    ],
    "hidTrackTask": {
        "trackRecord": "test trackRecord infromatin",
        "resolveAmount": "",
        "dealPersonOrgId": "",
        "inputEndDate": "",
        "auditEndDate": "",
        "dealPerson": "超级管理员",
        "resolveStatus": "2",
        "delFlag": "",
        "inputStartDate": "",
        "modifyPerson": "10000:admin",
        "taskType": "01",
        "times": 0,
        "taskState": "1",
        "locationSite": "",
        "id": "f3e0eb5307b642c3b86e8415120ba599",
        "trackPerson": "",
        "receivedDate": "",
        "trackWay": "02",
        "createDate": "2018-10-19 09:25:54",
        "previousTaskType": "",
        "injureCaseId": "f3e0eb5307b642c3b86e8415120ba599",
        "modifyDate": "2018-10-18 17:02:42",
        "resolveDate": "",
        "auditCompleteDate": "",
        "dealPersonOrgName": "",
        "callStartTime": "",
        "auditCompleteStatus": "",
        "createPerson": "admin",
        "isSplitadjustmentFlag": "",
        "inputPerson": "",
        "trackStartDate": "",
        "auditStartDate": "",
        "flowOrder": "",
        "isSmallCase": "",
        "locationCoordinate": "",
        "auditPerson": "",
        "trackEndDate": "",
        "callTime": ""
    },
    "hidTrackRecord": "",
    "hidTrackTreatmentInfo": [ ],
    "collectionStatus": 0
}

dic = {}
# def json_txt(dic_json):
#     if isinstance(dic_json, dict):  # 判断是否是字典类型isinstance 返回True false
#         for key in dic_json:
#             if isinstance(dic_json[key], dict):  # 如果dic_json[key]依旧是字典类型
#                 print("****key--：%s value--: %s" % (key, dic_json[key]))
#                 json_txt(dic_json[key])
#                 dic[key] = dic_json[key]
#             else:
#                 print("****key--：%s value--: %s" % (key, dic_json[key]))
#                 dic[key] = dic_json[key]

def json_txt(dic_json):
    if isinstance(dic_json, dict):  # 判断是否是字典类型isinstance 返回True false
        for key in dic_json:
            if isinstance(dic_json[key], dict):  # 如果dic_json[key]依旧是字典类型
                # print('1')
                # print("****key--：%s value--: %s" % (key, dic_json[key]))
                json_txt(dic_json[key])
                dic[key] = dic_json[key]
            # elif isinstance(dic_json[key],list) :
            #     print('检测列表数据')
            #     print("****key--：%s value--: %s" % (key, dic_json[key]))
            #     json_txt(dic_json[key])
            #     dic[key] = dic_json[key]
            else:
                print('2')
                print("*key--：%s value--: %s" % (key, dic_json[key]))
                dic[key] = dic_json[key]



def check_json_value(dic_json, k, v):
    if isinstance(dic_json, dict):
        for key in dic_json:
            if key == k:
                dic_json[key] = v
            elif isinstance(dic_json[key], dict):
                check_json_value(dic_json[key], k, v)

#
# def count_data(res):
#     res_data=dict()
#     # res_data['sex'] = int(res[16])% 2 ==0
#     res_data['sex'] = res[16]
#     res_data['data'] = res[6:10]+'-'+res[10:12]+'-'+res[12:14]
#     res_data['age'] = int(test.get_data_yera(test))-int(res[6:10])
#     return res_data

# def ssss():
#     header={
#         'Connection': 'keep-alive',
#         'Content-Type': 'application/json;charset=UTF-8',
#     }
#     data={
#         "name":'ABS传感器(后)'
#     }
#     res = requests.post('http://192.168.11.199:8081/drools/rest/dsrule/PartsDisabilityService/partsDisabilitP',data=json.dumps(data),headers=header)
#     print(res.text)



if __name__=='__main__':
    ssss()

    # json_txt(date_json)

    # print("date_json 变更前   :")
    # print(date_json)
    # check_json_value(date_json, "injureCaseId","f3e0eb5307b642c3b86e8415120ba599")
    # print("date_json 变更后   :")
    # print(date_json)

    # test=MyBaseTest
    # s='440505199002022212'
    #
    #
    # res=count_data(s)
    # print(res['data'])
    # print(res['age'])
    # print(res['sex'])
    # num = float(res['sex']) % 2==0
    # print('显示结果%s'%num)

    # print(s[6:14])
    # print(s[6:10]+'-'+s[10:12]+'-'+s[12:14])
    # print(int(test.get_data_yera(test))-int(s[6:10]))