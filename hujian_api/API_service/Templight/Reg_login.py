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
#提供手机号或邮箱注册
#邮箱注册
    def Off_01(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/register'
        params = {'username':'huj@zhiyun-tech.com', 'password':'12345678'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#提供手机号或邮箱注册
#手机注册
    def Off_01_mobile(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/register'
        params = {'username':'+8613418483933', 'password':'12345678','vcode':'110110'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#提供手机号或邮箱登录
    def Off_02(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/login'
        params = {'username':'huj@zhiyun-tech.com', 'password':'12345678'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#用leancloud的token登录
    def Off_03(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/login_by_token'
        params = {'username':'huj@zhiyun-tech.com', 'token':'14daf4af07f2befd2fb108d66d302fb0'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#提供qq,weibo等第三方登录。
    def Off_04(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/sforeignlogin'
        params = {'platform':'qq', 'authData':{ "openid":"0395BA18A5CD6255E5BA185E7BEBA242","access_token":"12345678-SaMpLeTuo3m2avZxh5cjJmIrAfx4ZYyamdofM7IjU" }}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#游客登录
    def Off_05(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/login_by_visitor'
        params = {'sid':'9e09c0bb436eff3e5cd98f02baf2f08b'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#游客注册
    def Off_06(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/register'
        params = {'username':'youke', 'password':'8','vcode':'1','token':'abce'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#退出登录
    def Off_07(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/logout'
        params = {'token':'9e09c0bb436eff3e5cd98f02baf2f08b'}

        time.sleep(1)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#发送验证码
    def Off_08(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        data = Gt.Gt()
        listData = data.getGt()
        challenge = listData[0]
        validate = listData[1]
        seccode = listData[2]

        url = 'http://172.16.2.101:3000/v1/sendvcode'
        params = {'to':'+8613418483933','geetest_challenge':'challenge','geetest_validate':'validate','geetest_seccode':'jordan'}

        params['challenge'] = challenge
        params['validate'] = validate
        params['seccode'] = seccode

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#验证验证码
    def Off_04(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/shoppingcart/add'
        params = {'to':'9e09c0bb4', 'vcode':'123456'}

        time.sleep(1)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#解绑时验证验证码
    def Off_10(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/shoppingcart/add'
        params = {'to':'9e09c0bb436eff3e5cd98f02baf2f08b', 'vcode':'123456'}

        time.sleep(1)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#发送重置密码验证码
    def Off_11(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/requestPasswordReset'
        params = {'to':'huj@zhiyun-tech.com', 'lang':'en'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#重置密码
    def Off_12(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/resetpassword'
        params = {'username':'12345678901234567890123456789012', 'password':'87654321','vcode':'1'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#设置初始密码
    def Off_13(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/initpassword'
        params = {'token':'12345678901234567890123456789012', 'password':'87654321'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#绑定手机邮箱
    def Off_14(self,userId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/bind'
        params = {'token':'12345678901234567890123456789012', 'to':'huj@zhiyun-tech.com','vcode':'241195'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#解绑手机邮箱
    def Off_15(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/unbind_for_test'
        params = { 'username':'huj@zhiyun-tech.com'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#人机验证
    def Off_16(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/gt/register'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, 'true')
        Consts.RESULT_LIST.append('True')


#个人资料
    def Off_17(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/profile'
        params = {'userId':'1', 'token':'12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData
        params['userId'] = str(userId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#个人资料更新
    def Off_18(self,userId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/profile/update'
        params = {'token':'12345678901234567890123456789012', 'avatar':'https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/User_Avatar/17/2019-03-13-11:47:06.png',\
                  'nickname':'hujian','birthday':'2020-03-30','country':'中国','city':'深圳市','introduction':'tester','hobby':'test','sex':'1','adnotification':'0'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#个人当前信息切换
    def Off_19(self,userId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/user/update'
        params = {'token':'12345678901234567890123456789012', 'deviceType':'ios',\
                  'deviceId':'2309A4DD-2B97-4B85-8029-9D9CFB1647AD','lang':'en'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#登录成功绑定设备id
    def Off_20(self,userId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/bindLeanCloudInstallation'
        params = {'token':'12345678901234567890123456789012', 'type':'ios','deviceId':'2309A4DD-2B97-4B85-8029-9D9CFB1647AD'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#退出解绑设备
    def Off_21(self, userId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/unbindLeanCloudInstallation'
        params = {'token': '12345678901234567890123456789012', 'deviceId': '2309A4DD-2B97-4B85-8029-9D9CFB1647AD'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')



if __name__ == '__main__':
    a = Official_01()
    a.Off_02()
