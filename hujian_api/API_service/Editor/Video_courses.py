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


#智云视频教程
class Editor_filter:
#教程分类列表
    def filter_01(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())
        langList = ["zh-cn","zh-tw","en","all"]

        for i in langList:
            url = 'http://47.99.180.185:2999/v1/courses/list?typeId=8&lang='+i

            res = get_req.get_model_a(sessionX, url)
            print(res)

            resCode = res['code']
            resText = res['text']

            assert ass.assert_code(resCode, 200)
            assert ass.assert_in_text(resText, '成功')
            Consts.RESULT_LIST.append('True')

        url = 'http://47.99.180.185:2999/v1/courses/list?typeId=8'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#分类基础信息
    def filter_02(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())
        langList = ["zh-cn", "zh-tw", "en"]

        for i in langList:
            url = 'http://47.99.180.185:2999/v1/courses/type?typeId=8&lang='+i

            res = get_req.get_model_a(sessionX, url)
            print(res)

            resCode = res['code']
            resText = res['text']

            assert ass.assert_code(resCode, 200)
            assert ass.assert_in_text(resText, '成功')
            Consts.RESULT_LIST.append('True')

        url = 'http://47.99.180.185:2999/v1/courses/type?typeId=8'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#获取课程视频
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())
        langList = ["zh-cn", "zh-tw", "en", "all"]

        for i in langList:

            url = 'http://47.99.180.185:2999/v1/courses/videos?courseId=8&lang='+i

            res = get_req.get_model_a(sessionX, url)
            print(res)

            resCode = res['code']
            resText = res['text']

            assert ass.assert_code(resCode, 200)
            assert ass.assert_in_text(resText, '成功')
            Consts.RESULT_LIST.append('True')

        url = 'http://47.99.180.185:2999/v1/courses/videos?courseId=8'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#获取产品课程视频
    def filter_04(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())
        langList = ["zh-cn", "zh-tw", "en", "all"]

        for i in langList:

            url = 'http://47.99.180.185:2999/v1/courses/product/videos?lang='+i+'&page=1&pageSize=12&code=C020110C'

            res = get_req.get_model_a(sessionX, url)
            print(res)

            resCode = res['code']
            resText = res['text']

            assert ass.assert_code(resCode, 200)
            assert ass.assert_in_text(resText, '成功')
            Consts.RESULT_LIST.append('True')

        url = 'http://47.99.180.185:2999/v1/courses/product/videos?page=1&pageSize=12&code=C020110C'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#获取教程视频
    def filter_05(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())
        rNumber = random.randint(1,100)

        url = 'http://47.99.180.185:2999/v1/courses/video/url?vid=3'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')




if __name__ == '__main__':
    a = Editor_filter()
    a.filter_05()


