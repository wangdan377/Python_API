import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

class Official_01:
#相机品牌列表(移动端文件)
    def Off_01(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/camera/cameraBrandListFile'


        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#相机型号列表(移动端文件)
    def Off_02(self,cameraBrand):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/camera/cameraModelListFile?cameraBrand='+cameraBrand


        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#相机镜头列表(移动端文件)
    def Off_03(self,cameraModel):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseListFile?cameraModel='+cameraModel


        res = post_req.post_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#支持查询_移动端
    def Off_04(self,productModel,cameraBrand,cameraModel,lense):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/camera/cameraSupportQueryApp?lang=zh_cn&productModel='+productModel+'&cameraModel='+cameraModel+'&cameraBrand='+cameraBrand+'&lense='+lense


        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#相机型号列表(模糊查询)
    def Off_05(self,productTitle,productModel,cameraModel):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/camera/cameraModelListLike?cameraModel='+cameraModel+'&productTitle='+productTitle+'&productModel='+productModel


        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#相机镜头列表(模糊查询)
    def Off_06(self,cameraLense):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/camera/cameraLenseListLike?cameraLense='+cameraLense

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')



if __name__ == '__main__':
    a = Official_01()
    a.Off_06()
