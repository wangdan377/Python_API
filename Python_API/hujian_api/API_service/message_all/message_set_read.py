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


class Message_set_read:
#token  用户token
#id     消息里的 notifyId
#type   消息里的 type
#设置消息已读
    def off_read(self, type, notifyId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/notify/set_read'
        params = {'token':'12345678901234567890123456789012', 'id':'1', 'type':'1'}

        tokenData = off_login()
        print(tokenData)

        params['token'] = tokenData
        params['id'] = notifyId
        params['type'] = type

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Message_set_read()
    test.off_read('notice', '100')

