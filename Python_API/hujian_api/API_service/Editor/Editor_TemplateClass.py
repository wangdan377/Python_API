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

        class_001_11000 = {"label": "", "label_tw": "", "label_en": "class_001_11000",
                           "status": "1", "platfromIds": "1,2"}
        class_010_11011 = {"label": "", "label_tw": "class_010_11011", "label_en": "",
                           "status": "1", "platfromIds": "1,2,4,5"}
        class_011_01101 = {"label": "", "label_tw": "class_011_01101", "label_en": "class_011_01101",
                           "status": "1", "platfromIds": "2,3,5"}

        class_011_10110 = {"label": "", "label_tw": "class_011_10110", "label_en": "class_011_10110",
                           "status": "1", "platfromIds": "1,3,4"}
        class_101_10011 = {"label": "class_101_10011", "label_tw": "", "label_en": "class_101_10011",
                           "status": "1", "platfromIds": "1,4,5"}
        class_101_01110 = {"label": "class_101_01110", "label_tw": "", "label_en": "class_101_01110",
                           "status": "1", "platfromIds": "2,3,4"}

        class_100_11101 = {"label": "class_100_11101", "label_tw": "", "label_en": "",
                           "status": "1", "platfromIds": "1,2,3,5"}
        class_111_00001 = {"label": "class_111_00001", "label_tw": "class_111_00001", "label_en": "class_111_00001",
                           "status": "1", "platfromIds": "5"}
        class_110_10100 = {"label": "class_110_10100", "label_tw": "class_110_10100", "label_en": "",
                           "status": "1", "platfromIds": "1,3"}

        class_110_01010 = {"label": "class_110_01010", "label_tw": "class_110_01010", "label_en": "",
                           "status": "1", "platfromIds": "2,4"}
        class_111_11111 = {"label": "class_111_11111", "label_tw": "class_111_11111", "label_en": "class_111_11111",
                           "status": "1", "platfromIds": "1,2,3,4,5"}

        temClassList = [class_001_11000, class_010_11011, class_011_01101,
                        class_011_10110, class_101_10011, class_101_01110,
                        class_100_11101, class_111_00001, class_110_10100,
                        class_110_01010, class_111_11111]

        url = 'http://47.99.180.185:3999/video/templates/types/create_or_update'
        for i in range(11):
            params = temClassList[i]
            res = post_req.post_model_b(sessionX, url, params)
            time.sleep(1)
            print(res)




if __name__ == '__main__':
    a = Editor_filter()
    a.filter_00()
    a.filter_000()


