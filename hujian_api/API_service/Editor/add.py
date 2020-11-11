import pytest
import allure
import requests
import json
import time
import random

from Editor import Aaa

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class Editor_filter:
#登录
    def filter_00(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:3999/login'
        params = {'username':'admin@zhiyun-tech.com', 'password':'helloworld'}

        res = post_req.post_model_b(sessionX, url, params)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

        return sessionX


#新增模板
    def filter_01(self):
        a = Aaa.mod_data()
        sessionX = self.filter_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())
        rNumber = random.randint(1,100)

        url = 'http://47.99.180.185:3999/video/templates/create'
        params = a.params

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')




if __name__ == '__main__':
    a = Editor_filter()
    a.filter_01()


