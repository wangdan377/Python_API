import pytest
import allure
import requests
import json
import time
import random

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class Editor_filter:
#注册
    def filter_0(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:3000/v1/register'
        params = {'username':'jj', 'password':'hujian123456'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

        return sessionX

#登录
    def filter_00(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:3000/v1/login'
        params = {'username':'jj.huu', 'password':'hujian123456'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

        return sessionX


#解绑手机或者邮箱
    def filter_01(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())
        rNumber = random.randint(1,100)

        url = 'http://47.99.180.185:2999/v1/unbind_email_or_mobile1/filters/types/list'
        params = {'token':'9fe7b132fd27451c0662cd51c401d55a','unbindType':'1'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


    def filter_0(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:3000/v1/register'
        params = {'username':'jj.huu@transcontinenta.nl', 'password':'hujian123456'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

        return sessionX

#登录
    def filter_000(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:3000/v1/sendvcode'
        params = {'username':'huj@zhiyun-tech.com', 'lang':'en'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

        return sessionX



if __name__ == '__main__':
    a = Editor_filter()
    a.filter_0()


