from locust import HttpLocust,TaskSet,task
import json

class UserBehavior(TaskSet):
    """
    单个配件,测试规则引擎
    启动方法：locuts -f *.py --host=ip
    """
    @task()
    def test(self):
        header = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
        }
        data = {"name": '保险杠(前)'}
        #http://192.168.11.199:8081
        url = '/drools/rest/dsrule/PartsDisabilityService/partsDisabilitP'
        self.client.post(url,data=json.dumps(data),headers=header)

class WebUserLocust(HttpLocust):
    weight = 1
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0



