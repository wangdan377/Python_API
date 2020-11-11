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


class Punish_verify_message_list:
#token  传token会返回用户是否已点赞,已收藏等
#type   通知这里传personal
    def off_list(self, type):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/notify/list'
        params = {'page': 1, 'pageSize': 20, 'token':'12345678901234567890123456789012', 'type':'personal', 'lang':'en'}

        tokenData = off_login()

        params['token'] = tokenData
        params['type'] = type

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Punish_verify_message_list()
    test.off_list('notice')

