import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

from message.login import off_login


class Circle:
#userId_S加入circleId_M（需要圈主审核：通过，不通过）
    def Off_circle_join(self, circleId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/circle/circleJoin'
        params = {'id':'1', 'token':'12345678901234567890123456789012'}

        tokenData = off_login()

        params['token'] = tokenData
        params['id'] = str(circleId_M)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#圈主审核列表
    def Off_circle_join_list(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/circle/circleJoinList'
        params = {'id':'319', 'token':'12345678901234567890123456789012'}

        tokenData = off_login()

        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#圈主审核
    def Off_circle_join_very(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/circle/circleJoinList'
        params = {'id':'8861', 'token':'12345678901234567890123456789012','type':0}

        tokenData = off_login()

        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ =="__main__":
    test = Circle()
    test.Off_circle_join_very()

