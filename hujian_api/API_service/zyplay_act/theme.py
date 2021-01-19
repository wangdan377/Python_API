import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class Act:
    def act_code(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()
        url = 'https://api-test.zhiyun-tech.com/v1/device/bind/list'
        params = {'token': '185d1cf0fdec350ebd772b0596e5a2c1'}
        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Act()
    test.act_code()


