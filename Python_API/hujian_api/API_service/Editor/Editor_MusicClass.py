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

        class_011_0 = {"name":"","name_tw":"","name_en":"",
                       "cover_url":"https://oss.zhiyun-tech.com/zyplaytest/templates/47/2020-04-13-13:43:11.png","status":""}
        class_011_1 = {"name":"","name_tw":"","name_en":"",
                       "cover_url":"https://oss.zhiyun-tech.com/zyplaytest/templates/47/2020-04-13-13:43:11.png","status":""}
        class_101_0 = {"name":"","name_tw":"","name_en":"",
                       "cover_url":"https://oss.zhiyun-tech.com/zyplaytest/templates/47/2020-04-13-13:43:11.png","status":""}

        class_101_1 = {"name":"","name_tw":"","name_en":"",
                       "cover_url":"https://oss.zhiyun-tech.com/zyplaytest/templates/47/2020-04-13-13:43:11.png","status":""}
        class_110_0 = {"name":"","name_tw":"","name_en":"",
                       "cover_url":"https://oss.zhiyun-tech.com/zyplaytest/templates/47/2020-04-13-13:43:11.png","status":""}
        class_110_1 = {"name":"","name_tw":"","name_en":"",
                       "cover_url":"https://oss.zhiyun-tech.com/zyplaytest/templates/47/2020-04-13-13:43:11.png","status":""}

        class_111_1 = {"name":"","name_tw":"","name_en":"",
                       "cover_url":"https://oss.zhiyun-tech.com/zyplaytest/templates/47/2020-04-13-13:43:11.png","status":""}


        musicClassList = [class_011_0, class_011_1, class_101_0, class_101_1, class_110_0, class_110_1, class_111_1]

        url = 'http://47.99.180.185:3999/tpl/music/albums/createOrUpdate'
        for i in range(7):
            params = musicClassList[i]
            if i == 0:
                params['name'] = ''
                params['name_tw'] = 'tw'+str(times)
                params['name_en'] = 'en'+str(times)
                params['status'] = '0'

            if i == 1:
                params['name'] = ''
                params['name_tw'] = 'tw'+str(times)
                params['name_en'] = 'en'+str(times)
                params['status'] = '1'

            if i == 2:
                params['name'] = 'zh'+str(times)
                params['name_tw'] = ''
                params['name_en'] = 'en'+str(times)
                params['status'] = '0'

            if i == 3:
                params['name'] = 'zh'+str(times)
                params['name_tw'] = ''
                params['name_en'] = 'en'+str(times)
                params['status'] = '1'

            if i == 4:
                params['name'] = 'zh'+str(times)
                params['name_tw'] = 'tw'+str(times)
                params['name_en'] = ''
                params['status'] = '0'

            if i == 5:
                params['name'] = 'zh'+str(times)
                params['name_tw'] = 'tw'+str(times)
                params['name_en'] = ''
                params['status'] = '1'

            if i == 6:
                params['name'] = 'zh'+str(times)
                params['name_tw'] = 'tw'+str(times)
                params['name_en'] = 'en'+str(times)
                params['status'] = '1'

            res = post_req.post_model_b(sessionX, url, params)
            time.sleep(1)
            print(res)




if __name__ == '__main__':
    a = Editor_filter()
    a.filter_00()
    a.filter_000()


