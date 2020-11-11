import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

class Official_02:
    #官网留言
    def Off_01(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/site/add_feedback'
        params = {'name':'胡健','contact':'13418483933','content':'吃饭了没?','userId':'','type':'feedback','mobileModel':'abc','appVersion':'1.1.1','mobileOSVersion':'1.1.1','deviceModel':'abc','images':'http://www.abc.com/a.jpg'}

        time.sleep(1)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

    #官网订阅
    def Off_02(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/site/add_followmail'
        params = {'mobile':'13418483933', 'nickname':'hj'}

        time.sleep(1)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

    #外链点击日志
    def Off_03(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/site/add_link_click_log'
        params = { 'linkId':1, 'token':'text_news/link_news'}

        time.sleep(1)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')



if __name__ == '__main__':
    a = Official_02()
    a.Off_03()
