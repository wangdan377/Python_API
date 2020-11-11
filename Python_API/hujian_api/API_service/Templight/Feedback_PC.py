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
#硬件型号列表
    def Off_01(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4006/feedback/hardwareModelList'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#固件版本列表
#product--string硬件名称
    def Off_02(self,product):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4006/feedback/firmwareList?product='+product

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#软件平台列表
    def Off_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4006/feedback/platformList'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#手机型号列表
#platform--string 软件平台ios,android
    def Off_04(self,platform):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4006/feedback/phoneModelList?platform='+platform

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#手机版本号列表
#platform--string	软件平台ios,android
#model--string	手机型号
    def Off_05(self,platform,model):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4006/feedback/phoneVersionList?platform'+platform+'&model='+model

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#app版本号列表
#platform--string 软件平台ios,android
    def Off_06(self,platform):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4006/feedback/appVersionList?platform='+platform

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#反馈列表
    def Off_07(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4006/feedback/feedbackList'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#创建反馈
#userId_S创建反馈
#type	string	类型
#hardmodel	string	硬件
#firmwareversion |string | 固件版本 | |platform |string | 软件平台 | |phonemodel	string	手机型号
#phoneversion |string | 手机版本 | |appversion	string	应用型号
#lang	string	语言
#frequency	string	频率
#title	string	标题
#des	string	描述
#attachments	string	附件（最多3个，url用英文逗号隔开）
#contact	string	联系方式
#remark	string
    def Off_08(self,userId_S):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        params = {'token': '12345678901234567890123456789012', 'type': '1001',\
                  'hardmodel':'WEEBILL LAB', 'firmwareversion' : '1.81( m0_1.11,m1_1.76)',\
                  'platform' : 'android','phonemodel' : 'HUAWEI','phoneversion' : 'v.2.3.4',\
                  'appversion': '2.2.5', 'lang': 'zh_cn','frequency': '1','title': '编辑反馈test',\
                  'des': '描述', 'attachments': 'https://zyfeedback.oss-cn-shenzhen.aliyuncs.com/feedbacktest/482/2019-04-28-04:08:15.mp4', \
                  'contact': '13418483933', 'remark': '备注'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/feedback/feedbackCreate'

        res = post_req.post_model_b(sessionX, url , params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#补充反馈
#id--int	反馈编号
#token--string
#extraDes--string	补充描述
#extraAttachments--string	补充附件
    def Off_09(self,userId_S,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        params = {'id':1 , 'token':'12345678901234567890123456789012' ,'extraDes':'补充下' ,\
                  'extraAttachments':'https://zyfeedback.oss-cn-shenzhen.aliyuncs.com/feedbacktest/482/2019-04-28-04:27:23.png'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = id

        url = 'http://172.16.2.101:4006/feedback/extraFeedback'

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#查看补充反馈
#userId查看反馈id
    def Off_10(self,userId_S,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/feedback/getExtraFeedback?id='+str(id)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#我的反馈列表
#userId_S查询'我'的反馈列表
    def Off_11(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/feedback/myFeedbackList?token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#查看反馈
#id--int 反馈id
#userId_S查看反馈id
    def Off_12(self,userId_S,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:4006/feedback/queryFeedback?token='+tokenData+'&id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#撤销反馈
#id--int 反馈编号
#userId_S撤销反馈id
    def Off_13(self,userId_S,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:4006/feedback/withdrawFeedback?token='+tokenData+'&id='+str(id)

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#编辑反馈
#id--int 反馈id
#userId_S编辑反馈id
#type--string 类型 1001 硬件反馈，1002 软件反馈， 1003 建议/其他
#hardmodel--string	硬件类型，对应zy.product_params
#firmwareversion |string | 固件版本 | + |platform |string | 软件平台 | + |phonemodel|	string|	手机型号
#phoneversion |string | 手机版本 | + | appversion |string |	应用型号
#lang--string	语言
#frequency--string	出现频率
#title--string	标题
#des--string	描述
#attachments--string	附件（最多3个，url用英文逗号隔开）
#contact--string	联系方式
#remark--string	备注
    def Off_14(self,userId_S,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        type = '1001'
        hardmodel = '5'
        firmwareversion = '1.78'
        platform = 'android'
        phonemodel = 'HUAWEI'
        phoneversion = 'v.2.3.4'
        appversion = '2.2.5'

        lang = 'en'
        frequency = '1'
        title = '编辑反馈test'
        des = '描述'
        attachments = 'https://zyfeedback.oss-cn-shenzhen.aliyuncs.com/feedbacktest/482/2019-04-28-04:08:15.mp4'
        contact = '13418483933'
        remark = '备注'

        url = 'http://172.16.2.101:4006/feedback/editFeedback?id='+str(id)+'&token='+tokenData+'&type='+type+'&hardmodel='+hardmodel+'&firmwareversion='+firmwareversion+'&platform='+platform+'&phonemodel='+phonemodel+'&phoneversion='+phoneversion+'&appversion='+appversion+'&lang='+lang+'&frequency='+frequency+'&title='+title+'&des='+des+'&attachments='+attachments+'&contact='+contact+'&remark='+remark

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#激活反馈
#id--int 反馈id
#userId_S激活反馈id
    def Off_15(self,userId_S,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:4006/back/feedback/activeFeedbackBack?token='+tokenData+'&id='+str(id)

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#获取公用ossToken
#access--r/rw,默认rw
#userId_S获取公用ossToken
    def Off_16(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/feedback/feedbackGetAliyunOSSToken?token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == '__main__':
    a = Official_01()
    a.Off_14()
