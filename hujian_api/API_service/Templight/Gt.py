import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

class Gt:
#challenge码
    def getGt(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        true = True

        url = 'http://172.16.2.101:3000/v1/gt/register'

        res = get_req.get_model_a(sessionX, url)

        resText = res['text']
        resTextDict = eval(resText)
        challenge = resTextDict['challenge']
        gt = resTextDict['gt']

        codeList = []
        codeList.append(challenge)
        codeList.append(gt)

        url_validate = 'https://api.geetest.com/ajax.php?gt='+codeList[1]+'&challenge='+codeList[0]+'&pt=0&lang=zh-cn&callback=geetest_'+str(int(time.time())*1000)

        res_page = get_req.get_model_a(sessionX, url_page)


        print(res)

if __name__ == '__main__':
    a = Gt()
    sth = a.getGt()