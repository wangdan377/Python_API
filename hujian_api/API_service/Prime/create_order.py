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

        url = 'https://service-test.zhiyun-tech.com/purchase/v1/createOrder'

        params = {'userid': 1788821, 'user_token': '70308f6314c80f03f0ef7123cc49fda7',
                  'packageName': 'com.zhiyun.cama', 'platform_product_id': 15, 'deviceId': '2453', 'lang': 'zh_cn',
                  'country_code_price_show': 'CHN￥15.00', 'country_code_price': '1500', 'country_code': 'CHN',
                  'channel': 'yyb', 'purchase_ids': ''}

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


