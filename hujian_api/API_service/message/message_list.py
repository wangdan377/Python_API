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


class Message_list:
#userId消息列表
#type - follow like comment notice message
    def off_list(self,type):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/notify/list'
        params = {'token':'12345678901234567890123456789012', 'type':'1', 'lang':'en'}

        tokenData = off_login()

        params['token'] = tokenData
        params['type'] = type

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#未读消息数
    def off_unread_count(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/notify/unread_count'
        params = {'token':'12345678901234567890123456789012', 'lang':'en'}

        tokenData = off_login()

        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#设置消息已读
    def Off_read(self, type, notifyId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/notify/set_reade'
        params = {'token':'12345678901234567890123456789012', 'id':'1', 'type':'1'}

        tokenData = off_login()

        params['token'] = tokenData
        params['id'] = str(notifyId)
        params['type'] = type

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#设置类型已读
    def Off_read_type(self, type):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/notify/set_read_by_type'
        params = {'token':'12345678901234567890123456789012', 'type':'1'}

        tokenData = off_login()

        params['token'] = tokenData
        params['type'] = type

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#删除消息
    def Off_read_type(self, notifyId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/notify/del'
        params = {'token':'12345678901234567890123456789012', 'id':'1'}

        tokenData = off_login()

        params['token'] = tokenData
        params['id'] = type

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#消息阅读量计数
    def Off_read_type(self, notifyId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'https://api-test.zhiyun-tech.com/v1/push/add_read_count'
        params = {'token':'12345678901234567890123456789012', 'notifyId':'1'}

        tokenData = off_login()

        params['token'] = tokenData
        params['notifyId'] = notifyId

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

if __name__ == "__main__":
    test = Message_list()
    test.off_list('notice')
