import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

https://api.restream.io/login?response_type=code&client_id=10ff85d9-e5a8-488b-b473-7b750171ab7d&redirect_uri=https://service.zhiyun-tech.com/thirdparty/restream/callback&state=eyJzZXNzaW9uSWQiOjk3OSwicGxhdGZvcm0iOiJyZXN0cmVhbSIsImRldmljZUlkIjoiMDM2ZTViMDE1MTVhZWU4NzJkMmZkZWU0YmI5NjE3YmYiLCJhcHBpZCI6IjEwZmY4NWQ5LWU1YTgtNDg4Yi1iNDczLTdiNzUwMTcxYWI3ZCIsImVudiI6IiIsInRzIjoxNTk2Nzk5MTMxfQ==
class Access_token:
#platform 平台: kuaishou, weibo, facebook, restream
#deviceId 手机设备id
#userid  用户id
#code  第三方平台返回的code值
    def access_token(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'https://service.zhiyun-tech.com/thirdparty/v1/token/access_token'
        params = {'platform': 'restream', 'deviceId': '036e5b01515aee872d2fdee4bb9617bf', 'appid': '10ff85d9-e5a8-488b-b473-7b750171ab7d',
                  'code': 'e503e0cc188ad0d057308c7be3bee68b708a9901'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, 'success')
        Consts.RESULT_LIST.append('True')


if __name__ =="__main__":
    test = Access_token()
    test.access_token()

