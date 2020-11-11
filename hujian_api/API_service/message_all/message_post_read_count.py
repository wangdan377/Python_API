import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

from message_all.login import off_login


class Message_post_read_count:
#每访问一次，消息阅读量累加1
#token      用户token
#notifyId   (/notify/list 列表里的id)
    def off_post_read_count(self, notifyId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/push/add_read_count'
        params = {'token':'12345678901234567890123456789012', 'notifyId':'1'}

        tokenData = off_login()

        params['token'] = tokenData
        params['notifyId'] = notifyId

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Message_post_read_count()
    test.off_post_read_count('100')


