import pytest
import allure
import requests
import json
import time

from Templight import GetMysqlData

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

class Official_01:
#商城首页
    def Off_01(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/mainpage'
        params = {'lang':'zh_cn'}

        time.sleep(1)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#商城页面布局
    def Off_02(self):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/storelayout'
        params = {'code':'share_banner', 'lang':'zh_cn'}

        time.sleep(1)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#商品列表
    def Off_03(self,categoryId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/sku/list'
        params = { 'lang':'zh_cn', 'categoryId':'1'}

        params['categoryId'] = str(categoryId)

        time.sleep(1)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#商品详情
    def Off_04(self,skuId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/sku/detail'
        params = { 'skuId':'1'}

        params['skuId'] = str(skuId)

        time.sleep(1)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#购物车新增
    def Off_05(self,userId,skuId,number):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/shoppingcart/add'
        params = {'token':'12345678901234567890123456789012', 'skuId':'1','num':'1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        params['skuId'] = str(skuId)
        params['num'] = str(number)

        time.sleep(1)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#购物车修改
#isChecked--int 0取消勾选,1勾选
    def Off_06(self,userId,skuId,number):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/shoppingcart/update'
        params = {'token': '12345678901234567890123456789012', 'skuId': '1', 'num': '1', 'isChecked': 1}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        params['skuId'] = str(skuId)
        params['num'] = str(number)

        time.sleep(1)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#购物车列表
#isChecked--int	0返回所有商品,1返回已勾选商品
    def Off_07(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/shoppingcart/list'
        params = { 'token':'12345678901234567890123456789012','isChecked':0}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        time.sleep(1)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#地址修改
#id--string有则更新,否则新增
    def Off_08(self,userId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/address/update'
        params = {'token': '12345678901234567890123456789012', 'addressee': '胡健', 'mobile': '+8613418483933', 'phone': '075512345678','country': '中国','region': '广东 深圳 龙华区 ','address': '瓦窑排村','isDefault': '1'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        time.sleep(1)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#地址列表
    def Off_09(self,userId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/address/list'
        params = { 'token':'12345678901234567890123456789012'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        time.sleep(1)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#订单提交
    def Off_10(self,userId,addressId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/order/submit'
        params = {'token': '12345678901234567890123456789012', 'addressId': '1', 'payMode': '1', 'expressMode': '1','invoiceType': '企业','invoiceTitle': '智神信息科技有限公司','invoiceNo': '1234567890','invoiceContent': '明细'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        params['addressId'] = str(addressId)

        time.sleep(1)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#订单详情
    def Off_11(self,userId,orderId):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/order/detail'
        params = { 'token':'12345678901234567890123456789012','orderNo':'1234567890123456'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        params['orderNo'] = str(orderId)

        time.sleep(1)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#订单列表
#orderStatus string	订单状态,可选,10订单提交成功/待买家付款 20买家付款成功/待发货
#30卖家已发货/待收货 40买家已收货/完成 50售后 80订单关闭（终态）/超时未支付/手动取消  7月19日改动 订单 orderStatus 去掉售后50状态

    def Off_12(self,userId,orderStatus):
        sessionX = requests.session()
        get_req = Get.Get()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/order/list'
        params = { 'token':'12345678901234567890123456789012','orderStatus':'10'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        params['orderStatus'] = str(orderStatus)

        time.sleep(1)

        res = get_req.get_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#取消订单
    def Off_13(self,userId,orderId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/order/cancel'
        params = {'token': '12345678901234567890123456789012', 'orderNo': '1234567890123456'}

        data = GetMysqlData.GetMysqlData()
        tokenData = data.getTokenByUserId(userId)
        params['token'] = tokenData

        params['orderNo'] = str(orderId)

        time.sleep(1)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')

#订单确认收货
    def Off_14(self,userId,orderId):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://172.16.2.101:3000/v1/store/order/confirm_recv'
        params = {'token': '12345678901234567890123456789012', 'orderNo': '12345678901234567890123456789012'}

        time.sleep(1)

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')



if __name__ == '__main__':
    a = Official_01()
    a.Off_14()
