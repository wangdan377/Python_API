import pytest
import allure
import requests
import json
import time

from Templight import  GetMysqlDataSeller

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

class Official_01:
#userId_S查看工单列表
#type--string 类型
#dealProcess--int 状态 1待指派2待确认3处理中4已关闭（待激活）
#workorderPriority--int	优先级
#startdate |date | 开始时间 | |enddate|	date|	结束时间
#start	int	起始时间
#limit	int	截止时间
#flag	int	1:正序2：倒序
#q	string	标题或指派人模糊搜索
#range	string	范围：null全部 tome 指派给我的 mycreate我创建的 quality完成质量
#token	string

    def Off_01(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workorder/workorderList?token='+tokenData+'&range='

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#userId_S新建工单
#frontWorkorderId	int	前置工单号
#backWorkorderId	int	后置工单号
#type	string	类型
#dispatcher	int	派送人id
#workorderPriority	int	优先级
#expectTime	date	期待完成时间
#title	string	标题
#des	string	描述
#attachments	string	附件 sourceUrl用英文逗号隔开
#remark	string	备注
#token	string
#feedbackFrom	string	反馈端：硬件设备，ZY Play app端、PC端、其他
#hardmodel	string	硬件型号
#firmwareversion |string | 固件版本 | |platform |string | 平台 | |phonemodel	string	手机型号
#phoneversion |string | 手机版本 | |appversion	string	app版本
#lang	string	语言
    def Off_02(self,userId_S):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        frontWorkorderId = 20
        backWorkorderId = 25
        type = '1'
        dispatcher = 100
        workorderPriority = 1
        expectTime = '2019-08-09'
        title = '标题'
        des = '描述'
        attachments = 'https://zyfeedback.oss-cn-shenzhen.aliyuncs.com/feedbacktest/upload/1/2019-05-13-11:56:52.png'
        remark = '备注'

        feedbackFrom = '硬件设备'
        hardmodel = 'smooth4'
        firmwareversion = '1.1'
        platform = 'app'
        phonemodel = ''
        phoneversion = ''
        appversion = ''
        lang = 'en'

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workorder/workorderCreate?token='+tokenData+'&frontWorkorderId='+str(frontWorkorderId)+\
              '&backWorkorderId='+str(backWorkorderId)+'&type='+type+'&dispatcher='+str(dispatcher)+'&workorderPriority='+str(workorderPriority)+ \
              '&expectTime=' +expectTime +'&title='+title+'&des='+des+'&attachments='+attachments+'&remark='+remark+'&feedbackFrom='+feedbackFrom+\
              '&hardmodel='+hardmodel+'&firmwareversion='+firmwareversion+'&platform='+platform+'&phonemodel='+phonemodel+ \
              '&phoneversion='+phoneversion+'&appversion='+appversion+'&lang='+lang

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单编辑回显
#userId_S查看工单号id
    def Off_03(self,userId_S,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workorder/workorderEdit?id='+str(id)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单编辑提交
#userId_S编辑工单id
    def Off_04(self,userId_S,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        frontWorkorderId = 19
        backWorkorderId = 27
        type = '1'
        dispatcher = 56
        workorderPriority = 1
        expectTime = '2019-08-09'
        title = '标题1'
        des = '描述1'
        attachments = 'https://zyfeedback.oss-cn-shenzhen.aliyuncs.com/feedbacktest/upload/1/2019-05-13-11:56:52.png'
        remark = '备注1'

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData


        url = 'http://172.16.2.101:4006/workorder/workorderEditSubmit?token='+tokenData+'&id='+str(id)+'&frontWorkorderId='+str(frontWorkorderId)+\
              '&backWorkorderId='+str(backWorkorderId)+'&type='+type+'&dispatcher='+str(dispatcher)+'&workorderPriority='+str(workorderPriority)+ \
              '&expectTime=' +expectTime +'&title='+title+'&des='+des+'&attachments='+attachments+'&remark='+remark

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单查询单列表
#userId_S查看列表
    def Off_05(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workorder/workorderSearchList?token='+tokenData


        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单撤销
#userId_S撤销工单id
    def Off_06(self,userId_S,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workorder/workorderCancel?id='+str(id)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#userId工单派发给dispatcher
#id	int	前置工单号
#dispatcher	int	派送人id
#workorderPriority	int	优先级
#expectTime	date	期待完成时间
#title	string	标题
#des	string	描述
#remark	string	备注
#token	string
    def Off_07(self,userId_S,dispatcher):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        id = 100
        workorderPriority = 1
        expectTime = '2020-04-29'
        title = '派发标题'
        des = '描述派发'
        remark = '备注派发'

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workorder/workorderDispatch?token='+tokenData+'&dispatcher='+str(dispatcher)+\
              '&id='+str(id)+'&workorderPriority='+str(workorderPriority)+'&expectTime='+expectTime+'&title='+title+\
              '&des='+des+'&remark='+remark

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单评分
#id	int	工单号
#score	int	分数
#scoreRemark	string	评分描述
#token	string
    def Off_08(self,userId,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        score = 100
        scoreRemark = '优秀'
        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workorder/workorderScore?token='+tokenData+'&id='+str(id)+'&score='+str(score)+'&scoreRemark='+scoreRemark


        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#拆分工单
#fatherWorkorderId
    def Off_09(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        fatherWorkorderId = 10
        frontWorkorderId = 20
        backWorkorderId = 25
        type = '1'
        dispatcher = 100
        workorderPriority = 1
        expectTime = '2019-08-09'
        title = '标题'
        des = '描述'
        attachments = 'https://zyfeedback.oss-cn-shenzhen.aliyuncs.com/feedbacktest/upload/1/2019-05-13-11:56:52.png'
        remark = '备注'

        feedbackFrom = '硬件设备'
        hardmodel = 'smooth4'
        firmwareversion = '1.1'
        platform = 'app'
        phonemodel = ''
        phoneversion = ''
        appversion = ''
        lang = 'en'

        url = 'http://172.16.2.101:4006/workorder/workorderSplit?token=' + tokenData +'&fatherWorkorderId='+fatherWorkorderId+ '&frontWorkorderId=' + str(frontWorkorderId) + \
              '&backWorkorderId=' + str(backWorkorderId) + '&type=' + type + '&dispatcher=' + str(dispatcher) + '&workorderPriority=' + str(workorderPriority) + \
              '&expectTime=' + expectTime + '&title=' + title + '&des=' + des + '&attachments=' + attachments + '&remark=' + remark + '&feedbackFrom=' + feedbackFrom + \
              '&hardmodel=' + hardmodel + '&firmwareversion=' + firmwareversion + '&platform=' + platform + '&phonemodel=' + phonemodel + \
              '&phoneversion=' + phoneversion + '&appversion=' + appversion + '&lang=' + lang


        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#修改工单状态
#id	int	工单号
#resolveCase	string	解决方案
#resolveVersion	string	解决版本
#expectTime	date	解决日期
#dispatcher	int	指派人
#chainAttachments	string	添加附加
#chainRemark	string	备注
#token	string
    def Off_10(self,userId_S,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        resolveCase = '设计原因'
        resolveVersion =  'C020010-1.1.4'
        expectTime = '2020-05-09'
        dispatcher = 67
        chainAttachments = 'https://zyfeedback.oss-cn-shenzhen.aliyuncs.com/feedbacktest/upload/1/2019-05-13-11:56:52.png'
        chainRemark = '这是备注'

        url = 'http://172.16.2.101:4006/workorder/workorderModify?token'+tokenData+'&id='+str(id)+ \
              '&resolveCase=' + resolveCase +'&resolveVersion='+resolveVersion+'&expectTime='+expectTime+\
              '&dispatcher='+str(dispatcher)+'&chainAttachments='+chainAttachments+'&chainRemark='+chainRemark

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#解决版本号列表
#userId_S查看解决版本号LIst
    def Off_11(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workorder/resolveVersionList?token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单列表导出
#type	string	类型
#dealProcess	int	状态 1待指派2待确认3处理中4已关闭（待激活）
#workorderPriority	int	优先级
#startdate |date | 开始时间 | |enddate	date	结束时间
#start	int
#limit	int	 //limit传入大值导出全部
#flag	int	1:正序2：倒序
#q	string	标题或指派人模糊搜索
#range	string	范围：null全部 tome 指派给我的 mycreate我创建的
#token	string
    def Off_12(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workorder/workorderListExcel?token='+tokenData+'&range=&flag=2&limit=1000'


        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#工单处理与不处理
#id	int	工单号
#token	string
#flag	string	1处理2不处理
    def Off_13(self,userId_S,id,flag):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workorder/workorderDealOrNot?token='+tokenData+'&id='+str(id)+'&flag='+flag


        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单激活
#userId_S激活工单id
    def Off_14(self,userId_S,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/workorder/workorderActive?token='+tokenData+'&id='+str(id)

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
