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
    def post_info(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://service-test.zhiyun-tech.com/purchase/v1/code/use'

        params = {'userid': 1788821, 'user_token': '9fb199651f2ac99d201027c47088c738',
                  'code': '9SP3DTOE5YSL',
                  'deviceId': '60C0C81B-2378-4D95-8D43-87DC3DA75DEF',
                  'lang': 'en',
                  "X-ZY-Platform": "android",
                  "X-ZY-Production": "zycami",
                  "X-ZY-Version": "1.0.15"}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, 'success')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Act()
    test.post_info()

