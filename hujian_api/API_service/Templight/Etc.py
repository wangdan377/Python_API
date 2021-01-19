import pytest
import allure
import requests
import json
import time

from Templight import GetMysqlDataSeller
from Templight import GetMysqlData

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class Official_01:
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


#资源管理-列表接口
#tag    string	可选，资源标记，默认全部；编辑器模板，请前填写editor
    def Off_01(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/resource/list'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#资源管理-模板列表
    def Off_02(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/video/templates/list'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#阿里云跨域转码--提供阿里云视频转码功能
#fromBucket	string	源视频所在的Bucket
#inputObject	string	源视频Object
#outputObject	string	目标视频Object
    def Off_03(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/site/transcode'
        params = {'fromBucket':'zhiyundata', 'inputObject':'E:/wenti/7.mp4', 'outputObject':'E:/wenti/5.mp4'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#阿里云转码查询-提供阿里云视频转码是否完成的查询功能，如果同时跨域移动回源Bucket
#fromBucket	string	源视频所在的Bucket
#inputObject	string	源视频Object
#outputObject	string	目标视频Object
    def Off_04(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/site/queryfile'
        params = {'fromBucket':'zhiyundata', 'inputObject':'kmstest/5S3lab.mp4','outputObject':'kmstest/5S3labOut.mp4'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#经销商状态切换
#userId_S转换其状态
#token	string	是
#id	经销商id	number	是
#status	状态 1 下架 、2 上架、0删除；必须	number	是
    def Off_05(self,userId_S,id,status):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/seller/agent/status'
        params = {'token':'12345678901234567890123456789012', 'id':1,'status':0}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = id
        params['status'] = status

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == '__main__':
    a = Official_01()
    a.Off_03()
