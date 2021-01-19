import pytest
import allure
import requests
import json
import time

from Templight import GetMysqlData
from Templight import GetMysqlDataSeller

from Common.Hash import my_md5

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


class Official_01:
#创建分享
#userId_S创建postId
    def Off_01(self,userId_S):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/post/create'
        params = {'token':'12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#发布分享
#前置条件：先创建postId，userId_S发布share_post
    def Off_02(self,userId_S):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/post/publish'
        params = {'token':'12345678901234567890123456789012', 'postId':'6664', 'sourceUrls':[], 'title':'这是一个胡健测试','mail':'13418483933@139.com','des':'test','tags':'风景美如画','platform':'web'}
        params['sourceUrls'] = ['','https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/zyplay/share/103640/6641/2020-03-06-11:56:50.mp4']

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        postIdData = data.getPostId_none(userId_S)
        params['postId'] = str(postIdData)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#分享详情
    def Off_03(self,userId,postId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/post/detail'
        params = {'postId': '1234','token':'12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        params['postId'] = str(postId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#删除分享
#userId_S删除发布的postId_M
    def Off_04(self,userId_S,postId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/post/del'
        params = {'token':'12345678901234567890123456789012', 'id':'1234'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = str(postId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#用户分享列表
    def Off_05(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/get_user_posts'
        params = {'userId': '1'}
        params['userId'] = str(userId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#最新分享列表
#userId--是否已点赞/收藏
    def Off_06(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/post/newest'
        params = {'token': '12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#热门分享列表
#userId--是否已点赞/收藏
    def Off_07(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/post/recommend'
        params = {'token': '12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#分享默认标签
    def Off_08(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/codstr'
        params = {'code':'tag'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#消息阅读+1
    def Off_09(self,userId_S,notifyId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/push/add_read_count'
        params = {'token':'12345678901234567890123456789012', 'notifyId':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['notifyId'] = str(notifyId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#添加评论
#userId_S给postId_M添加comment
    def Off_10(self,userId_S,postId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/comment/add'
        params = {'token':'12345678901234567890123456789012', 'postId':'1234','content':'这是评论test'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['postId'] = str(postId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#删除评论
#userId_S删除--给postId_M添加的comment
    def Off_11(self,userId_S,commentId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/comment/del'
        params = {'token':'12345678901234567890123456789012', 'id':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = str(commentId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#评论列表
    def Off_12(self,postId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/comments'
        params = {'postId': '1'}

        params['postId'] = str(postId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#关注
#userId_S关注userId_M
    def Off_13(self,userId_S, userId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/user/follow'
        params = {'token':'12345678901234567890123456789012', 'to':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = str(userId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#取消关注
#userId_S取消关注userId_M
    def Off_14(self,userId_S,userId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/user/unfollow'
        params = {'token':'12345678901234567890123456789012', 'to':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['to'] = str(userId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#用户粉丝列表
    def Off_15(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/user/get_followers'
        params = {'userId': '1'}
        params['userId'] = str(userId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#用户关注列表
    def Off_16(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/user/get_follows'
        params = {'userId': '1'}
        params['userId'] = str(userId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#点赞
#userId_S点赞postId_M
    def Off_17(self,userId_S,postId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/post/like'
        params = {'token':'12345678901234567890123456789012', 'postId':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['postId'] = str(postId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#取消点赞
#userId_S取消点赞postId_M
    def Off_18(self,userId_S,postId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/post/unlike'
        params = {'token':'12345678901234567890123456789012', 'postId':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['postId'] = str(postId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#点赞用户列表
#userId--是否已点赞
    def Off_19(self,userId,postId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/post/likes'
        params = {'postId': '1','token':'12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        params['postId'] = str(postId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#收藏
#userId_S收藏postId_M
    def Off_20(self,userId_S,postId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/post/fav'
        params = {'token':'12345678901234567890123456789012', 'postId':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['postId'] = str(postId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#取消收藏
#userId_S取消收藏postId_M
    def Off_21(self,userId_S,postId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/post/unfav'
        params = {'token':'12345678901234567890123456789012', 'postId':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['postId'] = str(postId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#增加分享数
    def Off_22(self,postId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/post/incrshare'
        params = {'postId':'1'}
        params['postId'] = str(postId)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#最新活动列表
    def Off_23(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/activity/newest'
        params = {'showtype': 'all'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#进行中活动列表
    def Off_24(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/activity/ongoing'
        params = {'showtype': 'all'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#已结束活动列表
    def Off_25(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/activity/finished'
        params = {'showtype': 'all'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#活动详情
    def Off_26(self,actId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/activity/detail'
        params = {'id': '1'}
        params['id'] = str(actId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#活动作品列表
#userId--是否已点赞/已收藏
    def Off_27(self,userId,actId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/activity/list'
        params = {'id': '1','token':'12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        params['id'] = str(actId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#主题详情
    def Off_28(self,themeId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/cat/detail'
        params = {'id': '1'}
        params['id'] = str(themeId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#主题作品列表
#userId--是否已点赞/已收藏
    def Off_29(self,userId,themeId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/cat/list'
        params = {'id': '1','token':'12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        params['id'] = str(themeId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#获取页面布局相关的图
    def Off_30(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/sitelayout'
        params = {'code': 'share_banner'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#获取页面-分享主页share_post相关的图
    def Off_31(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/page/share_mainpage'
        params = {'lang': 'zh_ cn'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#增加页面点击数
#postId分享页面
    def Off_32(self,postId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/incr_sitelayout_click'
        params = {'id': '1'}
        params['id'] = str(postId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#举报
    def Off_33(self,userId_S,targetId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/report_spam'
        params = {'targetId':'1', 'targetType':'share_post','reasonType':'违反法律','reason':'违规啦','userId':'1'}

        params['targetId'] = targetId
        params['userId'] = userId_S

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#拿阿里云oss token
    def Off_34(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/getAliyunOSSToken'
        params = {'token': '12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#阿里云oss_by_userId
    def Off_35(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/getAliyunOSSTokenByUserId'
        params = {'userId': '1'}
        params['userId'] = str(userId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#app最新版本查询
#检查平台/应用商店/软件的最新版本
    def Off_36(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/app/queryLatestVersionInfo_v2'
        params = {'platform': 'iOS','channel':'AppStore','env':'test'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#app强制升级查询
    def Off_37(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/app/checkForceUpdate_v2'
        params = {'platform': 'iOS','channel':'AppStore','version':'1.0.0','env':'test'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#app固件升级查询
    def Off_38(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/version_query'
        params = {'code':1329, 'platform': 'firmware','version':'1.1.1','lang':'zh_cn','env':'test'}

        #params = {'code':1329, 'platform': 'firmware','module':'{"m0":"1.00", "m1":"1.82"}','lang':'zh_cn','env':'test' }

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#app固件升级查询v2
    def Off_39(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/firmware_update'
        params = {'code': 1329,'version':'1.92','lang':'zh_cn','env':'test'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#app闪屏广告
    def Off_40(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/app/splash_ad'
        params = {'lang': 'zh_cn'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#app产品列表图
    def Off_41(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/app/production'
        params = {'lang': 'zh_cn','layoutCode':'v2'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#产品设备参数
    def Off_42(self,code):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/product_params'
        params = {'code': 'C020014C'}
        params['code'] = code

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#视频截图
#userId_S视频截图
    def Off_43(self,userId_S):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/screenshot'
        params = {'token':'12345678901234567890123456789012', 'url':'https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/zyplay/share/103640/6641/2020-03-06-11:56:50.mp4'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#添加回复
#userId_S给comment添加reply
    def Off_44(self,userId_S,commentId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/reply/add'
        params = {'token':'12345678901234567890123456789012', 'commentId':1, 'content':'testSth'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['commentId'] = commentId_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#删除回复
#userId_S删除他的reply
    def Off_45(self,userId_S,replyId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/reply/del'
        params = {'token':'12345678901234567890123456789012', 'id':1}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = replyId_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#回复列表
#commentId--reply列表
    def Off_46(self,commentId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/replys'
        params = {'commentId': 1}
        params['commentId'] = commentId

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#主题精选
    def Off_47(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/cat/recommend'
        params = {'postLimit': '5'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#主题热门
#userId--是否已点赞/已收藏
    def Off_48(self,userId,themeId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/cat/hottest'
        params = {'id': '1','token':'012345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        params['id'] = str(themeId)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#用户关注人的作品列表
#userId--是否已点赞/已收藏
    def Off_49(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/user/myfollows'
        params = {'token': '12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#推荐关注人
#userId--是否已关注推荐人
    def Off_50(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/user/recommend_follows'
        params = {'token': '12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#搜索
    def Off_51(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/search'
        params = {'q': '90654'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#未读消息数
#userId用户未读消息数
    def Off_52(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/notify/unread_count'
        params = {'token': '12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#消息列表
    def Off_53(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/notify/list'
        params = {'token':'12345678901234567890123456789012','type': 'notice'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#设置已读
    def Off_54(self,userId_S,notifyId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/notify/set_read'
        params = {'token':'12345678901234567890123456789012', 'id':'1234'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = str(notifyId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#设置类型已读
    def Off_55(self,userId_S,notifyId_type_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/notify/set_read_by_type'
        params = {'token':'12345678901234567890123456789012', 'type':'notice'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['type'] = notifyId_type_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#删除消息
    def Off_56(self,userId_S,notifyId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/notify/del'
        params = {'token':'12345678901234567890123456789012', 'id':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['id'] = str(notifyId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#发送私信
    def Off_57(self,userId_S,userId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/notify/sendmessage'
        params = {'token':'12345678901234567890123456789012', 'to':1, 'content':'helloTest'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['to'] = userId_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#群发私信
#userId_to_list为'1,2,3,4'格式
    def Off_58(self,userId_S,userId_list_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/notify/sendmessagebatch'
        params = {'token':'12345678901234567890123456789012', 'to_list':'1,2','content':'helloListTest'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['to_list'] = userId_list_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#聊天私信列表
#2个userId之间的私信列表
    def Off_59(self,userId_from,userId_to):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/notify/message_list'
        params = {'token': '12345678901234567890123456789012','to':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_from)
        params['token'] = tokenData

        params['to'] = str(userId_to)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#私信对话列表
#userId的私信对话列表
    def Off_60(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/notify/message_chat_list'
        params = {'token': '12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#系统通知列表
    def Off_61(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/notify/notice_list'
        params = {'lang': 'zh_cn'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#设置对话已读
    def Off_62(self,userId_from,userId_to):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/notify/set_read_by_chat'
        params = {'token':'12345678901234567890123456789012', 'to':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_from)
        params['token'] = tokenData

        params['to'] = str(userId_to)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#删除对话
    def Off_63(self,userId_from,userId_to):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/notify/del_by_chat'
        params = {'token':'12345678901234567890123456789012', 'to':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_from)
        params['token'] = tokenData

        params['to'] = str(userId_to)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#根据tag获取作品列表
#newest
    def Off_64_01(self,tag):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/tag/newest_posts'
        params = {'tag': '自然','lang':'zh_cn'}
        params['tag'] = tag

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#根据tag获取作品列表
#hot
    def Off_64_02(self,tag):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/tag/hot_posts'
        params = {'tag': '自然','lang':'zh_cn'}
        params['tag'] = tag

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#tag详情
    def Off_64_03(self,tag):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/tag/detail'
        params = {'tag': '自然','lang':'zh_cn'}
        params['tag'] = tag

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#扫码登录
#sid为二维码
    def Off_65(self,userId,sid):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/site/smlogin'
        params = {'token':'12345678901234567890123456789012', 'sid':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        params['sid'] = sid

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#扫码登录查询
#sid为二维码
    def Off_66(self,sid):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/site/query_smlogin'
        params = {'sid': '1'}
        params['sid'] = 's%3ApfNGd4VaCRn3qJZCoD6bRBapREXxje-t.v%2BXo09%2FgroqZQhiylXO%2BkdE7AbREiZs322Bq%2FU21eVU'

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#手机设备支持查询
    def Off_67(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/app/check_mobile_support'
        params = {'retailBranding': 'Apple','model':'iPhone8,1'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#上传手机设备信息
    def Off_68(self,userId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/app/upload_model_feedback'
        params = {'userId':'1', 'retailBranding': 'HUAWEI','model':'LIO-AL00'}

        params['userId'] = str(userId)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#上传app产品设备使用记录
    def Off_69(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/app/add_app_production_info'
        params = {'userid':103665, 'phoneid':'0FD8CEE0-879A-4FA7-A1BE-BD907766D6E0', \
                  'model':'Weebill Lab', 'deviceid':'WEEBILL LAB_3AE7', \
                  'longitude':'114.027585', 'latitude':'22.526951', 'serial_num':'70f09f055000023',\
                  'camera':'Canon', 'bts':'2020-02-07 02:31:50', 'ets':'2020-03-07 02:36:52'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#上传作品发布失败信息
    def Off_70(self,userId,postId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/add_app_share_post_publish_log'
        params = {'userId':1, 'postId':1, 'phoneid':'0FD8CEE0-879A-4FA7-A1BE-BD907766D6E0', 'version':'1.1.1',\
                  'reason':'错了', 'reasonCode':'compress_failed', \
                  'sourceUrl1':'https://oss.zhiyun-tech.com/zyplay/share/39/96/02017-08-31-14:29:40.jpg',\
                  'sourceUrl2':'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4',  'failAt':'2018-02-07 02:31:50'}
        params['userId'] = userId
        params['postId'] = postId

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#上传app版本信息
    def Off_71(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/add_app_startup_info_light'
        params = {'userId':103665, 'lang':'zh_cn', 'phoneid':'0FD8CEE0-879A-4FA7-A1BE-BD907766D6E0', 'os':'iOS',\
                  'osVersion':'10.3.1', 'appId':'com.zhiyun.zyplay', 'appVersion':'v6.1.1', 'startupAt':'2018-02-07 02:31:50'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#所有设备型号查询
    def Off_72(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/app/get_all_model'
        params = {'page': '1','pageSize':'20'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#按品牌查询设备型号
    def Off_73(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/app/get_model_by_brand'
        params = {'retailBranding': 'Apple'}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#黑名单-新增
#userId_M被加入黑名单
    def Off_74(self,userId_S,userId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/user/block/add'
        params = {'token':'12345678901234567890123456789012', 'to':1}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['to'] = userId_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#黑名单-删除
#userId_M被取消黑名单
    def Off_75(self,userId_S,userId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/user/block/del'
        params = {'token':'12345678901234567890123456789012', 'to':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['to'] = str(userId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#黑名单-列表查询
    def Off_76(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/user/block/query'
        params = {'token': '12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#黑名单-单个查询
#userId_M被查询
    def Off_77(self,userId_S,userId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/user/block/query_single'
        params = {'token': '12345678901234567890123456789012','to':1}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['to'] = userId_M

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#后台--反馈列表
#tpye = 'all', 'advice', 'other', 'feedback'中一个
    def Off_78(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/feedback/feedbackList?limit=15&start=0&type=all'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#后台反馈--删除
#id为反馈id
    def Off_79(self,feedbackId):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/feedback/feedbackDel?id='+str(feedbackId)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#后台反馈--查看
    def Off_80(self,feedbackId):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/feedback/feedbackQuery?id='+str(feedbackId)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#后台反馈--进行回复
#recieverId--反馈人ID
    def Off_81(self,recieverId,feedbackId):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/feedback/feedbackAnswer'

        params = {'recieverId':1, 'feedbackId':1, 'answerContent':'回复一下'}
        params['recieverId'] = recieverId
        params['feedbackId'] = feedbackId

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


###审核-用户所有作品
    def Off_82(self,userId_S,userId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/share/get_user_posts?token='+tokenData+'&userId='+str(userId_M)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


###审核-用户待审核头像
    def Off_83(self,userId_S,userId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/profile/approval?token='+tokenData+'&userId='+str(userId_M)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


###审核-用户所有文章
    def Off_84(self,userId_S,userId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/articleList?token='+tokenData+'&userId='+str(userId_M)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


###审核-创建的所有圈子
    def Off_85(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/appeal'
        params = {'token':'12345678901234567890123456789012', 'classify':'1','approvalId':'1','appealReason':'求饶'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


###审核-审核/惩罚通知--消息列表
    def Off_86(self,userId_S):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/notify/list'
        params = {'token': '12345678901234567890123456789012','type':'personal'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


###审核-创建申诉
    def Off_87(self,userId_S,approvalId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/appeal'
        params = {'userId':'1', 'classify':1,'appealReason':'求饶please','approvalId':123,\
                  'sourceUrls':'https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/zyplay/share/103640/6641/02020-03-06-11:56:48.jpg'}
        params['userId'] = str(userId_S)
        params['approvalId'] = approvalId_M

        #params = {'userId': '1', 'classify': 2, 'appealReason': '求饶please', 'punishId': 1,'sourceUrls': 'https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/zyplay/share/103640/6641/02020-03-06-11:56:48.jpg'}
        #params['userId'] = str(userId_S)
        #params['punishId'] = punishId_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


###审核-获取单条申诉
    def Off_88(self,userId_S,appealId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/appeal?userId='+str(userId)+'&appealId='+str(appealId)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


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



if __name__ == '__main__':
    a = Official_01()
    a.Off_00()


