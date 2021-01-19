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
#工单反馈--后台反馈列表
#start--int
#limit--int
#type--string	反馈类型（如工单反馈）
#dealProcess--string	进度（如待确认）
#workorderDispatcher--string	指派人
#startdate|date|起始时间 | + |enddate|date|截止时间
#q--string	模糊查询条件（对应title）
#flag--string	1：按id正序 0或者不传：按id倒序
#(userId_S)token--string	传入token,显示我创建的，否则查所有
    def Off_01(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        start_date = '2019-04-28'
        end_date = '2020-04-28'

        url = 'http://172.16.2.101:4006/back/feedback/feedbackListBack?start_date='+start_date+'&end_date='+end_date+'&dealProcess=1'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#后台反馈查看（管理员，创建人，非管理员）
#userId_S查看反馈id
    def Off_02(self,userId_S,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/back/feedback/feedbackQueryBack?token='+tokenData+'&id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#后台反馈撤销（创建人）
#userId_S撤销反馈id
    def Off_03(self,userId_S,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/back/feedback/feedbackWithdrawBack?id='+str(id)+'&token='+tokenData


        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#后台反馈拒绝（管理员)
#userId_S拒绝反馈id
#withdrawReason--拒绝原因
    def Off_04(self,userId_S,id,withdrawReason):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/back/feedback/feedbackRejectBack?id='+str(id)+'&token='+tokenData+'&withdrawReason='+withdrawReaso

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#后台反馈编辑（创建人）
    def Off_05(self,userId,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

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

        url = 'http://172.16.2.101:4006/back/feedback/feedbackEditBack?id=' + str(id) + '&token=' + tokenData + '&type=' + type + '&hardmodel=' + hardmodel + '&firmwareversion=' + firmwareversion + '&platform=' + platform + '&phonemodel=' + phonemodel + '&phoneversion=' + phoneversion + '&appversion=' + appversion + '&lang=' + lang + '&frequency=' + frequency + '&title=' + title + '&des=' + des + '&attachments=' + attachments + '&contact=' + contact + '&remark=' + remark


        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#生成工单
#id--int反馈id
#token--string
#type--string	类型
#expectTime--date	期待完成时间
#workorderPriority--string	优先级
#remark--string	备注
    def Off_06(self,userId_S,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        type = '1'
        expectTime = '2019-04-29'
        workorderPriority = '1'
        remark = '设计备注'

        url = 'http://172.16.2.101:4006/back/feedback/createWorkorderFromFeedback?id='+str(id)+'&token='+tokenData+'&type='+type+'&expectTime='+expectTime+'&workorderPriority='+workorderPriority+'&remark='+remark

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#后台新建反馈
#userId_S新建反馈
    def Off_07(self,userId_S):
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

        url = 'http://172.16.2.101:4006/back/feedback/feedbackCreateBack?token=' + tokenData + '&type=' + type + '&hardmodel=' + hardmodel + '&firmwareversion=' + firmwareversion + '&platform=' + platform + '&phonemodel=' + phonemodel + '&phoneversion=' + phoneversion + '&appversion=' + appversion + '&lang=' + lang + '&frequency=' + frequency + '&title=' + title + '&des=' + des + '&attachments=' + attachments + '&contact=' + contact + '&remark=' + remark

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#指派人下拉
    def Off_08(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4006/back/feedback/workorderDispatcherList'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#导出反馈
#start--int
#limit--int
#type--string	反馈类型（如工单反馈）
#dealProcess--string	进度（如待确认）
#workorderDispatcher--string	指派人
#startdate |date | 起始时间 | |enddate	date	截止时间
#q--string	模糊查询条件（对应title）
#flag--string	1：按id正序 0或者不传：按id倒序
#token--string	传入token,显示我创建的，否则查所有

    def Off_09(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        start_date = '2019-07-31'
        end_date = '2020-07-31'

        url = 'http://172.16.2.101:4006/back/feedback/feedbackListBackExcel?start_date='+start_date+'&end_date='+end_date+'&dealProcess=1'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#工单类型列表
    def Off_10(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:4006/back/feedback/workorderTypeList'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#后台激活反馈
#userId_S激活反馈id
    def Off_11(self,userId_S,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        data = GetMysqlDataSeller.GetMysqlDataSeller()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        url = 'http://172.16.2.101:4006/back/feedback/activeFeedbackBack?id='+str(id)+'&token='+tokenData

        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == '__main__':
    a = Official_01()
    a.Off_14()
