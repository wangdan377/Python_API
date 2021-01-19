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
#后台圈子列表
#status--int 圈子状态 0删除1正常2未审核3审核不通过
#q--string 关键字（圈子名称或者圈子id）
#rankType--int 1：活跃值升序 2：活跃值降序
    def Off_01(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/circleList?rankType=2'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子-审核,封禁,解禁
#type--int	1:通过2：拒绝3：封禁（删除）4：解禁
    def Off_02(self,circleId,type):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/circleStatusModify?circleId='+str(circleId)+'&type='+str(type)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子封禁详情
    def Off_03(self,circleId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/forbidEdit?circleId='+str(circleId)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子封禁提交
    def Off_04(self,circleId):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/forbidSubmit'
        params = {'circleId': 1 , 'forbiddenReason':'胡健封了封了','forbiddenDetails':'就是要封','forbiddenPeriodStart':'2018-08-30 14:02:02','forbiddenPeriodEnd':'2020-08-30 14:02:02'}

        params['circleId'] = circleId

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#封禁圈子列表
    def Off_05(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/forbiddenCircleList?limit=10&start=0'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子查看
    def Off_06(self,circleId):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/circleQuery?circleId='+str(circleId)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子作品
    def Off_07(self,circleId):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/circleWorks?circleId='+str(circleId)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#作品置顶
#workId--int 作品id
#workType--int 作品类型'article', 'video', 'topic'
#type--int	1置顶2取消置顶
#circleId--int 当前圈子id
    def Off_08(self,circleId,workId):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/recommendWork?workId='+str(workId)+'&workType=video&type=1&circleId='+str(circleId)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#作品删除
    def Off_09(self,workId):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/delWork?workId='+str(workId)+'&workType=article'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#作品查看
    def Off_10(self,workId):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/queryWork?workId='+str(workId)+'&workType=topic'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, 'basicInfo')
        Consts.RESULT_LIST.append('True')


#圈子成员列表
    def Off_11(self,circleId):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/circleMemberList?circleId='+str(circleId)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#授予圈主
    def Off_12(self,circleId,userId):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/switchCirclePublisher?circleId='+str(circleId)+'&userId='+str(userId)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#后台踢出圈子
#id--圈子用户中间表id
    def Off_13(self,userId_M,circleId,id):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/tickoutCircle?id='+str(id)+'&circleId='+str(circleId)+'&userId='+str(userId_M)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#后台发布文章
    def Off_14(self,userId_S, circleId_M):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/publishArticle'
        params = {'token':'12345678901234567890123456789012', 'cover':'https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/User_Avatar/43/2019-06-28-21:01:33.jpg',\
                  'title':'这是后台文章','content':'低头思故乡','circleId':1}

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


###后台发布视频--禁掉
    def Off_15_01(self,userId_S,circleId_M,postId_M):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/circle/publishVideo'
        params = {'token':'12345678901234567890123456789012', 'des':'这是后台发布视频','url':'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4',\
                  'circleId':'1','longitude':114.416512,'latitude':24.564150,'postId':'1','tags':'风景美如画'}

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


#后台发布视频
    def Off_15(self,userId_S,circleId_M,postId_M):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/share/post/publish'
        params = {'token': '12345678901234567890123456789012', 'postId': '6668', 'sourceUrls': [], 'title': '这是一个胡健测试',
                  'mail': '13418483933@139.com', 'des': 'test', 'tags': '风景美如画', 'platform': 'web','circleId':524}
        params['sourceUrls'] = ['','https://zhiyundata.oss-cn-shenzhen.aliyuncs.com/zyplay/share/103640/6641/2020-03-06-11:56:50.mp4']

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


#后台发布话题
    def Off_16(self,userId_S,circleId_M):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/publishTopic'
        params = {'token':'12345678901234567890123456789012', 'title':'这是后台发布话题', 'des':'tTest', 'circleId':'1'}

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


#热门tag列表
    def Off_17(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/hotCirlceTagList'
        params = {'status':1}

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#热门tag上下架
#type--string 1:上架2：下架
#tagId--int	标签id
    def Off_18(self,tagId,type):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/upDownCircleTag'
        params = {'type': '1','tagId':1}

        params['type'] = str(type)
        params['tagId'] = tagId

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#添加圈子热门tag
    def Off_19(self):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/addCircleHotTag'
        params = {'lang': 'en','tagname': '加上这个','scope': '北京,上海,广州,深圳','start': '2018-08-30 14:02:02','end': '2020-08-30 14:02:02'}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子热门tag编辑回显
    def Off_20(self,tagId):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/queryCircleHotTag?tagId='+str(tagId)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#圈子热门tag编辑
#status--int	0下架1上架
    def Off_21(self,tagId):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/modifyCircleHotTag'
        params = {'tagId':1,'lang': 'en','tagname': '改一改','scope': '深圳','start': '2018-10-19 00:00:00','end': '2020-10-19 00:00:00','status':0}

        params['tagId'] = tagId

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#推荐和官方圈子列表
#start	int	标签id
#limit	int	语言
#classes	string	选择类型1活动2主题3作品4圈子5用户
#q	string
    def Off_22(self,classes):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/mapCircleList?classes='+str(classes)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#推荐和官方圈子列表搜索
#classes--string	选择类型1活动2主题3作品4圈子5用户
#q--string
    def Off_23(self,classes,q):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/mapSearch?classes='+str(classes)+'&q='+str(6667)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '6667')
        Consts.RESULT_LIST.append('True')


#后台圈子修改
#id--int名称
#classes--string类型1活动2主题3作品4圈子5用户
#type--int位置类型：1官方2推荐3真实
#longitude--float	地理位置：经度
#latitude--float	地理位置：纬度
#upStartDateTime datetime上架时间：起始（永久为'1-1-1'）
#upEndDateTime	datetime	上架时间：截止（永久为'9999-1-1'）
    def Off_24(self,circleId,classes):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/mapModify'
        params = {'id':1,'classes': '4','type': 1,'longitude': 114.036251,'latitude': 22.53829,\
                  'upStartDateTime': '0001-01-01 00:00:00','upEndDateTime':'9999-01-01 00:00:00'}

        params['id'] = circleId
        params['classes'] = str(classes)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#后台圈子编辑回显
    def Off_25(self,circleId):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/mapEdit?id='+str(circleId)+'&classes=4'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, 'id')
        Consts.RESULT_LIST.append('True')


#后台圈子删除
    def Off_26(self,circleId):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/mapDel?id='+str(circleId)+'&classes=4'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


###地图编码-接口禁掉
#type--int 1正编码2逆编码
#address--string地址如（北京市海淀区上地十街10号）type为1时传入
#longitude	float	经度type为2时传入
#latitude	float	纬度type为2时传入
    def Off_27(self,code):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/circle/mapCode?type='+str(code)+'&address=北京市海淀区上地十街10号'

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
        params = {'username':'huj@zhiyun-tech.com', 'password':'12345678'}

        res = post_req.post_model_b(sessionX, url, params)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

        return sessionX




if __name__ == '__main__':
    a = Official_01()
    a.Off_14()
