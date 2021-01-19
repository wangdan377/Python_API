import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

from message_verb.login import off_login


class Like:
#userId_S点赞postId_M
    def off_like(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/share/post/like'
        params = {'token':'12345678901234567890123456789012', 'postId':'305023'}

        tokenData = off_login()
        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#userId_S在圈子circleId_M点赞postId_M
    def off_like_circle(self, circleId_M, postId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/share/post/like'
        params = {'token':'12345678901234567890123456789012', 'postId':'1', 'circleId':1}

        tokenData = off_login()

        params['token'] = tokenData
        params['postId'] = str(postId_M)
        params['circleId'] = circleId_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#取消点赞
#userId_S取消点赞postId_M
    def Off_unlike(self,postId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:2999/v1/share/post/unlike'
        params = {'token':'12345678901234567890123456789012', 'postId':'1'}

        tokenData = off_login()

        params['token'] = tokenData
        params['postId'] = str(postId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Like()
    test.off_like()

