import pytest
import allure
import requests
import json
import time

from Templight import GetMysqlData
from Templight import GetMysqlDataSeller

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class Official_01:
#官网留言
#type--string反馈类型, feedback/advice/other
    def Off_01(self,userId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/site/add_feedback'
        params = {'name':'胡健','contact':'13418483933','content':'吃饭了没?','userId':1,'type':'feedback','mobileModel':'CL001','appVersion':'0.0.1','mobileOSVersion':'10.0.2','deviceModel':'360','images':'https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/zyplay/site_feedback/2018-10-24-11:53:05.jpg'}

        params['userId'] = userId

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#官网订阅
#手机, 邮箱手机二选一
    def Off_02(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/site/add_followmail'
        params = {'mobile':'13418483933', 'nickname':'hj'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#外链点击日志
    def Off_03(self,userId,linkId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/site/add_link_click_log'
        params = { 'linkId':1, 'token':'12134567890121345678901213456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        params['linkId'] = linkId

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
