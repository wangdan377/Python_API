import pytest
import allure
import requests
import json
import time

from Templight import GetMysqlData

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

class Official_01:
#SDK配置列表
#platType--string 平台类型 Android IOS
    def Off_01(self,platType):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkVersionList?platType='+platType

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#SDK配置添加
    def Off_02(self,version,des,remark,sourceUrl,platType):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkVersionAdd?version='+version+'&des='+des+'&remark='+remark+'&sourceUrl='+sourceUrl+'platType='+platType


        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#SDK配置编辑回显
#id--int SDK编号
    def Off_03(self,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkVersionEditQuery?id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#SDK配置编辑提交
#id--SDK编号
    def Off_04(self,id,version,des,remark,sourceUrl,platType):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkVersionEditSubmit?id='+str(id)+'version='+version+'&des='+des+'&remark='+remark+'&sourceUrl='+sourceUrl+'platType='+platType


        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#SDK配置删除
#id--SDK编号
    def Off_05(self,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkVersionDel?id='+str(id)


        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#SDK配置开启及关闭开启
#id--SDK编号
    def Off_06(self,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkVersionOffOrOn?id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#参考文档管理列表
    def Off_07(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkDocumentList'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#参考文档管理添加
#lang--string	语言
#des--string	描述
#remark--string	备注
#sourceUrl--string	sdk文件url地址
#sort--int	排序编号
    def Off_08(self,lang,des,remark,sourceUrl,sort):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkDocumentAdd?lang='+lang+'&des='+des+'&remark='+remark+'&sourceUrl='+sourceUrl+'&sort='+str(sort)

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#参考文档管理编辑回显
#id--int参考文档编号
    def Off_09(self,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkDocumentEditQuery?id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#参考文档管理编辑提交
#id--参考文档id
#sort--排序设置顺序id
    def Off_10(self,id,lang,des,remark,sourceUrl,sort):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkDocumentEditSubmit?id='+str(id)+'&lang='+lang+'&des='+des+'&remark='+remark+'&sourceUrl='+sourceUrl+'&sort='+str(sort)


        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#参考文档管理删除
#id--参考文档id
    def Off_11(self,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkDocumentDel?id='+str(id)


        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')



#参考文档管理开启及关闭开启
#id--参考文档id
    def Off_12(self,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkDocumentDel?id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#开发者审核管理列表
#status--int 状态：0：删除，1：正常 2：待审核3:不通过
#nickName--string 用户名，模糊匹配
#按status和nickName条件查询
    def Off_13(self,nickName,status):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkUserList?nickName='+nickName+'&status='+str(status)


        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#开发者审核管理-审核回显
#id--开发者编号
    def Off_14(self,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkUserCheckQuery?id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#开发者审核管理-审核
#id--int 开发者编号
#feedback--string 审核反馈
#type--string 1通过 2不通过
    def Off_15(self,id,feedback,type):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/appsdk/appsdkUserCheck?id='+str(id)+'&feedback='+feedback+'&type='+type


        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#app开发者申请提交SDK
#userId_S为app开发者zy.userId
#type--string 申请人类型，个人：'personal',企业：'enterprise'
#token--string	token
#mail--string	邮箱（可选）
#firstName--string	名
#lastName--string	姓
#region--string	地区
#city--string	城市
#industry--string	行业
#career--string	职业（type为personal时填）
#usage--string	用途
#company--string	企业名（type为enterprise时填）
    def Off_16(self,userId_S):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData
        type = 'personal'
        firstName = 'hu'
        lastName = 'HU'
        region = '中国广东省'
        city =  '深圳市'
        industry = 'IT'
        career = 'tester'
        usage = '测试'

        url = 'http://172.16.2.101:3000/v1/appsdk/appsdkUserApplySubmit?type='+type+'&token='+tokenData+'&firstName='+firstName+'&lastName='+lastName+'&region='+region+'&city='+city+'&industry='+industry+'&career='+career+'&usage='+usage
        #params = {'type':'personal','token':'12345678901234567890123456789012','firstName':'hu','lastName':'HU','region':'中国广东省','city':'深圳市','industry':'IT','career':'tester','usage':'测试'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#APP开发者单个回显
#userId_S查询APP开发者
    def Off_17(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:3000/v1/appsdk/appsdkUserGet?token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#APP参考文档管理列表
#userId_S查询文档List
    def Off_18(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:3000/v1/appsdk/appsdkDocumentList?token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#APP参考文档管理下载
#userId_S下载文档id
    def Off_19(self,userId_S,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:3000/v1/appsdk/appsdkDocumentDownload?token='+tokenData+'&id='+str(id)


        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#SDK配置列表
#userId_S查询appsdkVersionList
    def Off_20(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:3000/v1/appsdk/appsdkVersionList?token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#SDK配置文件下载
#userId_S下载sdkVersion
    def Off_21(self,userId_S,sdkVersion):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:3000/v1/appsdk/appsdkDownload?token='+tokenData+'&sdkversion='+sdkVersion

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')



if __name__ == '__main__':
    a = Official_01()
    a.Off_21()
