import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class Third_login_url:
#平台: kuaishou, weibo, facebook, restream
#deviceId: 手机设备id
#userId
    def third_url(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'https://api.restream.io/login?response_type=code\\u0026client_id=10ff85d9-e5a8-488b-b473-7b750171ab7d\\u0026redirect_uri=https://service.zhiyun-tech.com/thirdparty/restream/callback\\u0026state=eyJzZXNzaW9uSWQiOjQ3LCJ1c2VySWQiOjEzLCJwbGF0Zm9ybSI6InJlc3RyZWFtIiwiZGV2aWNlSWQiOiJhYmQxMjMiLCJ0cyI6MTU5NDAyMTQ3Nn0='

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, 'success')
        Consts.RESULT_LIST.append('True')


if __name__ =="__main__":
    test = Third_login_url()
    test.third_url()

