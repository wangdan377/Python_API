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


class Post_share:
#userId_S创建postId
    def post_01(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/share/post/create'
        params = {'token':'12345678901234567890123456789012'}

        tokenData = off_login()

        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#前置条件：先创建postId，userId_S发布share_post
    def Off_02(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/share/post/publish'
        params = {'token':'12345678901234567890123456789012', 'postId':'304783', 'sourceType': 'flash', 'sourceUrls':[], 'des': '这是测试', 'platform':'android'}

        tokenData = off_login()

        params['token'] = tokenData
        params['sourceUrls'] = ['','https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/zyplay/share/103640/6641/2020-03-06-11:56:50.mp4']

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

if __name__ =="__main__":
    test = Post_share()
    #test.post_01()
    test.Off_02()

