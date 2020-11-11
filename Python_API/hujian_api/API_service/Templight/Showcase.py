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

        url = 'http://172.16.2.101:3001/v1/login'
        params = {'username': 'huj@zhiyun-tech.com', 'password': '12345678'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#账号获取权限
#userId_S获取其权限
    def Off_01(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/user/role'
        params = {'token':'12345678901234567890123456789012'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#用户信息查询
#userId_S查询其他用户信息
    def Off_02(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/user/query'
        params = {'token':'12345678901234567890123456789012'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#账号详细信息查询
#userId_S查询userId_M详细信息
    def Off_03(self,userId_S,userId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/user/info'
        params = { 'token':'12345678901234567890123456789012', 'id':1}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = userId_M

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#账号信息修改
#userId_S修改userId_M信息
    def Off_04(self,userId_S,userId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/user/update'
        params = {'token':'12345678901234567890123456789012', 'userId':1,'username':'huTester','nickname':'enEn','password':'12345678','departName':'软件研发部','permList':[{'permId':1,'permCode':'super'}]}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['userId'] = userId_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#账号新增
#userId_S新增其他账号
    def Off_05(self,userId_S):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/user/add'
        params = {'token':'12345678901234567890123456789012','username':'huJason1','nickname':'hjHJ','password':'12345678','departName':'软件研发部',\
                  'userId':'' , 'permList':[{"permId":1 ,"permCode":"super"},{"permId":2 ,"permCode":"perm_reseller_on"}]}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['userId'] = userId_S

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#账号状态禁用/启用
#userId_S禁用/启用userId_M
    def Off_06(self,userId_S,userId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/user/status_change'
        params = {'token': '12345678901234567890123456789012', 'userId': 1}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['userId'] = userId_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#账号删除
#userId_S删除userId_M
    def Off_07(self,userId_S,userId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/user/delete'
        params = {'token': '12345678901234567890123456789012', 'userId': 1}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['userId'] = userId_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#监控规则列表查询
#userId_S查询监控规则
    def Off_08(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/monitor/query'
        params = { 'token':'12345678901234567890123456789012'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#监控规则详细查询
#userId_S查询moId监控规则
    def Off_09(self,userId_S,moId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/monitor/search'
        params = {'token': '12345678901234567890123456789012', 'id':1}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = moId

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, 'ruleList')
        Consts.RESULT_LIST.append('True')


#新增监控规则
#userId_S新增监控规则
    def Off_10(self,userId_S):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/monitor/add'
        params = {'token': '12345678901234567890123456789012', 'name': '这是HU的监控规则111', 'agentList': '1,2,3', 'ruleList':'[{"rate":"semiannual","type":"prop","expression":"=","formula":"prop","quota":2232,"operator":"43","correction":10}]','ruleRelation': 'or','status': 1,'email':'huj@zhiyun-tech.com'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#修改监控规则
#userId修改id监控规则
    def Off_11(self,userId_S,ruleId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/monitor/update'
        params = {'token': '12345678901234567890123456789012','id':1, 'name': 'huH', 'agentList': '85414', 'ruleList':'[{"rate":"semiannual","type":"prop","expression":"=","formula":"prop","quota":2232,"operator":"43","correction":11}]','ruleRelation': 'or','status': 1,'email':'huj@zhiyun-tech.com'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = ruleId

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#删除监控规则
#userId_S删除监控规则ruleId
    def Off_12(self,userId_S,ruleId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/monitor/delete'
        params = {'token': '12345678901234567890123456789012', 'id': 1}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = ruleId

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#监控规则上下架
#userId_S上下架ruleId
    def Off_13(self,userId_S,ruleId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/monitor/up_down'
        params = {'token': '12345678901234567890123456789012', 'id': 1}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = ruleId

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#经销商权限查询
    def Off_14(self,userId_S,agentNo):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/seller/agent_perm_query'
        params = {'token': '12345678901234567890123456789012', 'agentNo': '8'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['agentNo'] = str(agentNo)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


###经销商权限编辑
#userList--赋予权限用户id列表	string 仅自己可见送空
    def Off_15(self,userId_S,agentNo):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/seller/agent_perm_update'
        params = {'token': '12345678901234567890123456789012', 'agentNo': '100','userList':[]}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['agentNo'] = str(agentNo)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#经销商销售统计
#dateType--日期分类 string stockoutAt/出库时间 createAt/激活时间
    def Off_16(self,userId_S,agentNo):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/reseller/query_sn'
        params = { 'token':'12345678901234567890123456789012','agentNo':'20','dateType':'stockoutAt'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['agentNo'] = str(agentNo)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#经销商总览
    def Off_17(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/seller/agent_overview_total'
        params = {'token': '12345678901234567890123456789012'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#经销商列表查询
    def Off_18(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/reseller/query'
        params = {'token': '12345678901234567890123456789012'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#IP白名单查询
    def Off_19(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/whitelist/query'
        params = {'token': '12345678901234567890123456789012'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#IP白名单更新
    def Off_20(self,userId_S,ipList):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/whitelist/update'
        params = {'token': '12134567890121345678901213456789012', 'ipList': '192.168.0.1,192.0.0.1'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['ipList'] = ipList

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#设备使用区域查询
    def Off_21(self,userId_S,SN):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/reseller/query_region'
        params = { 'token':'12345678901234567890123456789012','sn':'123456789012'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['sn'] = SN

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#展架登录
    def Off_22(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/login'
        params = {'username': '13418483933@139.com', 'password': '12345678'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#经销商的新增和编辑
#agentNo--有为编辑，无为新增
#isfixed 0可编辑 1禁止编辑
    def Off_23(self,userId_S,agentNo):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/seller/agent/update'
        params = {'token': '12345678901234567890123456789012','agentNo':'9111', 'name': '胡健经销商', 'country': '中国',\
                  'region': '广东省深圳市', 'address': '龙岗区星河World', 'phone': '075586862715', 'mail': '13418483933@139.com',\
                  'url':'https://www.baidu.com','isfixed': '0'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['agentNo'] = str(agentNo)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


    def Off_23_edit(self, userId_S, id, agentNo):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/seller/agent/update'

        params = {'token': '12345678901234567890123456789012', 'id':'85427','agentNo': '9121', 'name': '胡健经销商','country': '中国', \
                  'region': '广东省深圳市', 'address': '龙岗区星河World', 'phone': '075586862715', 'mail': '13418483933@139.com', \
                  'url': 'https://www.baidu.com/', 'isfixed': '0'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['agentNo'] = str(agentNo)
        params['id'] = str(id)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#经销商区域编辑
    def Off_24(self,userId_S,agentNo):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/reseller/update_reseller_region'
        params = {'token': '12345678901234567890123456789012', 'agentNo': '911', 'addList': '[{"region_code":"CHN","region_name":"中国"}]'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['agentNo'] = str(agentNo)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#经销商更新
#目标环境 prd(线上)/dev(本地)
    def Off_25(self,userId_S):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/reseller/sync_sn_data'
        params = {'token': '12345678901234567890123456789012', 'env':'dev'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#国家地址查询
#region_code--string 不传默认返回第一级地区, 否则返回对应的地区
    def Off_26(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/reseller/region_list'
        params = { 'token':'12345678901234567890123456789012'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#展架退出
    def Off_27(self,userId_S):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/logout'
        params = {'token': '12345678901234567890123456789012'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#展架更新账号密码
    def Off_28(self,userId_S):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/updatepassword'
        params = {'token': '12345678901234567890123456789012','username':'newnew','password':'12345678'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#展架--获取页面-主页相关的图
    def Off_29(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/sitelayout/index'
        params = { 'token':'12345678901234567890123456789012'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#产品列表
#productionType--string--mobile,pro,sport
    def Off_30(self,userId_S,productionType):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/production/list'
        params = { 'token':'12345678901234567890123456789012','productionType':'mobile'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['productionType'] = productionType

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#视频列表
#videoType--string--xuanchuan,wanfa,jiaocheng, 不传显示全部
    def Off_31(self,userId_S,productionId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/production/video_list'
        params = { 'token':'12345678901234567890123456789012','productionId':'1','lang':'zh_cn'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['productionId'] = str(productionId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#视频加点击量
    def Off_32(self,userId_S,videoId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/production/incr_video_click'
        params = {'token': '12345678901234567890123456789012', 'id': '1'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = str(videoId)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#广告新增/编辑
#id--string 有id为修改,没有为新增
#code--string index_banner,index_mobile,index_pro,index_sport
#sort--string	排序1,2,3...
#status--string	1正常,2,下架,0删除
    def Off_33(self,userId_S,code):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/sitelayout/update'
        params = {'token': '12345678901234567890123456789012', 'code': 'index_banner','image':'https://oss.zhiyun-tech.com/zyplaytest/course_edit/1/2019-08-01-16:29:32.png'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['code'] = code

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


    def Off_33_edit(self, userId_S, id, code):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/sitelayout/update'
        params = {'token': '12345678901234567890123456789012', 'id':'1','code': 'index_mobile',\
                  'image': 'https://oss.zhiyun-tech.com/zyplaytest/course_edit/1/2019-08-01-16:29:32.png'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['code'] = code
        params['id'] = id

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#用户产品编辑
    def Off_34(self,userId_S,productionId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/production/user_update'
        params = {'token': '12345678901234567890123456789012', 'productionId': '1','hide':'1','price':'99'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['productionId'] = str(productionId)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#展架页面
##code--string index_banner,index_mobile,index_pro,index_sport
    def Off_35(self,userId_S,code):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/sitelayout'
        params = {'token': '12345678901234567890123456789012', 'code': 'index_banner'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['code'] = code

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#产品新增编辑
#id--string--有id为修改,没有为新增
#productionType--string--产品类别 mobile,pro,sport
    def Off_36(self,userId_S,productionType):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/production/update'
        params = {'token': '12345678901234567890123456789012', 'productionType': 'mobile'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['productionType'] = productionType

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


    def Off_36_edit(self,userId_S,id,productionType):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/production/update'
        params = {'token': '12345678901234567890123456789012', 'id':'1','productionType': 'mobile'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['productionType'] = productionType
        params['id'] = str(id)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#视频新增/编辑
#id--string--有id为修改,没有为新增
#videoType--string--xuanchuan,wanfa,jiaocheng, 不传显示全部
    def Off_37(self,userId_S,productionId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/production/video_update'
        params = {'token': '12345678901234567890123456789012', 'productionId': '1','videoType':'wanfa',\
                  'image':'https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/zyplaytest/share/1/2018-07-31-16:12:54.png',\
                  'video':'https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/zyplaytest/share/1/2018-09-07-17:44:23.mp4',\
                  'title':'这是test','text':'yes','sort':'1'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['productionId'] = str(productionId)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


    def Off_37_edit(self,userId_S,productionId,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3001/v1/production/video_update'
        params = {'token': '12345678901234567890123456789012', 'id':'1','productionId': '1','videoType':'xuanchuan',\
                  'image':'https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/zyplaytest/share/1/2018-07-31-16:12:54.png',\
                  'video':'https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/zyplaytest/share/1/2018-09-07-17:44:23.mp4',\
                  'title':'这是test','text':'yes','sort':'1'}

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = str(id)
        params['productionId'] = str(productionId)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == '__main__':
    a = Official_01()
    a.Off_00('new','12345678')