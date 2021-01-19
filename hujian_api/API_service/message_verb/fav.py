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

class Fav:
#userId_S收藏postId_M
    def Off_20(self,postId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/share/post/fav'
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


#取消收藏
#userId_S取消收藏postId_M
    def Off_21(self,postId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/share/post/unfav'
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

