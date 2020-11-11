import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class Official_01:
#获取设备激活码
    def Off_01(self:
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/get_device_activation_code?userId=100&deviceModel=Smooth3&deviceName=Crane207CE&serialNum=000000000000018&longitude=72.596639&latitude=23.238025'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机品牌列表
    def Off_02(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/v1/add_app_device_activation_info'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')
