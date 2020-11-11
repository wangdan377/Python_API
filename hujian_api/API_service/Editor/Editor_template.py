import pytest
import allure
import requests
import json
import time
import random

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class Editor_filter:
    #登录
    def filter_00(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:3999/login'
        params = {'username':'admin@zhiyun-tech.com', 'password':'helloworld'}

        res = post_req.post_model_b(sessionX, url, params)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

        return sessionX


    #模板分类--不过滤语言
    def filter_01(self):
        times = int(time.time())
        rNumber = random.randint(1, 100)

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
                    "X-ZY-Production": "zycami"}

        res = requests.get('http://47.99.180.185:2999/v1/templates/types/list', headers)

        print(res.text)


    #模板列表--不过滤语言
    def filter_02(self,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())
        rNumber = random.randint(1,100)

        url = 'http://47.99.180.185:2999/v1/templates/list?page=1&pageSize=10&isPkg=0&typeId='+id

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


    #JSON格式模板详情
    def filter_03(self,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())
        rNumber = random.randint(1,100)

        url = 'http://47.99.180.185:2999/v1/templates/info?id='+id

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


    #zip格式模板详情--delete
    def filter_03_old(self,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())
        rNumber = random.randint(1,100)

        url = 'http://47.99.180.185:2999/v1/templates/download/url?id='+id

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#保存用户模板配置
    def filter_04(self):
        times = int(time.time())
        rNumber = random.randint(1, 100)

        params = {'token':'b967144003a781aa84b68da4446908c0','share_id':198077,'config':''}

        params['config'] = "{\"global\": {\"duration\": 4411167,\"effect\": {\"contrast\": 0.0, \"enable\": false, \"exposure\": 0.0, \"hue\": 0.0, \"saturation\": 0.0,\"sharpen\": 0.0, \"temperature\": 0.0, \"vignette\": 0.0},\"filter\": {\"enable\": false, \"strength\": 1.0, \"isLocalSource\": true}, \"musics\": [],\"mute\": false, \"render\": {\"renderSize\": \"16:9\"}, \"rotate\": {\"enable\": false, \"rotate\": 0},\"stickers\": [], \"timebase\": 1000000, \"volume\": 1.0}, \"slices\": [{\"duration\": 4411167,\
                                                                                             \"effect\": {\"contrast\": 0.0,\
                                                                                                        \"enable\": true,\
                                                                                                        \"exposure\": 0.0,\
                                                                                                        \"hue\": 0.0,\
                                                                                                        \"saturation\": 0.0,\
                                                                                                        \"sharpen\": 0.0,\
                                                                                                        \"temperature\": 0.0,\
                                                                                                        \"vignette\": 0.0},\
                                                                                             \"endTime\": 4411167,\
                                                                                             \"filter\": {\"enable\": true,\
                                                                                                        \"strength\": 1.0,\"isLocalSource\": true},\"mute\": false, \"rate\": 1.0,\"rotate\": {\"enable\": true,\"rotate\": 0},\"startTime\": 0,\"timebase\": 1000000,\"volume\": 1.0}],\"version\": 0}"





        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
                  'X-ZY-Platform':'android',
                  'X-ZY-Production':'zycami',
                  'X-ZY-Version':'1.1.1'}

        res = requests.post('http://47.99.180.185:2999/v1/templates/save', params, headers)

        print(res.text)




if __name__ == '__main__':
    a = Editor_filter()
    a.filter_03('234')


