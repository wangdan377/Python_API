import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class Act_feedback:
    def off_act(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/site/feedback/active'
        params = {'token':'8b6348fd70216febf117ef4240cf053f', 'feedbackId':'607'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Act_feedback()
    test.off_act()

