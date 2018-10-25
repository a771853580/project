import json
from Base.PublicBase import MyBaseTest

def check_json_value(dic_json, k, v):
    """
    变更json数据
    :param dic_json:
    :param k:
    :param v:
    :return:
    """
    res =[]
    if isinstance(dic_json, dict):
        for key in dic_json:
            if key == k:
                dic_json[key] = v
                res.append(dic_json[key])
            elif isinstance(dic_json[key], dict):
                check_json_value(dic_json[key], k, v)


def count_data(res):
    test=MyBaseTest
    res_data=dict()
    res_data['data'] = res[6:10]+'-'+res[10:12]+'-'+res[12:14]
    res_data['age'] = int(test.get_data_yera(test))-int(res[6:10])
    return res_data