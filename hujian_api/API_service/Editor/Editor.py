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


class Editor_filter:
#登录
    def filter_00(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:3999/login'
        params = {'username':'admin@zhiyun-tech.com', 'password':'helloworld'}

        res = post_req.post_model_b(sessionX, url, params)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

        return sessionX

#新增
    def filter_000(self):
        sessionX = self.filter_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())
        rNumber = random.randint(1,100)

        url = 'http://47.99.180.185:3999/tpl/stickers/types/createOrUpdate'
        params = {"label": "013", "label_tw": "", "label_en": "", "sort": "1", "status": "1", "platfromIds": "3"}
        params['label'] = '013'+str(times)
        params['sort'] = str(rNumber)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#新增滤镜集
    def filter_01(self,status):
        sessionX = self.filter_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())
        rNumber = random.randint(1,100)

        url = 'http://47.99.180.185:3999/tpl/filters/groups/createOrUpdate'
        params = {'title':'胡健滤镜集合test', 'sort':'99', 'status':'1', 'thumb':'https://oss.zhiyun-tech.com/zyplaytest/templates/滤镜集合图a_20200410114645.png'}

        params['title'] = '胡健滤镜集合test'+str(times)
        params['sort'] = str(rNumber)
        params['status'] = status

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#编辑滤镜集
    def filter_02(self,id):
        sessionX = self.filter_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:3999/tpl/filters/groups/createOrUpdate'
        params = {'title':'胡健滤镜集合test', 'sort':'99', 'status':'1', 'thumb':'https://oss.zhiyun-tech.com/zyplaytest/templates/滤镜集合图a_20200410114645.png', 'id':'100'}
        params['id'] = id

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#删除滤镜集
    def filter_03(self,id):
        sessionX = self.filter_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:3999/tpl/filters/groups/del?id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#滤镜集里面新增滤镜
    def filter_04(self,status):
        sessionX = self.filter_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())
        rNumber = random.randint(1, 100)

        url = 'http://47.99.180.185:3999/tpl/filters/createOrUpdate'
        params ={'title':'胡健滤镜测试', 'title_tw':'胡健濾鏡測試', 'title_en':'myFilterTest', 'zy_play':'132', 'z_film':'132', 'sort':'66', 'status':'1', 'thumb':'https://oss.zhiyun-tech.com/zyplaytest/templates/滤镜集合图a_20200410143259.png','groupId':'75'}

        params['title'] = '胡健滤镜测试'+str(times)
        params['title_tw'] = '胡健濾鏡測試' + str(times)
        params['title_en'] = 'myFilterTest' + str(times)
        params['sort'] = str(rNumber)
        params['status'] = status

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#新增滤镜
    def filter_04(self,status):
        sessionX = self.filter_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())
        rNumber = random.randint(1, 100)

        url = 'http://47.99.180.185:3999/tpl/filters/createOrUpdate'
        params ={'title':'胡健滤镜测试', 'title_tw':'胡健濾鏡測試', 'title_en':'myFilterTest', 'zy_play':'132', 'z_film':'132', 'sort':'66', 'status':'1', 'thumb':'https://oss.zhiyun-tech.com/zyplaytest/templates/滤镜集合图a_20200410143259.png'}

        params['title'] = '胡健滤镜测试'+str(times)
        params['title_tw'] = '胡健濾鏡測試' + str(times)
        params['title_en'] = 'myFilterTest' + str(times)
        params['sort'] = str(rNumber)
        params['status'] = status

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#编辑滤镜
    def filter_05(self,id,status):
        sessionX = self.filter_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        times = int(time.time())
        rNumber = random.randint(1, 100)

        url = 'http://47.99.180.185:3999/tpl/filters/createOrUpdate'
        params ={'title':'胡健滤镜测试', 'title_tw':'胡健濾鏡測試', 'title_en':'myFilterTest', 'zy_play':'132', 'z_film':'132', 'sort':'66', 'status':'1', 'thumb':'https://oss.zhiyun-tech.com/zyplaytest/templates/滤镜集合图a_20200410143259.png', 'id':'99'}

        params['title'] = '胡健滤镜测试'+str(times)
        params['title_tw'] = '胡健濾鏡測試' + str(times)
        params['title_en'] = 'myFilterTest' + str(times)
        params['sort'] = str(rNumber)
        params['status'] = status
        params['id'] = id

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#删除滤镜
    def filter_06(self,id):
        sessionX = self.filter_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:3999/tpl/filters/delete?id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#查询滤镜列表
    def filter_07(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:2999/v1/filters/types/list'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#查询滤镜列表
    def filter_08(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:2999/v1/filters/list?page=1&pageSize=10'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')



if __name__ == '__main__':
    a = Editor_filter()
    for i in range(40):
        time.sleep(1)
        a.filter_000()

