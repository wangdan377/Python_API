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


#相机支持列表
    def Off_01(self,cameraBrand):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraSupportList?cameraBrand='+cameraBrand

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机品牌列表
    def Off_02(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraBrandList'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机型号列表
    def Off_03(self,cameraBrand):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraModelList?cameraBrand='+cameraBrand

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#稳定器品牌列表
    def Off_04(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/productTitleList'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#支持表回显
#id--int支持列表编号
    def Off_05(self,id):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/editQuery?id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#支持编辑
#id--int 支持列表id(新增时不传)
#type--int	0不支持1支持2未知
#detailList	json 支持功能详情(存[{lang:'zh_cn',supportDetail:'fsd'}]的json字符串)
    def Off_06(self):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/editSubmit'
        params = {'productTitle':'CRANE 3 S','productModel':'1582533285286','cameraBrand':'Canon','cameraModel':'enenen',\
                  'type':2,'lense':'EF 70-300mm f/4-5.6L IS USM','detailList':[{"lang":"zh_cn","supportDetail":"不知道"}]}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


    def Off_06_edit(self,id):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/editSubmit'
        params = {'id':1, 'productTitle':'CRANE 3 S','productModel':'1582533285286','cameraBrand':'Canon','cameraModel':'enenen',\
                  'type':2,'lense':'EF 70-300mm f/4-5.6L IS USM','detailList':[{"lang":"zh_cn","supportDetail":"不知道"}]}

        params['id'] = id

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#查询记录列表
    def Off_07(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/queryRecordList'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#删除相机支持
#id-int	支持列表id
    def Off_08(self,id):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraDelSupport?id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机镜头列表
    def Off_09(self,cameraModel):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseList?cameraModel='+cameraModel

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机镜头绑定列表
    def Off_10(self,cameraModel):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseSupportList?cameraModel='+cameraModel

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机镜头绑定
    def Off_11(self):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseSupport'
        params = {'cameraBrand':'Canon', 'cameraModel':'again', \
                  'cameraLenses':'Sigma~24-70mm F2.8 DG OS HSM A Nikon,Sigma~12-24mm F4 DG HSM A Canon',\
                  'cameraImgUrl':'', 'type':''}

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#导出查询记录
    def Off_12(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/queryRecordListExcel'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '.xml')
        Consts.RESULT_LIST.append('True')


#相机型号列表(模糊查询)
    def Off_13(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraModelListLike?cameraModel=alp'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机镜头列表(模糊查询)
    def Off_14(self,cameraLense):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseListLike?cameraLense='+cameraLense

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机镜头绑定删除
#id--int相机数据管理列表编号
    def Off_15(self,id):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseSupportDel?id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#镜头数据管理列表
    def Off_16(self,cameraLense):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseDataList?cameraLense='+cameraLense

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机镜头编辑回显
#id--int相机镜头型号列表编号
    def Off_17(self,id):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseDataQuery?id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机镜头编辑提交
#id--int 相机镜头型号列表编号(新增时不传)
#name--string	相机镜头型号
#image--string	相机镜头图片地址url
    def Off_18(self,name):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseDataEditSubmit'
        params = {'name': 'huaxia', 'image': '//cdn.dxomark.com/dakdata/xml/EOS_1Ds_Mark_II/vignette3.png'}

        params['name'] = name

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


    def Off_18_edit(self, id,name):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseDataEditSubmit'
        params = {'id':1, 'name': 'huaxiaedit', 'image': '//cdn.dxomark.com/dakdata/xml/EOS_1Ds_Mark_II/vignette3.png'}

        params['name'] = name
        params['id'] = id

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机镜头删除
#id--int  相机镜头型号列表编号
    def Off_19(self,id):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseDataDel?id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机镜头绑定编辑回显
#id--int 相机镜头型号列表编号
    def Off_20(self,id):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseSupportEditQuery?id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机镜头绑定编辑提交
#id	int	相机镜头绑定列表编号
#cameraModel	string	相机型号
#cameraLense	string	镜头型号,编辑时只能传一个
#cameraImgUrl	string	相机图片
    def Off_21(self,id):
        sessionX = self.Off_00()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseSupportEditSubmit'
        params = {'id': 1, 'cameraBrand': 'Canon', 'cameraModel': 'again', \
                  'cameraLense':'Sony~FE 100-400mm F4.5-5.6 GM OSS',\
                  'cameraImgUrl': '//cdn.dxomark.com/dakdata/xml/EOS_1Ds_Mark_II/vignette3.png','type':'2'}

        params['id'] = id

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机镜头绑定批量编辑提交
#id	int	相机数据管理列表编号
#cameraBrand	string	相机品牌
#cameraModel	string	相机型号
#cameraLenses	string	镜头型号,多个用英文逗号隔开
#cameraImgUrl	string	相机图片
#type	int	相机数据是否为raw,即为相机数据管理列表的type字段
#注意：type为1时，不能修改相机数据；根据回显的lenseArr中的type字段确定是否能删除该支持的镜头型号）
    def Off_22(self,id):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseSupportBattleEditSubmit'
        params = {'id': 1, 'cameraBrand': 'Canon', 'cameraModel': 'again', \
                  'cameraLenses': 'Sigma~12-24mm F4 DG HSM A Canon','cameraImgUrl': '//cdn.dxomark.com/dakdata/xml/EOS_1000D/vignette3.png','type': 2}

        params['id'] = id

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机镜头绑定编辑回显(改版通过cameraModel聚合)
    def Off_23(self,brand,cameraModel):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseSupportGroupByCameraModelEditQuery?cameraModel='+cameraModel+'&brand='+brand

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#相机镜头绑定删除(改版通过cameraModel聚合)
    def Off_24(self,brand,cameraModel):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraLenseSupportGroupByCameraModelDel?cameraModel='+cameraModel+'&brand='+brand

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#支持功能管理一级列表
    def Off_25(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraSupportFirstList'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#支持功能管理一级列表查看
    def Off_26(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraSupportFirstListQuery?cameraModel=again&cameraBrand=Canon&productModel=1582533285286&productTitle=CRANE 3 S'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#支持功能管理一级列表删除
    def Off_27(self):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraSupportFirstListDel?cameraModel=again&cameraBrand=Canon&productModel=1582533285286&productTitle=CRANE 3 S'

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#支持功能管理二级列表删除
#id--int二级列表的编号
    def Off_28(self,id):
        sessionX = self.Off_00()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3999/camera/cameraSupportSecondListDel?id='+str(id)

        res = get_req.get_model_a(sessionX, url)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == '__main__':
    a = Official_01()
    a.Off_14()
