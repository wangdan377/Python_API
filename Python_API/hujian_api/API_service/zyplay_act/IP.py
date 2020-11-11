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
    def post_info(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:3001/v1/check_sn_region'

        #params = {'sn': '7D601B05B010128', 'ip': '127.0.0.1',
        #          'longitude': '118.123', 'latitude': '30.123',
        #          'country_code_iso': 'USA', 'snId': '6206983'}

        params = {'sn': '7D601B05B010141', 'ip': '127.0.0.1',
                  'longitude': '120.123', 'latitude': '30.123',
                  'country_code_iso': 'CHN', 'snId': '6206984'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Act()
    test.post_info()

