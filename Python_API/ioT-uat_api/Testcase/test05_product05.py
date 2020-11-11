'''
@Author: xiaomin
@Date: 2020-04-27 11:37:04
@LastEditTime: 2020-05-11 11:14:17
@LastEditors: xiaomin
@Description: 产品的分配驱动流程
@FilePath: \ioT-uat\Testcase\test05_product05.py
'''

import os
import sys
sys.path.append("..")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import unittest
import requests
import json
import ddt

from Params.params import ProductTest05
from Common.test_init_data import initData
from Common.casefunction import CaseFunction
from Common.Requestsfun import requestMethod
from Common.comm import loginToken
from Common.config import Config


@ddt.ddt
class ProductTest_05(loginToken):
    '''
    创建产品-绑定驱动-查询产品已绑定驱动-解绑驱动-删除产品成功-查询产品失败
    '''
    @ddt.data({'title':'直连产品','dataFormat':'1','networkType':'WIFI','productName':'apitest_auto13','productNodeType':'0','sub':'false'},
              {'title':'网关子设备产品','dataFormat':'0','networkType':'WIFI','productName':'apitest_auto14','productNodeType':'0','sub':'true'},
              {'title':'边缘网关产品','dataFormat':'1','networkType':'WIFI','productName':'apitest_auto15','productNodeType':'2','sub':'false'})
    @ddt.unpack
    def test_product_05(self,dataFormat,networkType,productName,productNodeType,sub,title):

        # '''数据初始化'''
        a=initData()
        a.initdata({'productName':productName})

        # 变量用来控制调取接口索引
        i=0

        '''获取test_product5.yaml中的数据'''
        data=ProductTest05()
        request=requestMethod()
        urls=data.url
        headers=data.header
        para=data.data
        expcode=data.code

        '''给所有url补充域名'''
        url=[None]*len(urls)
        for n in range(0,len(urls)):
            url[n]=Config.host+urls[n]

        '''给所有接口添加token'''
        for n in range(0,len(headers)):
            headers[n].update(Authorization='bearer '+loginToken().token)
            

        '''实例化调用测试数据的类'''
        case_function=CaseFunction()  

        '''创建产品'''
        print('\n'+url[i])
        print('------创建产品入参------')
        createproduct=case_function.post_request(request,url[i],headers[i],para[i],{'dataFormat':dataFormat,'networkType':networkType,'productNodeType':productNodeType,'productName':productName,'sub':sub})
        curcode=createproduct.status_code
        print('------创建产品返回------')
        print('status:%s'%str(curcode))
        print(createproduct.text)
        self.assertEqual(expcode[i],curcode)
        createproduct=json.loads(createproduct.text)
        productkeys=createproduct['productKey']
        print('获取产品Key：'+productkeys)
        i=i+1

        '''绑定驱动'''
        print('\n'+url[i])
        print('------绑定驱动入参------')
        binddriver=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=binddriver.status_code
        print('------绑定驱动返回------')
        print('status:%s'%str(curcode))
        print(str(binddriver.text))
        if para[0]['productName']=='apitest_auto13':           
            self.assertEqual(409,curcode)
            i=i+1
        else:
            self.assertEqual(expcode[i],curcode)
            i=i+1

        '''查询产品已绑定驱动'''
        print('\n'+url[i])
        getbinddriver=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=getbinddriver.status_code
        print('------查询产品Topic返回------')   
        print('status:%s'%str(curcode))
        print(getbinddriver.text)
        if para[0]['productName']=='apitest_auto13':           
            self.assertNotIn(expcode[i],getbinddriver.text)
            i=i+1           
        else:           
            self.assertIn(expcode[i],getbinddriver.text)
            i=i+1
            

        '''解绑驱动'''
        print('\n'+url[i])
        print('------解绑驱动入参------')
        unbinddriver=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=unbinddriver.status_code
        print('------解绑驱动返回------')
        print('status:%s'%str(curcode))
        print(str(unbinddriver.text))
        if para[0]['productName']=='apitest_auto13':           
            self.assertEqual(409,curcode)
            i=i+1           
        else:      
            self.assertEqual(expcode[i],curcode)
            i=i+1  

        '''删除产品:成功'''
        print('\n'+url[i])
        print('------删除产品入参------')
        deleteproduct=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=deleteproduct.status_code
        print('------删除产品返回------')
        print('status:%s'%str(curcode))
        print(deleteproduct.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1
        
        '''查询产品详情'''
        print('\n'+url[i])
        getproduct=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=getproduct.status_code
        print('------查询产品返回------')   
        print('status:%s'%str(curcode))
        print(getproduct.text)
        self.assertEqual(expcode[i],curcode)
                

if __name__ == '__main__':
    unittest.main(verbosity=2)



