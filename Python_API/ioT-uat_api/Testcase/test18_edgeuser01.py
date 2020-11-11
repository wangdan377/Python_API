'''
@Author: xiaomin
@Date: 2020-05-09 17:22:09
@LastEditTime: 2020-05-11 15:48:37
@LastEditors: xiaomin
@Description: 用户的边缘计算流程
@FilePath: \ioT-uat\Testcase\test18_edgeuser01.py
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
import time

from Params.params import EdgeuserTest01
from Common.test_init_data import initData
from Common.casefunction import CaseFunction
from Common.Requestsfun import requestMethod
from Common.comm import loginToken
from Common.config import Config


@ddt.ddt
class EdgeuserTest_01(loginToken):
    '''
    开发者创建边缘网关产品-开发者创建边缘网关设备-用户查询边缘实例详情-用户绑定至网关-用户绑定驱动-开发者查询实例驱动-用户配置驱动-开发者查询驱动配置-用户绑定子设备-用户查询实例设备-用户实例部署
    '''  
    def test_edgeuser_01(self):

        # '''数据初始化'''
        a=initData()
        a.initdata({'productName':'apitest_autoEdge'})
        a.initdata({'productName':'apitest_autoSub'})

        # 变量用来控制调取接口索引
        i=0

        '''获取test_edgeuser.yaml中的数据'''
        data=EdgeuserTest01()
        request=requestMethod()
        urls=data.url
        headers=data.header
        para=data.data
        expcode=data.code

        '''给所有url补充域名'''
        url=[None]*len(urls)
        for n in range(0,len(urls)):
            if 'oauth/login' not in urls[n]:
                url[n]=Config.host+urls[n]
            else:
                url[n]=urls[n]

        '''登录用户'''
        print('\n'+url[i])
        print('------登录用户入参------')
        print(para[i])
        response=request.get_post(url[i],headers[i],para[i])
        res_usrtoken=json.loads(response.text)
        curcode=response.status_code
        print('------登录用户返回------')
        print('status:%s'%str(curcode))
        print(str(response.text))       
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''给接口添加token'''
        for n in range(1,len(headers)):
            if 'Owner' not in urls[n]:
                #开发者接口
                headers[n].update(Authorization='bearer '+loginToken().token)
            else:
                #用户接口
                headers[n].update(Authorization=res_usrtoken['token_type']+' '+res_usrtoken['access_token'])
            

        '''实例化调用测试数据的类'''
        case_function=CaseFunction()  

        '''开发者创建产品'''
        print('\n'+url[i])
        print('------开发者创建产品入参------')
        createproduct=case_function.post_request(request,url[i],headers[i],para[i])
        curcode=createproduct.status_code
        print('------开发者创建产品返回------')
        print('status:%s'%str(curcode))
        print(createproduct.text)
        self.assertEqual(expcode[i],curcode)
        createproduct=json.loads(createproduct.text)
        productkeys=createproduct['productKey']
        print('获取产品Key：'+productkeys)
        i=i+1

        '''开发者创建设备'''
        print('\n'+url[i])
        print('------开发者创建设备入参------')
        createdevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=createdevice.status_code
        print('------开发者创建设备返回------')
        print('status:%s'%str(curcode))
        print(createdevice.text)        
        self.assertEqual(expcode[i],curcode)
        deviceinfo=json.loads(createdevice.text)
        devicesecret=deviceinfo['deviceSecret']
        i=i+1

        '''用户绑定至网关'''
        print('\n'+url[i])
        print('------用户绑定至网关入参------')
        binduser=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys,'deviceSecret':devicesecret})
        curcode=binduser.status_code
        print('------用户绑定至网关返回------')
        print('status:%s'%str(curcode))
        print(str(binduser.text))
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''用户查询设备详情'''
        print('\n'+url[i])
        getdevice=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=getdevice.status_code
        print('------用户查询设备详情返回------')
        print('status:%s'%str(curcode))
        print(getdevice.text)
        self.assertIn(expcode[i],getdevice.text)
        deviceinstance=json.loads(getdevice.text)
        instanceid=deviceinstance['instanceId']
        print('获取实例id：'+instanceid)
        i=i+1

        '''用户绑定驱动'''
        print('\n'+url[i])
        print('------用户绑定驱动入参------')
        binddriver=case_function.post_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=binddriver.status_code
        print('------用户绑定驱动返回------')
        print('status:%s'%str(curcode))
        print(binddriver.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''开发者查询驱动'''
        print('\n'+url[i])
        getdriver=case_function.get_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=getdriver.status_code
        print('------开发者查询驱动返回------')   
        print('status:%s'%str(curcode))
        print(getdriver.text)
        self.assertIn(expcode[i],getdriver.text)
        i=i+1

        '''用户配置驱动'''
        print('\n'+url[i])
        print('------用户配置驱动入参------')
        setdriver=case_function.post_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=setdriver.status_code
        print('------用户配置驱动返回------')
        print('status:%s'%str(curcode))
        print(setdriver.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''开发者查询驱动配置'''
        print('\n'+url[i])
        getdriverconf=case_function.get_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=getdriverconf.status_code
        print('------开发者查询驱动配置返回------')   
        print('status:%s'%str(curcode))
        print(getdriverconf.text)
        self.assertIn(expcode[i],getdriverconf.text)
        i=i+1

        '''开发者创建子设备产品'''
        print('\n'+url[i])
        print('------创建子设备产品入参------')
        createsubproduct=case_function.post_request(request,url[i],headers[i],para[i])
        curcode=createsubproduct.status_code
        print('------创建子设备产品返回------')
        print('status:%s'%str(curcode))
        print(createsubproduct.text)
        self.assertEqual(expcode[i],curcode)
        createsubproduct=json.loads(createsubproduct.text)
        subproductkeys=createsubproduct['productKey']
        print('获取子设备产品Key：'+subproductkeys)
        i=i+1

        '''开发者创建子设备'''
        print('\n'+url[i])
        print('------创建设备入参------')
        createsubdevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':subproductkeys})
        curcode=createsubdevice.status_code
        print('------创建设备返回------')
        print('status:%s'%str(curcode))
        print(createsubdevice.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''用户绑定子设备'''
        print('\n'+url[i])
        print('------用户绑定子设备入参------')
        para[i]['deviceKeys'][0]['productKey']=subproductkeys
        para[i]['instanceId']=instanceid
        bindsubdevice=case_function.post_request(request,url[i],headers[i],para[i])
        curcode=bindsubdevice.status_code
        print('------用户绑定子设备返回------')
        print('status:%s'%str(curcode))
        print(bindsubdevice.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1
               
        '''用户查询实例设备'''
        print('\n'+url[i])
        getedgedevice=case_function.get_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=getedgedevice.status_code
        print('------用户查询实例设备返回------')   
        print('status:%s'%str(curcode))
        print(getedgedevice.text)
        self.assertIn(expcode[i],getedgedevice.text)
        i=i+1
       
        '''用户创建实例部署单'''
        print('\n'+url[i])
        print('------用户创建实例部署单入参------')
        createdeploy=case_function.post_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=createdeploy.status_code
        print('------用户创建实例部署单返回------')
        print('status:%s'%str(curcode))
        print(createdeploy.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''数据清理'''
        a.initdata({'productName':'apitest_autoEdge'})
        a.initdata({'productName':'apitest_autoSub'})


if __name__ == '__main__':
    unittest.main(verbosity=2)