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


class Message_unread_count:
#未读消息数
#follow like comment notice message
    def off_unread_count(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/notify/unread_count'
        params = {'token':'12345678901234567890123456789012', 'lang':'en'}

        tokenData = off_login()

        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Message_unread_count()
    test.off_unread_count()

