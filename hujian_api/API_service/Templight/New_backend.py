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
        params = {'username': 'huj@zhiyun-tech.com','password':'12345678'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#用户中心.数据总览
#product string	筛选平台（选填，1代表zyplay，2代表莱塔社，不填代表ALL）
    def Off_01(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/user/overview'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#用户中心.用户导出
#product  string 筛选平台（选填，1代表zyplay，2代表莱塔社，不填代表ALL）
#q	string	需要模糊查询字段（选填）
#status	 int  启用状态（选填，1代表启用，2代表禁用，不填代表ALL）
#startdate |string | 起始时间范围（选填） | enddate |string | 结束时间范围（选填）
#userIdList	string	用户id（选填，用逗号隔开的数字（或数组这个联调时可以商量着改）不填代表当前条件下所有用户）
    def Off_02(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/user/overAllUserListExport'

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#用户中心，VIP用户导出
#product  string	筛选平台（选填，1代表zyplay，2代表莱塔社，不填代表ALL）
#q	string	需要模糊查询字段（选填）
#status	 int  启用状态（选填，1代表启用，2代表禁用，不填代表ALL）
#startdate |string |起始时间范围（选填）  |enddate |	string	|结束时间范围（选填）
#userIdList	string	用户id（选填，用逗号隔开的数字（或数组这个联调时可以商量着改）不填代表当前条件下所有用户）
    def Off_03(self,userIdList):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/user/vipUserListExport'
        params = {'userIdList':'1,2,3'}

        params['userIdList'] = userIdList

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#账号设置-获取用户权限
    def Off_04(self,userId_S,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3002/v1/user/perm_get_by_id?token='+tokenData+'&id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#账号设置--账号新增用户
#username	string	用户名
#password	string	密码
#vcode	int	暂时不知道…
#role	string	角色id，逗号隔开
    def Off_05(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/user/add?username=hujian&password=12345678&role=1,2'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#账号设置.账号角色列表
#start	int	开始位置（非必填默认为0）
#limit	int	结束位置（非必填默认为0）
    def Off_06(self,start,limit):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/store/sku/detail'
        params = {'start': 0,'limit': 10}
        params['start'] = start
        params['limit'] = limit

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#账号设置.编辑账号userId_M权限permissionId
#userId	 int  用户id
#permissionId	string	编辑添加的用户权限id，用逗号隔开
    def Off_07(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/user/perm_edit'
        params = {'userId':1, 'permissionId':'1,2'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#账号设置.账号角色信息
#roleId	 int  角色id
    def Off_08(self,roleId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/user/getRoleById'
        params = {'roleId': 1}

        params['roleId'] = roleId

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#账号设置.账号添加角色
#rolekey  string	关键词
#rolename  string	角色名字
#permissionId	string	权限id，逗号隔开
#description	string	角色描述
    def Off_09(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/user/addRole'
        params = {'rolekey':'adminN', 'rolename':'次级管理员','permissionId':'1,2','description':'角色'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#账号设置.账号编辑角色
#roleId	int	角色id
#rolekey	string	关键词
#rolename	string	角色名字
#permissionId	string	权限id，逗号隔开
#description	string	角色描述
    def Off_10(self,roleId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/user/roleEdit'
        params = {'roleId':1,'rolekey':'zale', 'rolename':'炸了','permissionId':'1,2','description':'咋了'}

        params['roleId'] = roleId

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#内容中心.内容课程列表
#startdate |string |时间范围  |enddate |	string	| 时间范围
#start	int	开始位置
#limit	int	每页限制
#q	string	模糊查询
#type	int	原type
#status	int	原status
#ablbumId	int	合辑id
#platform	String	投放平台
#sort	string	排序方式
    def Off_11(self,ablbumId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/school/course/courseList'
        params = {'start': 0,'limit': 10,'status': 1,'q':'','ablbumId':1,'sort':'sortlikeCnt2'}

        params['ablbumId'] = ablbumId

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#内容中心.内容作品总览
#product int 产品1代表ZYPlay 2代表莱塔社
    def Off_12(self,product):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/school/overview'
        params = {'product': 1}
        params['product'] = product

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#内容中心.内容课程总览
#product  int	产品1代表ZYPlay 2代表莱塔社
    def Off_13(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/share/post/overview'
        params = {'product': 1}

        params['product'] = product

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#内容中心.内容热门课程
#start	int	开始位置（非必填默认为0）
#limit	int	结束位置（非必填默认为5）
#startdate |string |时间范围  |enddate|	string|	时间范围
    def Off_14(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/school/hotSchool'
        params = {'start': 0,'limit': 5}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#内容中心.内容热门分类
#start	int	开始位置（非必填默认为0）
#limit	int	结束位置（非必填默认为5）
#startdate |string |时间范围  |enddate|	string| 时间范围
    def Off_15(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/school/hotType'
        params = {'start': 0,'limit': 5}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#产品管理列表
#startdate |string |时间范围 |enddate | string| 时间范围
#start	int	开始位置
#limit	int	每页限制
#q	string	模糊查询
#type	int	type
#status	int	status
#sort	string	排序方式
    def Off_16(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/product/productList?q=1&status=0&type=testtype'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#产品编辑
#id	int	目标id 不传为新增
#name	string	产品名称
#type	string	产品类型
#platform	string	平台
#channel	string	渠道
#resourcesUrl	string	资源url
#iosUrl	string	iosurl
#mailUsers	string	通知人员邮箱或者id','隔开
#checkUsers	string	可查看人员id','隔开
#note	string	备注
    def Off_17(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/store/shoppingcart/add'
        params = {'name':'新增的', 'type':'1','platform':'1','channel':'1','resourcesUrl':'1','iosUrl':'1','mailUsers':'1','checkUsers':'1','note':'1'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#邮箱列表
#startdate |string |时间范围 |enddate |string | 时间范围
#start	int	开始位置
#limit	int	每页限制
#q	string	模糊查询
#code	string	code可不传
#status	int	status
#sort	string	排序方式
    def Off_18(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/noticeMail/mailget?code=version_mails'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#邮箱更新
#id	int	目标id 不传为新增
#name	string	产品名称
#code	string	默认是'version_mails'
#mail	string	邮箱地址
#status	int	状态0代表禁用，1代表开启
#id	int	id 若无代表新增
    def Off_19(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/store/shoppingcart/add'
        params = {'id':'1', 'name':'1','mail':'13418483933@139.com','status':0}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#商品详情
#startdate |string |时间范围  |enddate |	string|	时间范围
#start	int	开始位置
#limit	int	每页限制
#q	string	模糊查询
#code	string	code可不传
#status	 int  status
#sort	string	排序方式
#productId	int	产品id 产品下查询用
#platform	string	平台
    def Off_20(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/version/versionList?status=1&platform=android'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#版本更新
#id	int	目标id 不传为新增
#version	string	版本号
#product	int	产品id
#platform	string	类似原platform
#channel	string	类似原channel
#fileURL	string	文件url
#langs	string	简介语言多语言同时传
#notices	string	简介，多语言同时传
#releaseNotes	string	说明，多语言同时传
#forceUpdate	int	是否强制更新
#publishStatus	int	发布状态
#packageId	int	安装包id
#releaseDate	string	更新时间
    def Off_21(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        params ={'version': '0.0.2', 'productId': 1, 'platform': 'platform', 'channel': 'channel', \
                 'fileURL': 'fileURL','notices': 'notices','releaseNotes': 'releaseNotes',\
                 'forceUpdate': 1,'publishStatus': 1,'packageId': 3}

        url = 'http://172.16.2.101:3002/v1/version/versionUpdate'

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#硬件列表
#startdate |string |时间范围 |enddate | string|	时间范围
#start	int	开始位置
#limit	int	每页限制
#q	string	模糊查询
#sort	string	排序方式
#needFunction	string	用到的方法
    def Off_22(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/productproductParamsList?q=1'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#硬件更新
#id	int	目标id 不传为新增
#title	string	硬件名称
#functions	string	开放的功能','隔开
    def Off_23(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/product/productParamsUpdate'
        params = {'id':1, 'title':'测试', 'functions':'fun1'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#安装包列表
#startdate |string |时间范围  |enddate | string| 时间范围
#start	int	开始位置
#limit	int	每页限制
#q	string	模糊查询
#sort	string	排序方式
#product	string	对应产品
    def Off_24(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3002/v1/version/packageList?product=usb'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')



if __name__ == '__main__':
    a = Official_01()
    a.Off_00()
