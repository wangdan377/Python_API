'''
@Author: xiaomin
@Date: 2020-04-28 17:28:50
@LastEditTime: 2020-05-11 10:28:11
@LastEditors: xiaomin
@Description: 驱动的创建绑定解绑流程
@FilePath: \ioT-uat\Testcase\test12_driver01.py
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
import time,datetime

from Params.params import DriverTest01
from Common.test_init_data import initData
from Common.casefunction import CaseFunction
from Common.Requestsfun import requestMethod
from Common.comm import loginToken
from Common.config import Config


class DriverTest_01(loginToken):
    '''
    上传驱动文件-创建驱动-创建产品-绑定驱动-更新驱动-删除驱动失败-解绑驱动-删除驱动成功-查询驱动
    '''
    def test_driver_01(self):

        # '''数据初始化'''
        a=initData()
        a.initdata({'productName':'testdriver'})

        # 变量用来控制调取接口索引
        i=0

        '''获取test_driver1.yaml中的数据'''
        data=DriverTest01()
        request=requestMethod()
        urls=data.url
        headers=data.header
        para=data.data
        expcode=data.code

        '''给所有url补充域名'''
        url=[None]*len(urls)
        for n in range(0,len(urls)):
            if 'smallfile' not in urls[n]:
                url[n]=Config.host+urls[n]
            else:
                url[n]=urls[n]

        '''给所有接口添加token'''
        for n in range(0,len(headers)):
            headers[n].update(Authorization='bearer '+loginToken().token)

        '''实例化调用测试数据的类'''
        case_function=CaseFunction()

        '''上传驱动文件'''
        f1=open('\\ioT-uat\\testdriverfile.txt','rb')
        files={'file':('testdriverfile.text',f1,'text/plain')}
        print('\n'+url[i])
        print('------上传驱动文件入参------')
        print(para[i])
        response=request.get_post(url[i],headers[i],para[i],files)
        curcode=response.status_code
        print('------上传驱动文件返回------')
        print('status:%s'%str(curcode))
        print(str(response.text))
        f1.close()
        
        self.assertEqual(expcode[i],curcode)
        res_address=json.loads(response.text)
        address=res_address['host']+'/'+res_address['key']
        print('获取文件地址：'+str(address))
        i=i+1

        time.sleep(2)

        '''创建驱动'''
        print('\n'+url[i])
        print('------创建驱动入参------')
        createdriver=case_function.post_request(request,url[i],headers[i],para[i],{'fileUrl':address})
        curcode=createdriver.status_code
        print('------创建驱动返回------')
        print('status:%s'%str(curcode))
        print(createdriver.text) 
        self.assertEqual(expcode[i],curcode)
        res_driverid=json.loads(createdriver.text)
        driverid=res_driverid['driverId']
        print('获取driverid：'+str(driverid))
        i=i+1

        '''创建产品'''
        print('\n'+url[i])
        print('------创建产品入参------')
        createproduct=case_function.post_request(request,url[i],headers[i],para[i])
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
        binddriver=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys,'driverId':driverid})
        curcode=binddriver.status_code
        print('------绑定驱动返回------')
        print('status:%s'%str(curcode))
        print(binddriver.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''更新驱动'''
        print('\n'+url[i])
        print('------更新驱动入参------')
        updatedriver=case_function.post_request(request,url[i],headers[i],para[i],{'driverId':driverid})
        curcode=updatedriver.status_code
        print('------更新驱动返回------')
        print('status:%s'%str(curcode))
        print(updatedriver.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''删除驱动失败'''
        print('\n'+url[i])
        print('------删除驱动入参------')
        deletedriver=case_function.post_request(request,url[i],headers[i],para[i],{'driverId':driverid})
        curcode=deletedriver.status_code
        print('------删除驱动返回------')
        print('status:%s'%str(curcode))
        print(deletedriver.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''解绑驱动'''
        print('\n'+url[i])
        print('------解绑驱动入参------')
        unbinddriver=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys,'driverId':driverid})
        curcode=unbinddriver.status_code
        print('------解绑驱动返回------')
        print('status:%s'%str(curcode))
        print(unbinddriver.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''删除驱动成功'''
        print('\n'+url[i])
        print('------删除驱动入参------')
        deletedriver=case_function.post_request(request,url[i],headers[i],para[i],{'driverId':driverid})
        curcode=deletedriver.status_code
        print('------删除驱动返回------')
        print('status:%s'%str(curcode))
        print(deletedriver.text)
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''查询驱动'''
        print('\n'+url[i])
        getdriver=case_function.get_request(request,url[i],headers[i],para[i],{'driverId':driverid})
        curcode=getdriver.status_code
        print('------查询驱动返回------')   
        print('status:%s'%str(curcode))
        print(getdriver.text)
        self.assertEqual(expcode[i],curcode)
        
        '''数据清理'''
        a.initdata({'productName':'testdriver'})


if __name__ == '__main__':
    unittest.main(verbosity=2)