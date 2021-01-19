import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

from message_all.login import off_login


class Circle_message_list:
    def off_circle_list(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/circle/circleMsgList'
        params = {'page': 1, 'pageSize': 20, 'token':'12345678901234567890123456789012'}

        tokenData = off_login()

        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Circle_message_list()
    test.off_circle_list()

