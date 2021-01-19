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
#平台: restream
#deviceId: 手机设备id
#appid
    def third_url(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'https://service.zhiyun-tech.com/thirdparty/v1/login/url?platform=restream&appid=10ff85d9-e5a8-488b-b473-7b750171ab7d&deviceId=036e5b01515aee872d2fdee4bb9617bf'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']
        resUri = eval(resText)['uri']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, 'success')
        Consts.RESULT_LIST.append('True')

        return resUri


if __name__ =="__main__":
    test = Third_login_url()
    print(test.third_url())

