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
# 购物车修改
    def Off_01(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/shoppingcart/update'
        params = {'token': '9e09c0bb436eff3e5cd98f02baf2f08b', 'skuId': '8', 'num': '3', 'isChecked': 1}

        time.sleep(1)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == '__main__':
    a = Official_01()
    a.Off_14()
