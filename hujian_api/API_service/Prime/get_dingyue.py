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
        url = 'https://service-test.zhiyun-tech.com/purchase/v1/subStatus'
        params = {'userid': 1788821, 'user_token': '70308f6314c80f03f0ef7123cc49fda7'}
        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, 'success')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Act()
    test.act_code()

