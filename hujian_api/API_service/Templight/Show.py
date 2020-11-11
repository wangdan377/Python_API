import pytest
import allure
import requests
import json
import time

from requests_toolbelt import MultipartEncoder

from Templight import GetMysqlDataSeller
from Templight import GetMysqlData

from Common.Hash import my_md5

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class Official_01:
#提供手机号或邮箱登录
    def Off_0(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/login'
        params = {'username': 'huj@zhiyun-tech.com', 'password': '12345678'}

        res = post_req.post_model_b(sessionX, url, params)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

        return sessionX


    def Off_000(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/login'
        params = {'username': 'newnew', 'password': '12345678'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


    def Off_00(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/login'
        params = {'username': 'huj@zhiyun-tech.com', 'password': '12345678'}

        res = post_req.post_model_b(sessionX, url, params)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

        return sessionX


    def Off_13(self, userId_S, userId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/user/follow'
        params = {'token': '12345678901234567890123456789012', 'to': '1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = str(userId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#取消关注
#userId_S取消关注userId_M
    def Off_14(self,userId_S,userId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/user/unfollow'
        params = {'token':'12345678901234567890123456789012', 'to':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['to'] = str(userId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')



if __name__ == '__main__':
    a = Official_01()
    a.Off_14(103665,1)
