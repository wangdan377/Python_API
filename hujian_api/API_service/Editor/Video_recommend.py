import pytest
import allure
import requests
import json
import time
import random

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts


#视频推荐
class Editor_filter:
#推荐列表
    def filter_01(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/share/recommend/list?page=3&pageSize=1'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#喜欢作品列表
    def filter_02(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/share/post/like/list?token=80edf069d6844b0495745311a6778268&page=1&pageSize=4'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#课程（school）--合集--合集&课程接口
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/school/album/list?lang=zh_cn&dataType=set&page=1&pageSize=10'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#集合详情
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/school/album/info?lang=zh_cn&id=39&token=f05d77da036f7a1e4b374b1263018c57'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#课程收藏列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/school/post/favs?token=2cf5c1ba51ec71fc3d1f1a793d22e3fc&page=1&pageSize=10'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#分享活动-线下活动报名列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/share/activity/alllist?lang=zh_cn&page=1&pageSize=10'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#收藏课程
    def filter_03(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/school/post/fav'
        params = {}

        res = post_req.post_model_b(sessionX, url,params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#取消收藏课程
    def filter_03(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/school/post/unfav'
        params = {}

        res = post_req.post_model_b(sessionX, url,params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#课程和合集收藏列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/school/album/post/favs?token=2cf5c1ba51ec71fc3d1f1a793d22e3fc&page=1&pageSize=5&lang=zh_tw'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#基础-seo-拉取seo数据
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/site/pagedata?pageId=agency'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#类型列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/school/post/types?lang=zh_cn&code=school_type'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#记录观看位置
    def filter_03(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/video/record/create'
        params = {}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#通过ids获取视频观看记录
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/video/record/logs_by_ids?token=2cf5c1ba51ec71fc3d1f1a793d22e3fc&ids=20,19,37&tag=school'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#标签接口
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/codstr?lang=zh_cn&code=tag'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#记录观看位置
    def filter_03(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/site/add_feedback'
        params = {}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#资源列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/resources/list'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#获取资源详情
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/resources/info?id=149'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#资源下载上报
    def filter_03(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/resources/use_report'
        params = {}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#编辑器模板--模板--视频模板列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/templates/list'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#编辑器模板--模板--获取视频模板下载url
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/templates/download/url?id=1'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


# 编辑器模板--模板--获取模板详情
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/templates/info?id=25'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')



#保存用户视频配置
    def filter_03(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/templates/save'
        params = {}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

# 编辑器模板--模板--获取模板详情
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/templates/types/list'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#字体--字体列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/fonts/list?page=1&pageSize=2'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#字体--样式列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/styles/list?page=1&pageSize=10'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#贴纸--贴纸分类
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/stickers/types/list?page=1&pageSize=10'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#贴纸--贴纸列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/stickers/list?page=1&pageSize=10&typeId=27,5'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#音乐--专辑列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/music/albums'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#音乐--音乐列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/music/list?page=1&pageSize=10'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#音乐--热门音乐
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/music/hot/list?page=1&pageSize=10'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


# 滤镜--滤镜分类列表
def filter_03(self):
    sessionX = requests.session()
    get_req = Get.Get()
    ass = Assert.Assertions()

    times = int(time.time())

    url = 'http://47.99.180.185:2999/v1/filters/types/list'

    res = get_req.get_model_a(sessionX, url)
    print(res)

    resCode = res['code']
    resText = res['text']

    assert ass.assert_code(resCode, 200)
    assert ass.assert_in_text(resText, '成功')
    Consts.RESULT_LIST.append('True')


# 滤镜--滤镜列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/filters/list?page=1&pageSize=10'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


# 转场--转场列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/transitions/list?page=1&pageSize=10'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

    # 滤镜--滤镜列表
    def filter_03(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/filters/list?page=1&pageSize=10'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')



#登录
    def filter_03(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())

        url = 'http://47.99.180.185:2999/v1/login'
        params = {}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')



if __name__ == '__main__':
    a = Editor_filter()
    a.filter_01()


