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


class Message_del:
#删除消息
    def off_del(self, notifyId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/notify/del'
        params = {'token':'12345678901234567890123456789012', 'id':'1'}

        tokenData = off_login()

        params['token'] = tokenData
        params['id'] = notifyId

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Message_del()
    test.off_del('100')

