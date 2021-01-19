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
#userId_S添加circle（需要后台审核：通过，不通过）
    def Off_circle_add(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:3000/v1/circle/addCircle'
        params = {'name':'胡健的circle2', 'des':'好的好的', 'token':'12345678901234567890123456789012', 'address':'深圳市'}

        tokenData = off_login()

        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Circle()
    test.Off_circle_add()

