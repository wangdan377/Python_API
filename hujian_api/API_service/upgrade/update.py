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


class Update:
#APP强制升级查询
    def off_update_APP(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/app/checkForceUpdate'
        params = {'platform':'iOS', 'channel':'AppStore', 'version':'1.8.4'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#APP固件升级查询v2
    def off_updateV2_firmware(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/firmware_update'
        params = {'env':'test', 'version':'1.90','lang':'en', 'code':1329}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

if __name__ == "__main__":
    a = Update()
    a.off_updateV2_firmware()