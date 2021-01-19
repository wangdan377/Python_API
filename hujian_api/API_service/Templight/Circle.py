import pytest
import allure
import requests
import json
import time

from Templight import GetMysqlData
from Templight import GetMysqlDataSeller

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

class Official_01:
#添加圈子
#userId_S添加圈子
    def Off_01(self,userId_S):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/circle/addCircle'
        params = {'name':'这是胡健圈子吗?', 'avatar':'https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/User_Avatar/42/2017-10-25-10:49:54.jpg',\
                  'des':'tTest','longitude':'114.416512','latitude':'24.564150','tags':'测试','token':'12345678901234567890123456789012','address':'中国广东省深圳市'}

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


#圈子列表
#userId查圈子列表
    def Off_02(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)

        url = 'http://172.16.2.101:3000/v1/circle/circleList?searchType=2&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子地图
#userId圈子地图
    def Off_03(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)

        url = 'http://172.16.2.101:3000/v1/circle/circleMap?longitude=114.033806&latitude=22.534666&radius=50&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#标签列表
    def Off_04(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/circle/tagList'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子置顶
#circleId
    def Off_05(self,circleId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/circle/circleRecommend?id='+str(circleId)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#加入圈子
#userId_S加入circleId_M
    def Off_06(self,userId_S,circleId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/circleJoin?id='+str(circleId_M)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#加入圈子申请,审核列表
    def Off_07(self,userId_S,circleId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/circleJoinList?id='+str(circleId_M)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#加入圈子,审核
#userId_S
#type--0：拒绝 1：同意
#id-圈子用户中间表id
    def Off_08(self,userId_S,type,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/circleJoinCheck?id='+str(id)+'&type='+str(type)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子详情,基本信息
#userid--是否加入
    def Off_09(self,circleId,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)

        url = 'http://172.16.2.101:3000/v1/circle/circleQuery?id='+str(circleId)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子详情,动态（文章，视频，话题）
#userId--是否加入
    def Off_10(self,circleId,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)

        url = 'http://172.16.2.101:3000/v1/circle/circleQueryDetail?id='+str(circleId)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子成员
#userId--是否加入
    def Off_11(self,circleId,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/circle/circleMembers?id='+str(circleId)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子作品置顶
#id	string	作品id
#type	string	'article', 'video', 'topic'中的一个
#circleId	int	圈子id
#operateType	int	1:置顶2：取消置顶
    def Off_12(self,circleId, artId, artType, operateType):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/circle/workRecommend?circleId='+str(circleId)+'&id='+str(artId)+'&type='+artType+'&operateType='+str(operateType)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#发布文章
#userId在circleId发布文章
    def Off_13(self,userId_S,circleId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/circle/publishArticle'
        params = {'token':'12345678901234567890123456789012', 'cover':'http://f.youdao.com/?vendor=fanyi-new-bottom','title':'胡健圈子文章','content':'胡健test测试','circleId':1}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['circleId'] = circleId_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#发布视频-旧变新
#userId在circleId发布视频postId
    def Off_14(self,userId_S,circleId_M,postId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/circle/publishVideo'
        params = {'token': '12345678901234567890123456789012','des': '胡健圈子发布视频','url': 'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4',\
                  'circleId': '1','longitude': 114.033932,'latitude': 22.535047,'postId': '1','tags': '测试啊'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['circleId'] = str(circleId_M)
        params['postId'] = str(postId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#发布话题
#userId在circleId发布话题
    def Off_15(self,userId_S,circleId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/circle/publishTopic'
        params = {'token':'12345678901234567890123456789012', 'title':'这是圈子话题','des':'test','circleId':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['circleId'] = str(circleId_M)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#修改圈子资料(老版本)
    def Off_16(self,userId_S,circleId_M):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/circle/modifyCircleBasic'
        params = {'id':1, 'avatar':'https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/User_Avatar/43/2019-06-28-21:01:33.jpg',\
                  'name':'胡健名称','des':'这胡健是圈子','longitude':114.416512,'latitude':24.564150,'token':'12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['circleId'] = circleId_M

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#话题详情页
#userId--是否点赞/收藏
    def Off_17(self,topicId,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)

        url = 'http://172.16.2.101:3000/v1/circle/topicDetail?id='+str(topicId)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#话题--回复顶踩
#opType顶为1，踩为2
    def Off_18(self,userId_S,topicId_M,opType):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/updownTopicReply?id='+str(topicId_M)+'&token='+tokenData+'&type='+str(opType)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子话题发表看法
    def Off_19(self,userId_S,topicId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/releaseView?token='+tokenData+'&view=看法view&id='+str(topicId_M)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#删除圈子话题看法
#userId--viewId
    def Off_20(self,userId_S,replyId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/delView?token='+tokenData+'&id='+str(replyId_M)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子文章详情
#userId--是否点赞/收藏
    def Off_21(self,userId,artId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)

        url = 'http://172.16.2.101:3000/v1/circle/articleDetail?id='+str(artId)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子文章分享
    def Off_22(self,artId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/circle/articleShare?id='+str(artId)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子文章的点赞
#opType 1:点赞2：取消点赞
    def Off_23(self,userId_S,artId_M,opType):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/articleFav?id='+str(artId_M)+'&token='+tokenData+'&type='+str(opType)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子地图,点击圈子时显示的视频
#id--circleId/userId
#type 1：圈子 2：用户
#token--是否点赞/收藏
    def Off_24(self,id,type,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)

        url = 'http://172.16.2.101:3000/v1/circle/circleQueryVideo?id='+str(id)+'&type='+str(type)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子作品添加评论
#parentId，如果是第一级则传0
#type 1文章 2视频
    def Off_25(self,userId_S,parentId,workId_S,type):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/circle/circleAddComment'
        params = {'parentId':1, 'commentWords':'这是评论test','token':'12345678901234567890123456789012','workId':1,'type':1}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)
        params['token'] = tokenData

        params['parentId'] =parentId
        params['workId'] = workId_S
        params['type'] = type

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子作品删除评论
    def Off_26(self,userId_S,commentId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/circleDelComment?token='+tokenData+'&commentId='+str(commentId_M)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#查看圈子作品的父评论
#type--1文章 2视频
    def Off_27(self,userId_S,workId_M,type):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/circlePCommentQuery?workId='+str(workId_M)+'&token='+tokenData+'&type='+str(type)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#查看圈子作品的子评论（评论的回复）
#commentId--父评论id
    def Off_28(self,userId_S, commentId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/circleCCommentQuery?commentId='+str(commentId_M)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#退出圈子
#userId--客人
    def Off_29(self,userId_S,circleId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/quitCircle?token='+tokenData+'&circleId='+str(circleId_M)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#解散圈子
#userId--主人
    def Off_30(self,userId_S,circleId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/dissolveCircle?token='+tokenData+'&circleId='+str(circleId_M)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#踢出圈子
#userId--主人
#Id--圈子用户中间表id
    def Off_31(self,userId_S,id):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/beQuitedCircle?circleUserMidId='+str(id)+'&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#点赞-圈子话题的回复replyId
#type--1点赞2取消点赞
    def Off_32(self,userId_S,replyId_M,type):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/replyFav?token='+tokenData+'&replyId='+str(replyId_M)+'&type='+str(type)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子消息的通知列表
    def Off_33(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)

        url = 'http://172.16.2.101:3000/v1/circle/circleMsgList?token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#移动端作品删除
#workType作品类型'article', 'video', 'topic'
    def Off_34(self,userId_S,workId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/workDel?workId='+str(workId_M)+'&workType=article&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#移动端作品分享
#workType 作品类型'article', 'video', 'topic'
    def Off_35(self,userId_S,circleId_M,workId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/workShare?token='+tokenData+\
              '&circleId='+str(circleId_M)+'&workId='+str(workId_M)+'&workType=topic'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#用户位置修改
    def Off_36(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)

        url = 'http://172.16.2.101:3000/v1/circle/userLocate?longitude=112.435345&latitude=23.723486&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#根据commentId查找评论的详情
    def Off_37(self,commentId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/circle/getCircleComment?commentId='+str(commentId)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子文章添加收藏
#type--学院视频传school,圈子文章传circle_article
    def Off_38(self,userId_S,artId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/circleArticleFav?articleId='+str(artId_M)+'&type=circle_article&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子文章取消收藏
##type--学院视频传school,圈子文章传circle_article
    def Off_39(self,userId_S,artId_M):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId_S)

        url = 'http://172.16.2.101:3000/v1/circle/circleArticleUnfav?articleId='+str(artId_M)+'&type=circle_article&token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子文章收藏列表（整合入学院文章的收藏列表)
    def Off_40(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)

        url = 'http://172.16.2.101:3000/v1/circle/favList?token='+tokenData

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == '__main__':
    a = Official_01()
    a.Off_01()
