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


class Follow:
#userId_S关注userId_M
    def Off_follow(self,userId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/user/follow'
        params = {'token':'12345678901234567890123456789012', 'to':'1'}

        tokenData = off_login()

        params['token'] = tokenData
        params['to'] = str(userId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#userId_S取消关注userId_M
    def Off_unfollow(self,userId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/user/unfollow'
        params = {'token':'12345678901234567890123456789012', 'to':'1'}

        tokenData = off_login()

        params['token'] = tokenData
        params['to'] = str(userId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

if __name__ == "__main__":
    test = Follow()
    test.Off_follow(1788613)

