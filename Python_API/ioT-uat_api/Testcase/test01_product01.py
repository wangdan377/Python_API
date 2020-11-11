'''
@Author: xiaomin
@Date: 2020-04-27 11:37:04
@LastEditTime: 2020-05-11 11:10:54
@LastEditors: xiaomin
@Description: 产品的发布与撤销流程
@FilePath: \ioT-uat\Testcase\test01_product01.py
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

from Params.params import ProductTest01
from Common.test_init_data import initData
from Common.casefunction import CaseFunction
from Common.Requestsfun import requestMethod
from Common.comm import loginToken
from Common.config import Config


@ddt.ddt
class ProductTest_01(loginToken):
    '''
    创建产品-发布产品-更新产品失败-删除产品失败-撤销发布-更新成功-增量更新标签-全量更新标签-查询产品-删除产品成功-查询列表
    '''
    @ddt.data({'title':'直连产品','dataFormat':'1','networkType':'WIFI','productName':'apitest_auto1','productNodeType':'0','sub':'false'},
              {'title':'网关子设备产品','dataFormat':'0','networkType':'WIFI','productName':'apitest_auto2','productNodeType':'0','sub':'true'},
              {'title':'边缘网关产品','dataFormat':'1','networkType':'WIFI','productName':'apitest_auto3','productNodeType':'2','sub':'false'})
    @ddt.unpack
    def test_product_01(self,dataFormat,networkType,productName,productNodeType,sub,title):

        # '''数据初始化'''
        a=initData()
        a.initdata({'productName':productName})

        # 变量用来控制调取接口索引
        i=0

        '''获取test_product1.yaml中的数据'''
        data=ProductTest01()
        request=requestMethod()
        urls=data.url
        headers=data.header
        para=data.data
        expcode=data.code

        '''给所有url补充域名'''
        url=[None]*len(urls)
        for n in range(0,len(urls)):
            url[n]=Config.host+urls[n]

        '''给所有header添加token'''
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

        '''发布产品'''
        print('\n'+url[i])
        print('------发布产品入参------')
        createproduct=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=createproduct.status_code
        print('------发布产品返回------')
        print('status:%s'%str(curcode))
        print(str(createproduct.text))     
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''更新产品:失败'''
        print('\n'+url[i])
        print('------更新产品入参------')
        updateproduct=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=updateproduct.status_code        
        print('------更新产品返回------')
        print('status:%s'%str(curcode))
        print(str(updateproduct.text))        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''删除产品:失败'''
        print('\n'+url[i])
        print('------删除产品入参------')
        deleteproduct=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=deleteproduct.status_code
        print('------删除产品返回------')
        print('status:%s'%str(curcode))
        print(deleteproduct.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''撤销发布产品'''
        print('\n'+url[i])
        print('------撤销产品入参------')
        cancelproduct=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=cancelproduct.status_code
        print('------撤销产品返回------')
        print('status:%s'%str(curcode))
        print(cancelproduct.text)  
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''更新产品:成功'''        
        print('\n'+url[i])
        print('------更新产品入参------')
        updateproduct=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=updateproduct.status_code
        print('------更新产品返回------')       
        print('status:%s'%str(curcode))
        print(updateproduct.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''增量更新标签'''
        print('\n'+url[i])
        print('------增量更新标签入参------')
        producttag=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=producttag.status_code
        print('------增量更新标签返回------')
        print('status:%s'%str(curcode))
        print(producttag.text)       
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''全量更新标签'''
        print('\n'+url[i])
        print('------全量更新标签入参------')
        producttags=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=producttags.status_code
        print('------全量更新标签入参------')       
        print('status:%s'%str(curcode))
        print(producttags.text)        
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
        

if __name__ == '__main__':
    unittest.main(verbosity=2)



