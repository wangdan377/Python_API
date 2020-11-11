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


#分享
class Editor_filter:
#分享活动-全部活动
    def filter_01(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())
        showTypeList = ["all","1"]
        hotSort = ["0","1"]

        for i in showTypeList:
            for j in hotSort:
                url = 'http://47.99.180.185:2999/v1/share/activity/newest?page=1&pageSize=5&lang=zh_cn&hotSort='+j+'&showTypeList='+i

                res = get_req.get_model_a(sessionX, url)
                print(res)

                resCode = res['code']
                resText = res['text']

                assert ass.assert_code(resCode, 200)
                assert ass.assert_in_text(resText, '成功')
                Consts.RESULT_LIST.append('True')

        url = 'http://47.99.180.185:2999/v1/share/activity/newest?page=1&pageSize=5&lang=zh_cn&hotSort=1'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#分享活动-活动详情
    def filter_02(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/share/activity/detail?id=38&withApply=1&token=42537ab050198eb784560322b03dc9fd'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#分享活动-活动报名（线下活动）
    def filter_03(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/site/add_activity_apply'
        params ={}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#分享活动-我的活动
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/share/my/activitys?token=42537ab050198eb784560322b03dc9fd&type=1'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#分享活动-线下活动报名列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/share/activity/apply/users?activityId=14&page=1&pageSize=10'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#分享活动-线下活动报名列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/share/activity/alllist?lang=zh_cn&page=1&pageSize=10'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')








if __name__ == '__main__':
    a = Editor_filter()
    a.filter_01()


