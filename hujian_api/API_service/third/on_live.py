import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class On_live:
    def login(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api.zhiyun-tech.com/v1/login'
        params = {
            'username': '+8613418483933',
            'password': '12345678'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, 'success')
        Consts.RESULT_LIST.append('True')

    def login_2(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api.restream.io/login?response_type=code&client_id=10ff85d9-e5a8-488b-b473-7b750171ab7d&redirect_uri=https://service.zhiyun-tech.com/thirdparty/restream/callback&state=eyJzZXNzaW9uSWQiOjQxOCwicGxhdGZvcm0iOiJyZXN0cmVhbSIsImRldmljZUlkIjoiMDM2ZTViMDE1MTVhZWU4NzJkMmZkZWU0YmI5NjE3YmYiLCJhcHBpZCI6IjEwZmY4NWQ5LWU1YTgtNDg4Yi1iNDczLTdiNzUwMTcxYWI3ZCIsImVudiI6IiIsInRzIjoxNTk2MDEzMzE3fQ=='
        params = {
            'username': '+8613418483933',
            'password': '12345678'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, 'success')
        Consts.RESULT_LIST.append('True')


    def live(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://service.zhiyun-tech.com/public/v1/livevideo/publish'
        params = {'access_token': '66bd7eed528e42947bb140a128fdabb5338a9c7f',
                  'platform': 'restream', 'userid': '1720276',
                  'user_token': '9f1d860ab6e619682f92188720f6de70',
        }

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, 'success')
        Consts.RESULT_LIST.append('True')


if __name__ =="__main__":
    test = On_live()
    #test.login()
    test.live()

