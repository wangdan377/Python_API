import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class Third_login_status:
#sessionid 请求登录返回的sessionid
    def third_status(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'https://service.zhiyun-tech.com/thirdparty/v1/login/status?sessionid=979'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, 'success')
        Consts.RESULT_LIST.append('True')


if __name__ =="__main__":
    test = Third_login_status()
    test.third_status()

