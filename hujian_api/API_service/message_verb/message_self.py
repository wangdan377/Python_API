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


class Message_self:
#userId_S发送私信给userId_M
    def off_send(self,userId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/notify/sendmessage'
        params = {'token':'12345678901234567890123456789012', 'to':1, 'content':'helloTest'}

        tokenData = off_login()

        params['token'] = tokenData
        params['to'] = userId_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#userId_S群发私信
#userId_list_M为'1,2,3,4'格式
    def Off_58(self, userId_list_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://api-test.zhiyun-tech.com/v1/notify/sendmessagebatch'
        params = {'token':'12345678901234567890123456789012', 'to_list':'1,2','content':'helloListTest'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['to_list'] = userId_list_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

if __name__ == "__main__":
    test = Message_self()
    test.off_send(1788613)

