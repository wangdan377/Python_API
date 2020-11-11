import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

class Official_01:
#工单权限分组管理--列表
#userId_S查看列表
    def Off_01(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workordergroup/workordergroupList?token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单权限--添加权限分组
#name--string	名称
#des--string	描述
#workorderpermissions--string	工单权限用英文逗号隔开如 1,2,3
#token--string
    def Off_02(self,userId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        name = '新分组110'
        des = '看看'
        workorderpermissions = '1,2'

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData


        url = 'http://172.16.2.101:4006/workordergroup/workordergroupAdd?name='+name+'&des='+des+'&workorderpermissions='+workorderpermissions+'&token='+tokenData

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单权限-编辑权限分组-回显
#id--int 分组id
#userId_S查看分组id
    def Off_03(self,userId_S,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workordergroup/workordergroupEdit?id='+str(id)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单权限-编辑权限分组-提交
#userId_S编辑分组id权限
#id--int	分组id
#name--string	名称
#des--string	描述
#workorderpermissions--string	工单权限用英文逗号隔开如 1,2,3
#token--string
    def Off_04(self,userId_S,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        name = '编辑权限010101'
        des = '看看描述'
        workorderpermissions = '1,2,3'

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workordergroup/workordergroupEditSubmit?name='+name+'&des='+des+'&workorderpermissions='+workorderpermissions+'&id='+str(id)+'&token='+tokenData

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单权限--编辑权限分组--删除
#userId_S删除分组id权限
    def Off_05(self,userId_S,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workordergroup/workordergroupDel?id='+str(id)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单权限权限管理-列表
#userId_S查看列表
    def Off_06(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workordergroup/workordergroupWithUsersList?token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单权限权限管理-查看用户
#userId_S查看用户
    def Off_07(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workordergroup/workordergroupWithUsersQuery?id=10&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单权限-权限用户-列表
#userId查看权限用户列表
    def Off_08(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workordergroup/workgroupUsers?token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#工单权限-权限-添加用户
#id--int	分组id
#users--string	工单权限用户 英文逗号隔开如 1,2,3
#token--string
#userId_S添加用户users到权限分组id
    def Off_09(self,userId_S,users_M,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workordergroup/workgroupAddUsers?users='+users_M+'&token='+tokenData+'&id='+str(id)

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单权限-权限-删除用户
#id--int	分组id
#users--string	工单权限用户 英文逗号隔开如 1,2,3
#token--string
#userId_S删除用户users出权限分组id
    def Off_10(self,userId_S,users_M,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workordergroup/workgroupDelUsers?token='+tokenData+'&users='+users_M+'&id'+str(id)

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单权限-权限列表
#userId_S查看权限列表
    def Off_11(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workordergroup/workgroupPermissions?token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单权限-权限-编辑用户
#id--int	分组id
#users--string	工单权限用户 英文逗号隔开如 1,2,3
#token--string
#userId_S编辑用户users到权限分组id
    def Off_12(self,userId_S,users_M,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workordergroup/workgroupEditUsers?token='+tokenData+'&users='+users+'&id='+str(id)

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#后台补充反馈
#id--int 反馈编号
#token--string
#extraDes--string	补充描述
#extraAttachments--string	补充附件
    def Off_13(self,userId_S,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        extraDes = '补充描述'
        extraAttachments = 'https://zyfeedback.oss-cn-shenzhen.aliyuncs.com/feedbacktest/upload/4/2019-04-29-11:02:25.jpg'

        url = 'http://172.16.2.101:4006/back/feedback/extraFeedbackBack?token='+tokenData+'&id='+str(id)+'&extraDes='+extraDes+'&extraAttachments='+extraAttachments

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == '__main__':
    a = Official_01()
    a.Off_13()
