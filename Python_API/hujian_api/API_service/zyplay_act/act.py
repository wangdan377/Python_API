import pytest
import allure
import requests
import json
import time

from API_service.Common import Post
from API_service.Common import Get
from API_service.Common import Assert
from API_service.Common import Consts

class Act:
    def act_code(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()
        url = 'https://api-test.zhiyun-tech.com/v1/get_device_activation_code'
        #params = {'userId': 1340135, 'deviceModel': 551, 'deviceName': 'CRANE 2S_HUJ', 'serialNum': '7d406f04b010100', 'longitude': '120.123', 'latitude':'30.123'}
        params = {'userId': 1788821, 'deviceModel': 551, 'deviceName': 'SMOOTH-XS_HU', 'serialNum': '7D303904A000430', 'longitude': '120.123', 'latitude': '30.123'}
        #params = {'userId': 1340135, 'deviceModel': 550, 'deviceName': 'SMOOTH-X_HUJ', 'serialNum': '7D303904A000430', 'longitude': '120.123', 'latitude': '30.123'}
        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


    def post_info(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/add_app_device_activation_info'
        params = {'account': 'hujiantest112@zs.com',
                  'serialNum': '7D404504A010364', 'deviceModel': 551, 'deviceName': 'SMOOTH-XS_HU', 'appVersion': '1.0.17',
                  'longitude': '120.123', 'latitude': '30.123', 'activeCode': 'MTQ3MjU4MzY5MTI=',
                  'activeAt': '2020-08-28 15:20:40', 'activeStatus': '1', 'ex': '-'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Act()
    #test.act_code()
    test.post_info()


