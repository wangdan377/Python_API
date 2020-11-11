'''
@Author: xiaomin
@Date: 2020-05-09 14:45:42
@LastEditTime: 2020-05-11 11:15:40
@LastEditors: xiaomin
@Description: 开发者的边缘计算流程
@FilePath: \ioT-uat\Testcase\test17_edgedev01.py
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

from Params.params import EdgedevTest01
from Common.test_init_data import initData
from Common.casefunction import CaseFunction
from Common.Requestsfun import requestMethod
from Common.comm import loginToken
from Common.config import Config


@ddt.ddt
class EdgeTest_01(loginToken):
    '''
    创建边缘网关产品-创建边缘网关设备-查询边缘实例详情-绑定驱动-查询实例驱动-配置驱动-查询驱动配置-绑定子设备-查询实例设备-解绑驱动失败-配置实例设备-查询实例设备配置-实例部署-查询部署单-清空实例设备配置-查询实例设备配置-清空驱动配置-查询驱动配置-解绑子设备-查询实例设备-解绑驱动-查询实例驱动-实例部署-查询部署单
    '''  
    def test_edgedev_01(self):

        # '''数据初始化'''
        a=initData()
        a.initdata({'productName':'apitest_autoEdge'})
        a.initdata({'productName':'apitest_autoSub'})

        # 变量用来控制调取接口索引
        i=0

        '''获取test_device1.yaml中的数据'''
        data=EdgedevTest01()
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

        '''创建设备'''
        print('\n'+url[i])
        print('------创建设备入参------')
        createdevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=createdevice.status_code
        print('------创建设备返回------')
        print('status:%s'%str(curcode))
        print(createdevice.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''查询设备详情'''
        print('\n'+url[i])
        getdevice=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=getdevice.status_code
        print('------查询设备返回------')   
        print('status:%s'%str(curcode))
        print(getdevice.text)
        self.assertIn(expcode[i],getdevice.text)
        deviceinstance=json.loads(getdevice.text)
        instanceid=deviceinstance['instanceId']
        print('获取实例id：'+instanceid)
        i=i+1

        '''绑定驱动'''
        print('\n'+url[i])
        print('------绑定驱动入参------')
        binddriver=case_function.post_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=binddriver.status_code
        print('------绑定驱动返回------')
        print('status:%s'%str(curcode))
        print(binddriver.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''查询驱动'''
        print('\n'+url[i])
        getdriver=case_function.get_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=getdriver.status_code
        print('------查询驱动返回------')   
        print('status:%s'%str(curcode))
        print(getdriver.text)
        self.assertIn(expcode[i],getdriver.text)
        i=i+1

        '''配置驱动'''
        print('\n'+url[i])
        print('------配置驱动入参------')
        setdriver=case_function.post_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=setdriver.status_code
        print('------配置驱动返回------')
        print('status:%s'%str(curcode))
        print(setdriver.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''查询驱动配置'''
        print('\n'+url[i])
        getdriverconf=case_function.get_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=getdriverconf.status_code
        print('------查询驱动配置返回------')   
        print('status:%s'%str(curcode))
        print(getdriverconf.text)
        self.assertIn(expcode[i],getdriverconf.text)
        i=i+1

        '''创建子设备产品'''
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

        '''创建子设备'''
        print('\n'+url[i])
        print('------创建设备入参------')
        createsubdevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':subproductkeys})
        curcode=createsubdevice.status_code
        print('------创建设备返回------')
        print('status:%s'%str(curcode))
        print(createsubdevice.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''绑定子设备'''
        print('\n'+url[i])
        print('------绑定子设备入参------')
        para[i]['deviceKeys'][0]['productKey']=subproductkeys
        para[i]['instanceId']=instanceid
        bindsubdevice=case_function.post_request(request,url[i],headers[i],para[i])
        curcode=bindsubdevice.status_code
        print('------绑定子设备返回------')
        print('status:%s'%str(curcode))
        print(bindsubdevice.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1
               
        '''查询实例设备'''
        print('\n'+url[i])
        getedgedevice=case_function.get_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=getedgedevice.status_code
        print('------查询实例设备返回------')   
        print('status:%s'%str(curcode))
        print(getedgedevice.text)
        self.assertIn(expcode[i],getedgedevice.text)
        i=i+1

        '''解绑驱动'''
        print('\n'+url[i])
        print('------解绑驱动入参------')
        unbinddriver=case_function.post_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=unbinddriver.status_code
        print('------解绑驱动返回------')
        print('status:%s'%str(curcode))
        print(unbinddriver.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''配置设备'''
        print('\n'+url[i])
        print('------配置设备入参------')
        para[i]['deviceConfigs'][0]['productKey']=subproductkeys
        para[i]['instanceId']=instanceid
        setdevice=case_function.post_request(request,url[i],headers[i],para[i])
        curcode=setdevice.status_code
        print('------配置设备返回------')
        print('status:%s'%str(curcode))
        print(setdevice.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''查询设备配置'''
        print('\n'+url[i])
        getdeviceconf=case_function.get_request(request,url[i],headers[i],para[i],{'instanceId':instanceid,'deviceKeys[0].productKey':subproductkeys})
        curcode=getdeviceconf.status_code
        print('------查询设备配置返回------')   
        print('status:%s'%str(curcode))
        print(getdeviceconf.text)
        self.assertIn(expcode[i],getdeviceconf.text)
        i=i+1

        '''创建实例部署单'''
        print('\n'+url[i])
        print('------创建实例部署单入参------')
        createdeploy=case_function.post_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=createdeploy.status_code
        print('------创建实例部署单返回------')
        print('status:%s'%str(curcode))
        print(createdeploy.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''清空设备配置'''
        print('\n'+url[i])
        print('------清空设备配置入参------')
        para[i]['deviceKeys'][0]['productKey']=subproductkeys
        para[i]['instanceId']=instanceid
        setdevice=case_function.post_request(request,url[i],headers[i],para[i])
        curcode=setdevice.status_code
        print('------清空设备配置返回------')
        print('status:%s'%str(curcode))
        print(setdevice.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''查询设备配置'''
        print('\n'+url[i])
        getdeviceconf=case_function.get_request(request,url[i],headers[i],para[i],{'instanceId':instanceid,'deviceKeys[0].productKey':subproductkeys})
        curcode=getdeviceconf.status_code
        print('------查询设备配置返回------')   
        print('status:%s'%str(curcode))
        print(getdeviceconf.text)
        self.assertNotIn(expcode[i],getdeviceconf.text)
        i=i+1

        '''清空驱动配置'''
        print('\n'+url[i])
        print('------清空驱动配置入参------')
        setdriver=case_function.post_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=setdriver.status_code
        print('------清空驱动配置返回------')
        print('status:%s'%str(curcode))
        print(setdriver.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''查询驱动配置'''
        print('\n'+url[i])
        getdriverconf=case_function.get_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=getdriverconf.status_code
        print('------查询驱动配置返回------')   
        print('status:%s'%str(curcode))
        print(getdriverconf.text)
        self.assertNotIn(expcode[i],getdriverconf.text)
        i=i+1

        '''解绑子设备'''
        print('\n'+url[i])
        print('------解绑子设备参------')
        para[i]['deviceKeys'][0]['productKey']=subproductkeys
        para[i]['instanceId']=instanceid
        unbindsubdevice=case_function.post_request(request,url[i],headers[i],para[i])
        curcode=unbindsubdevice.status_code
        print('------解绑子设备返回------')
        print('status:%s'%str(curcode))
        print(unbindsubdevice.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''查询实例设备'''
        print('\n'+url[i])
        getedgedevice=case_function.get_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=getedgedevice.status_code
        print('------查询实例设备返回------')   
        print('status:%s'%str(curcode))
        print(getedgedevice.text)
        self.assertNotIn(expcode[i],getedgedevice.text)
        i=i+1

        '''解绑驱动'''
        print('\n'+url[i])
        print('------解绑驱动入参------')
        unbinddriver=case_function.post_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=unbinddriver.status_code
        print('------绑定驱动返回------')
        print('status:%s'%str(curcode))
        print(unbinddriver.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''查询驱动'''
        print('\n'+url[i])
        getdriver=case_function.get_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=getdriver.status_code
        print('------查询驱动返回------')   
        print('status:%s'%str(curcode))
        print(getdriver.text)
        self.assertNotIn(expcode[i],getdriver.text)
        i=i+1

        time.sleep(5)
        '''创建实例部署单'''
        print('\n'+url[i])
        print('------创建实例部署单入参------')
        createdeploy=case_function.post_request(request,url[i],headers[i],para[i],{'instanceId':instanceid})
        curcode=createdeploy.status_code
        print('------创建实例部署单返回------')
        print('status:%s'%str(curcode))
        print(createdeploy.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''数据清理'''
        a.initdata({'productName':'apitest_autoEdge'})
        a.initdata({'productName':'apitest_autoSub'})


if __name__ == '__main__':
    unittest.main(verbosity=2)