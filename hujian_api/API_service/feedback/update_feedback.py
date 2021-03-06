import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class Post_feedback:
    def off_feedback(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/site/feedback/update'
        params = {'token':'e66b0d28e5a2e988aceb4bb35de310d2',
                  'id':'607', 'name':'hujiantest003', 'contact':'13418483933', 'title':'后台页面有问题3', 'content':'出BUG了',
                  'appVersion':'', 'deviceModel':'', 'type':'feedback_software', 'images':'', 'mobileModel':'', 'mobileOSVersion':'',
                  'user_lang':'zh_cn', 'firmwareVersion':'', 'frequency':'1', 'advice_target':'zycami'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Post_feedback()
    test.off_feedback()

